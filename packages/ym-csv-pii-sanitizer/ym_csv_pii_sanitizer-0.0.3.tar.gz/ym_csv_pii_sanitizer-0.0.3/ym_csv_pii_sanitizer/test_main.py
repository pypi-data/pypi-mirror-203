from .main import main
import os


def test_main_function():
    input_path = "ym_csv_pii_sanitizer/__test__/test.csv"
    output_path = "ym_csv_pii_sanitizer/__test__/test-sanitized.csv"
    expected_output = "First Name,Last Name,Description,Full Name\n<PER>,\
<PER>e,this <US_DRIVER_LICENSE> is <LOC> <PHONE_NUMBER> description,<PER>\n"

    main(input_path, output_path)
    with open(output_path, mode='r') as f:
        actual_output = f.read()

    assert actual_output == expected_output

    os.remove(output_path)
