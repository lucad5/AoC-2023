import pytest
import os

import sys

# Add the parent directory and solutions folder to the path.
# If this is not done, then part_2.py will not be able to import part_1.py when this file (test_part_2.py) is run.
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)
solution_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))+"\\solution"
sys.path.append(solution_dir)

import solution.part_1
import solution.part_2

def test_if_answer_is_correct():

    answer_document = solution.part_1.open_file_as_list_of_lines("../tests/test_part_2_answer.txt")
    test_answer = int(answer_document[0])
    assert solution.part_2.calculate_answer("../input.txt") == test_answer

def test_exception_is_raised_if_file_not_found():
    with pytest.raises(FileNotFoundError):
        solution.part_1.open_file_as_list_of_lines("wrong_filename_that_doesn't_exist.txt")

## TODO: fill in these functions
# def test_string_with_one_digit():
# def test_string_with_one_spelled_out_number():
# def test_string_with_multiple_spelled_out_numbers():
# def test_string_with_one_digit_and_multiple_spelled_out_numbers():
# def test_string_with_multiple_digits_and_multiple_spelled_out_numbers():
# def test_string_with_alternating_digits_and_spelled_out_numbers():
# def test_string_with_repeating_digits_and_repeating_spelled_out_numbers():
# def test_string_with_digits_and_overlapping_spelled_out_numbers():
# def test_string_with_special_characters():
# def test_string_with_digit_and_spelled_out_number():
# def test_list_with_multiple_lines:
# def test_empty_string_is_handled_correctly():