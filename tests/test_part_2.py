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


## Tests involving strings containing a single digit, or one of each digit

def test_string_consisting_of_the_digit_for_the_number_one():

    test_file_name = "test_string_consisting_of_the_digit_for_the_number_one.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("1")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 11

    os.remove(test_file_name)

def test_string_consisting_of_the_digit_for_the_number_two():

    test_file_name = "test_string_consisting_of_the_digit_for_the_number_two.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("2")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 22

    os.remove(test_file_name)

def test_string_consisting_of_the_digit_for_the_number_three():

    test_file_name = "test_string_consisting_of_the_digit_for_the_number_three.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("3")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 33

    os.remove(test_file_name)

def test_string_consisting_of_the_digit_for_the_number_four():

    test_file_name = "test_string_consisting_of_the_digit_for_the_number_four.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("4")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 44

    os.remove(test_file_name)

def test_string_consisting_of_the_digit_for_the_number_five():

    test_file_name = "test_string_consisting_of_the_digit_for_the_number_five.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("5")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 55

    os.remove(test_file_name)

def test_string_consisting_of_the_digit_for_the_number_six():

    test_file_name = "test_string_consisting_of_the_digit_for_the_number_six.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("6")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 66

    os.remove(test_file_name)

def test_string_consisting_of_the_digit_for_the_number_seven():

    test_file_name = "test_string_consisting_of_the_digit_for_the_number_seven.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("7")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 77

    os.remove(test_file_name)

def test_string_consisting_of_the_digit_for_the_number_eight():

    test_file_name = "test_string_consisting_of_the_digit_for_the_number_eight.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("8")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 88

    os.remove(test_file_name)

def test_string_consisting_of_the_digit_for_the_number_nine():

    test_file_name = "test_string_consisting_of_the_digit_for_the_number_nine.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("9")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 99

    os.remove(test_file_name)

def test_string_containing_one_of_each():

    test_file_name = "test_string_containing_one_of_each_digit.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("123456789")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 19

    os.remove(test_file_name)

## Tests involving strings containing a single spelled-out number, or one of each spelled-out number

def test_string_consisting_of_the_spelled_out_number_one():

    test_file_name = "test_string_consisting_of_the_spelled_out_number_one.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("one")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 11

    os.remove(test_file_name)

def test_string_consisting_of_the_spelled_out_number_two():

    test_file_name = "test_string_consisting_of_the_spelled_out_number_two.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("two")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 22

    os.remove(test_file_name)

def test_string_consisting_of_the_spelled_out_number_three():

    test_file_name = "test_string_consisting_of_the_spelled_out_number_three.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("three")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 33

    os.remove(test_file_name)

def test_string_consisting_of_the_spelled_out_number_four():

    test_file_name = "test_string_consisting_of_the_spelled_out_number_four.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("four")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 44

    os.remove(test_file_name)

def test_string_consisting_of_the_spelled_out_number_five():

    test_file_name = "test_string_consisting_of_the_spelled_out_number_five.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("five")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 55

    os.remove(test_file_name)

def test_string_consisting_of_the_spelled_out_number_six():

    test_file_name = "test_string_consisting_of_the_spelled_out_number_six.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("six")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 66

    os.remove(test_file_name)

def test_string_consisting_of_the_spelled_out_number_seven():

    test_file_name = "test_string_consisting_of_the_spelled_out_number_seven.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("seven")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 77

    os.remove(test_file_name)

def test_string_consisting_of_the_spelled_out_number_eight():

    test_file_name = "test_string_consisting_of_the_spelled_out_number_eight.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("eight")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 88

    os.remove(test_file_name)

def test_string_consisting_of_the_spelled_out_number_nine():

    test_file_name = "test_string_consisting_of_the_spelled_out_number_nine.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("nine")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 99

    os.remove(test_file_name)

def test_string_consisting_of_the_spelled_out_number_nine():

    test_file_name = "test_string_consisting_of_the_spelled_out_number_nine.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("nine")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 99

    os.remove(test_file_name)

def test_string_with_one_of_each_spelled_out_number():

    test_file_name = "test_string_with_one_of_each_spelled_out_number.txt"

    with open(test_file_name, "w") as test_file:
        test_file.write("onetwothreefourfivesixseveneightnine")

    with open(test_file_name, "r") as test_file:
        assert solution.part_2.calculate_answer(os.path.basename(test_file.name)) == 19

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
