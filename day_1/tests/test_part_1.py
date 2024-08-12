import pytest
import os

import sys

# Add the parent directory to the path so all folders are accessible
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)

import solution.part_1

@pytest.fixture
def test_list_of_calibration_values_setup():
    """ Returns a list (test_calibration_values) containing all the calibration values needed to calculate the answer
    """
    
    test_calibration_values = []

    # Open text file containing the correct calibration values
    test_calibration_values_file_name = "part_1_calibration_values.txt"
    file_path = os.path.join(parent_dir, test_calibration_values_file_name)
    test_calibration_value_document = open(file_path, "r")
    test_calibration_value_document_lines = test_calibration_value_document.readlines()
    test_calibration_value_document.close()

    for line in test_calibration_value_document_lines:
        test_calibration_values.append(int(line))

    return test_calibration_values

def test_answer_is_correct():

    answer_document = solution.part_1.open_file_as_list_of_lines("../tests/test_part_1_answer.txt")

    test_answer = int(answer_document[0])

    assert solution.part_1.calculate_answer("../input.txt") == test_answer

def test_exception_is_raised_if_file_not_found():
    with pytest.raises(FileNotFoundError):
        solution.part_1.open_file_as_list_of_lines("wrong_filename_that_doesn't_exist.txt")

def test_calibration_values_list_has_correct_number_of_calibration_values(test_list_of_calibration_values_setup):
    assert len(test_list_of_calibration_values_setup) == len(solution.part_1.determine_calibration_values("../input.txt", test_list_of_calibration_values_setup))

def test_calibration_values_list_contains_correct_calibration_values(test_list_of_calibration_values_setup):
    assert test_list_of_calibration_values_setup == solution.part_1.determine_calibration_values("../input.txt", test_list_of_calibration_values_setup)