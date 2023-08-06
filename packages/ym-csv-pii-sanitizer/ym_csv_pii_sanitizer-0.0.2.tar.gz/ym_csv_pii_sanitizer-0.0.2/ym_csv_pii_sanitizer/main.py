import typer
import csv
from pathlib import Path
from typing import Optional
import spacy
from phonenumbers import PhoneNumberMatcher

nlp = spacy.load('en_core_web_sm')
# PERSON:      People, including fictional.
# NORP:        Nationalities or religious or political groups.
# FAC:         Buildings, airports, highways, bridges, etc.
# ORG:         Companies, agencies, institutions, etc.
# GPE:         Countries, cities, states.
# LOC:         Non-GPE locations, mountain ranges, bodies of water.
# PRODUCT:     Objects, vehicles, foods, etc. (Not services.)
# EVENT:       Named hurricanes, battles, wars, sports events, etc.
# WORK_OF_ART: Titles of books, songs, etc.
# LAW:         Named documents made into laws.
# LANGUAGE:    Any named language.
# DATE:        Absolute or relative dates or periods.
# TIME:        Times smaller than a day.
# PERCENT:     Percentage, including ”%“.
# MONEY:       Monetary values, including unit.
# QUANTITY:    Measurements, as of weight or distance.
# ORDINAL:     “first”, “second”, etc.
# CARDINAL:    Numerals that do not fall under another type.

# all except ORDINAL and CARDINAL
ent_labels_to_redact = ['DATE', 'EVENT', 'FAC', 'GPE', 'LANGUAGE', 'LAW', 'LOC', 'MONEY', 'NORP', 'ORG', 'PERCENT', 'PERSON', 'PRODUCT', 'QUANTITY', 'TIME', 'WORK_OF_ART']

def spacy_replace_entities_with_labels(text):
    spacy_doc = nlp(text)
    spacy_entities = spacy_doc.ents
    if len(spacy_entities) > 0:
        for ent in spacy_entities:
            if ent.label_ in ent_labels_to_redact:
                text = text.replace(ent.text, f"[{ent.label_}]")

    return text

def replace_phone_numbers(text):
    phone_numbers = [match.raw_string for match in PhoneNumberMatcher(text, region='US')]
    for phone_number in phone_numbers:
        text = text.replace(phone_number, "[PHONE_NUMBER]")
    return text

def main(
    input_path: Path = typer.Argument(..., exists=True, dir_okay=False, help="Path to csv file to sanitize.",),
    output_path: Optional[Path] = typer.Argument(None, dir_okay=False, help="Optional output path for result csv file.",)
    ):

    output_suffix = '-sanitized'
    # default to be the same as the input file, but with -sanitized added before the CSV file extension.
    if output_path is None: 
        output_file_name = f"{input_path.stem}{output_suffix}.csv"
        output_path = f"{input_path.parent}/{output_file_name}"

    # open input and output files
    with open(input_path, mode='r') as input_file,open(output_path, mode='w') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        # iterate every row and column
        for row in reader:
            output_row = []
            for item in row:
                # redact using spacy
                redacted_item = spacy_replace_entities_with_labels(item)
                # redact phone numbers
                redacted_item = replace_phone_numbers(redacted_item)

                output_row.append(redacted_item)
            
            writer.writerow(output_row)

def run():
    typer.run(main)

if __name__ == "__main__":
    run()