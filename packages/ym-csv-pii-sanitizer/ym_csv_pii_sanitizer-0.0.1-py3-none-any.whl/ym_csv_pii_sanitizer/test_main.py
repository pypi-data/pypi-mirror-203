from main import spacy_replace_entities_with_labels, replace_phone_numbers
from unittest.mock import patch, mock_open
from main import main
import os

def test_spacy_replace_entities_with_labels():
    test_input = "John Smith is a software engineer at Google."
    expected_output = "[PERSON] is a software engineer at [ORG]."
    assert spacy_replace_entities_with_labels(test_input) == expected_output

def test_replace_phone_numbers():
    test_input = "Call me at 212-456-7890."
    expected_output = "Call me at [PHONE_NUMBER]."
    assert replace_phone_numbers(test_input) == expected_output

def test_main_function():
    input_path = "ym_csv_pii_sanitizer/__test__/test.csv"
    output_path = "ym_csv_pii_sanitizer/__test__/test-sanitized.csv"
    expected_output = "First Name,Last Name,Description,Full Name\n[PERSON],Doe,[DATE] is [GPE] [PHONE_NUMBER] description,[PERSON]\n"

    main(input_path, output_path)
    with open(output_path, mode='r') as f:
            actual_output = f.read()
  
    assert actual_output == expected_output

    os.remove(output_path)
