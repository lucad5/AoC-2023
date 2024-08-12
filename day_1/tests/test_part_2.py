import pytest
import os

import sys

# Add the parent directory and solutions folder to the path.
# If this is not done, then part_2.py will not be able to import part_1.py
# when this file (test_part_2.py) is run.
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

def test_empty_string_is_handled_correctly():
    test_file_name = "test_empty_string_is_handled_correctly.txt"

    answer = 0

    with open(test_file_name, "w") as test_file:
        test_file.write("")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == answer

    os.remove(test_file_name)

## Tests involving strings containing a single digit, or one of each digit

def test_string_consisting_of_a_single_digit():

    test_file_name = "test_string_consisting_of_a_single_digit.txt"

    for number in range(1, 10):

        correct_calibration_value = int(str(number)+str(number))

        with open(test_file_name, "w") as test_file:
            test_file.write(str(number))

        with open(test_file_name, "r") as test_file:
            assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == correct_calibration_value

        with open(test_file_name, "w") as test_file:
            test_file.write("")

    os.remove(test_file_name)

def test_string_containing_one_of_each_digit():

    test_file_name = "test_string_containing_one_of_each_digit.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("123456789")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 19

    os.remove(test_file_name)

## Tests involving strings containing a single spelled-out number, or one of each spelled-out number

def test_strings_consisting_of_a_spelled_out_number_from_one_to_nine():

    test_file_name = "test_strings_consisting_of_a_spelled_out_number_from_one_to_nine.txt"

    spelled_out_numbers_and_their_numerical_equivalents = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    # Checks that the solution calculates the answer to be 11 for a string that only contains the text "one",
    # 22 for a string containing only the text "two", etc.
    for spelled_out_number, digit in spelled_out_numbers_and_their_numerical_equivalents.items():
        correct_calibration_value = int(str(digit)+str(digit))

        with open(test_file_name, "w") as test_file:
            test_file.write(spelled_out_number)

        with open(test_file_name, "r") as test_file:
            assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == correct_calibration_value

        os.remove(test_file_name)

def test_string_with_one_of_each_spelled_out_number():

    test_file_name = "test_string_with_one_of_each_spelled_out_number.txt"

    answer = 19

    with open(test_file_name, "w") as test_file:
        test_file.write("onetwothreefourfivesixseveneightnine")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == answer

    os.remove(test_file_name)

## Tests involving both digits and spelled-out numbers

def test_string_consisting_of_one_digit_followed_by_multiple_spelled_out_numbers():
    test_file_name = "test_string_consisting_of_one_digit_followed_by_multiple_spelled_out_numbers.txt"

    answer = 19

    with open(test_file_name, "w") as test_file:
        test_file.write("1onetwothreefourfivesixseveneightnine")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == answer

    os.remove(test_file_name)

def test_string_consisting_of_multiple_spelled_out_numbers_followed_by_one_digit():
    test_file_name = "test_string_consisting_of_multiple_spelled_out_numbers_followed_by_one_digit.txt"

    answer = 11

    with open(test_file_name, "w") as test_file:
        test_file.write("onetwothreefourfivesixseveneightnine1")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == answer

    os.remove(test_file_name)

def test_string_consisting_of_one_digit_followed_by_multiple_spelled_out_numbers_followed_by_one_digit():
    test_file_name = "test_string_consisting_of_one_digit_followed_by_multiple_spelled_out_numbers_followed_by_one_digit.txt"

    answer = 11

    with open(test_file_name, "w") as test_file:
        test_file.write("1onetwothreefourfivesixseveneightnine1")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == answer

    os.remove(test_file_name)

def test_string_consisting_of_each_digit_occurring_twice():
    test_file_name = "test_string_consisting_of_each_digit_occurring_twice.txt"

    answer = 10

    with open(test_file_name, "w") as test_file:
        test_file.write("11223344556677889900")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == answer

    os.remove(test_file_name)

def test_string_consisting_of_each_spelled_out_number_occurring_twice():
    test_file_name = "test_string_consisting_of_each_spelled_out_number_occurring_twice.txt"

    answer = 19

    with open(test_file_name, "w") as test_file:
        test_file.write("oneonetwotwothreethreefourfourfivefivesixsixsevenseveneighteightninenine")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == answer

    os.remove(test_file_name)

def test_string_consisting_of_digit_occurring_twice_followed_by_each_spelled_out_number_occurring_twice():
    test_file_name = "test_string_consisting_of_digit_occurring_twice_followed_by_each_spelled_out_number_occurring_twice.txt"

    answer = 19

    with open(test_file_name, "w") as test_file:
        test_file.write("11223344556677889900oneonetwotwothreethreefourfourfivefivesixsixsevenseveneighteightninenine")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == answer

    os.remove(test_file_name)

# TODO: fill in these tests

def test_string_with_alternating_digits_and_spelled_out_numbers():
    test_file_name = "test_string_with_alternating_digits_and_spelled_out_numbers.txt"

    answer = 19

    with open(test_file_name, "w") as test_file:
        test_file.write("one1two2three3four4five5six6seven7eight8nine9")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == answer

    os.remove(test_file_name)

def test_string_with_overlapping_spelled_out_numbers():
    test_file_name = "test_string_with_overlapping_spelled_out_numbers.txt"

    answer = 23

    with open(test_file_name, "w") as test_file:
        test_file.write("twonefiveightoneightthreeightnineightsevenineeightwoeighthree")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == answer

    os.remove(test_file_name)

def test_string_with_special_characters():
    test_file_name = "test_string_with_special_characters.txt"

    answer = 23

    with open(test_file_name, "w") as test_file:
        test_file.write(r"!@#$%^&*()_+~|}{:\"<>/.,l;'[]=-`?twonefiveightoneightthreeightnineightsevenineeightwoeighthree")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == answer

    os.remove(test_file_name)

def test_list_with_the_digits_for_one_and_two_on_two_lines():
    test_file_name = "test_list_with_the_digits_for_one_and_two_on_two_lines.txt"

    answer = 24

    with open(test_file_name, "w") as test_file:
        test_file.write("12\n12")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == answer

    os.remove(test_file_name)
