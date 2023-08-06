import typer
import csv
from pathlib import Path
from typing import Optional, List, Tuple, Set
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
from presidio_anonymizer import AnonymizerEngine
from presidio_analyzer import (
    RecognizerResult,
    EntityRecognizer,
    AnalysisExplanation,
)
from presidio_analyzer.nlp_engine import NlpArtifacts

try:
    from transformers import (
        AutoTokenizer,
        AutoModelForTokenClassification,
        pipeline,
    )
    from transformers.models.bert.modeling_bert import (
        BertForTokenClassification
    )
except ImportError:
    print("transformers is not installed")


class TransformersRecognizer(EntityRecognizer):
    """
    Wrapper for a transformers model,
    if needed to be used within Presidio Analyzer.
    :example:
    >from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
    >transformers_recognizer = TransformersRecognizer()
    >registry = RecognizerRegistry()
    >registry.add_recognizer(transformers_recognizer)
    >analyzer = AnalyzerEngine(registry=registry)
    >results = analyzer.analyze(
    >    "My name is Christopher and I live in Irbid.",
    >    language="en",
    >    return_decision_process=True,
    >)
    >for result in results:
    >    print(result)
    >    print(result.analysis_explanation)
    """

    ENTITIES = [
        "LOCATION",
        "PERSON",
        "ORGANIZATION",
        "AGE",
        "ID",
        "PHONE_NUMBER",
        "EMAIL",
        "DATE",
    ]

    DEFAULT_EXPLANATION = "Identified as {} by transformers's\
Named Entity Recognition"

    CHECK_LABEL_GROUPS = [
        ({"LOCATION"}, {"LOC", "HOSP"}),
        ({"PERSON"}, {"PER", "PERSON", "STAFF", "PATIENT"}),
        ({"ORGANIZATION"}, {"ORGANIZATION", "ORG", "PATORG"}),
        ({"AGE"}, {"AGE"}),
        ({"ID"}, {"ID"}),
        ({"EMAIL"}, {"EMAIL"}),
        ({"DATE"}, {"DATE"}),
        ({"PHONE_NUMBER"}, {"PHONE"}),
    ]

    PRESIDIO_EQUIVALENCES = {
        "PER": "PERSON",
        "LOC": "LOCATION",
        "ORG": "ORGANIZATION",
        "AGE": "AGE",
        "ID": "ID",
        "EMAIL": "EMAIL",
        "PATIENT": "PERSON",
        "STAFF": "PERSON",
        "HOSP": "LOCATION",
        "PATORG": "ORGANIZATION",
        "DATE": "DATE_TIME",
        "PHONE": "PHONE_NUMBER",
    }

    DEFAULT_MODEL_PATH = "obi/deid_roberta_i2b2"

    def __init__(
        self,
        supported_entities: Optional[List[str]] = None,
        check_label_groups: Optional[Tuple[Set, Set]] = None,
        model: Optional[BertForTokenClassification] = None,
        model_path: Optional[str] = None,
    ):
        if not model and not model_path:
            model_path = self.DEFAULT_MODEL_PATH

        if model and model_path:
            print(
                "Both 'model' and 'model_path' arguments were provided.\
                Ignoring the model_path"
            )

        self.check_label_groups = (
            check_label_groups if check_label_groups
            else self.CHECK_LABEL_GROUPS
        )

        supported_entities = (supported_entities if supported_entities
                              else self.ENTITIES)
        self.model = (
            model
            if model
            else pipeline(
                "ner",
                model=AutoModelForTokenClassification.from_pretrained(
                    model_path),
                tokenizer=AutoTokenizer.from_pretrained(model_path),
                aggregation_strategy="simple",
            )
        )

        super().__init__(
            supported_entities=supported_entities,
            name="transformers Analytics",
        )

    def load(self) -> None:
        """Load the model, not used. Model is loaded during initialization."""
        pass

    def get_supported_entities(self) -> List[str]:
        """
        Return supported entities by this model.
        :return: List of the supported entities.
        """
        return self.supported_entities

    # Class to use transformers with Presidio as an external recognizer.
    def analyze(
        self, text: str, entities: List[str],
        nlp_artifacts: NlpArtifacts = None
    ) -> List[RecognizerResult]:
        """
        Analyze text using Text Analytics.
        :param text: The text for analysis.
        :param entities: Not working properly for this recognizer.
        :param nlp_artifacts: Not used by this recognizer.
        :return: The list of Presidio RecognizerResult
        constructed from the recognized
            transformers detections.
        """

        results = []
        ner_results = self.model(text)

        # If there are no specific list of entities,
        # we will look for all of it.
        if not entities:
            entities = self.supported_entities

        for entity in entities:
            if entity not in self.supported_entities:
                continue

            for res in ner_results:
                if not self.__check_label(
                    entity, res["entity_group"], self.check_label_groups
                ):
                    continue
                textual_explanation = self.DEFAULT_EXPLANATION.format(
                    res["entity_group"]
                )
                explanation = self.build_transformers_explanation(
                    round(res["score"], 2), textual_explanation
                )
                transformers_result = self._convert_to_recognizer_result(
                    res, explanation
                )

                results.append(transformers_result)

        return results

    def _convert_to_recognizer_result(self,
                                      res, explanation) -> RecognizerResult:

        entity_type = self.PRESIDIO_EQUIVALENCES.get(
            res["entity_group"], res["entity_group"]
        )
        transformers_score = round(res["score"], 2)

        transformers_results = RecognizerResult(
            entity_type=entity_type,
            start=res["start"],
            end=res["end"],
            score=transformers_score,
            analysis_explanation=explanation,
        )

        return transformers_results

    def build_transformers_explanation(
        self, original_score: float, explanation: str
    ) -> AnalysisExplanation:
        """
        Create explanation for why this result was detected.
        :param original_score: Score given by this recognizer
        :param explanation: Explanation string
        :return:
        """
        explanation = AnalysisExplanation(
            recognizer=self.__class__.__name__,
            original_score=original_score,
            textual_explanation=explanation,
        )
        return explanation

    @staticmethod
    def __check_label(
        entity: str, label: str, check_label_groups: Tuple[Set, Set]
    ) -> bool:
        return any(
            [entity in egrp and label in lgrp for egrp,
             lgrp in check_label_groups]
        )


transformers_recognizer = (
    TransformersRecognizer()
)  # This would download a large (~500Mb) model on the first run

ner = pipeline("ner", aggregation_strategy="simple",
               model="dbmdz/bert-large-cased-finetuned-conll03-english")

registry = RecognizerRegistry()
registry.add_recognizer(transformers_recognizer)

analyzer = AnalyzerEngine(registry=registry)
defaultAnalyzer = AnalyzerEngine()
engine = AnonymizerEngine()


def presidio_custom_replace(text):
    analyzer_results = analyzer.analyze(text=text, language="en",
                                        return_decision_process=True)

    result = engine.anonymize(
        text=text, analyzer_results=analyzer_results
    )
    return result.text


def presidio_default_replace(text):
    analyzer_results = defaultAnalyzer.analyze(text=text, language="en",
                                               return_decision_process=True)

    result = engine.anonymize(
        text=text, analyzer_results=analyzer_results
    )
    return result.text


def ner_replace_default(text):
    output = ner(text)
    if len(output) > 0:
        for ent in output:
            text = text.replace(ent['word'], f"<{ent['entity_group']}>")

    return text


def main(
    input_path: Path = typer.Argument(..., exists=True,
                                      dir_okay=False,
                                      help="Path to csv file to sanitize.",),
    output_path: Optional[Path] = typer.Argument(
        None, dir_okay=False, help="Optional output path for result csv file.")
):

    output_suffix = '-sanitized'
    # default to be the same as the input file,
    # but with -sanitized added before the CSV file extension.
    if output_path is None:
        output_file_name = f"{input_path.stem}{output_suffix}.csv"
        output_path = f"{input_path.parent}/{output_file_name}"

    # open input and output files
    with open(input_path, mode='r') as input_file, \
            open(output_path, mode='w') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        # iterate every row and column
        for row in reader:
            output_row = []
            for item in row:
                redacted_item = ner_replace_default(item)

                redacted_item = presidio_default_replace(redacted_item)

                redacted_item = presidio_custom_replace(redacted_item)

                output_row.append(redacted_item)

            writer.writerow(output_row)


def run():
    typer.run(main)


if __name__ == "__main__":
    run()
