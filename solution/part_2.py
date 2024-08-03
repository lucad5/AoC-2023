# Solution for part 2 of the Day 1 challenge of Advent of Code 2023.

import os
import part_1

# Change to the directory containing this .py file
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def determine_position_of_each_number_in_a_string(string_from_list, spelled_out_numbers_and_their_numerical_equivalents):
    """ Returns a dictionary (numbers_and_their_positions) that contains:
    keys: each number that occurs in each string of the list passed to the function
    values: the index of each instance a particular number (key) occurs within the string.
    """

    # Determine the index for each digit in the string
    numbers_and_their_positions = {}
    for index, character in enumerate(string_from_list):
        if character.isdigit():
            if numbers_and_their_positions.get(character) == None:
                numbers_and_their_positions[character] = []
            numbers_and_their_positions[character].append(index)
    numbers_in_current_line = []

    # Determine the position (index of first letter) of each spelled-out number in the string
    for spelled_out_number in spelled_out_numbers_and_their_numerical_equivalents:

        index_of_spelled_out_number = 0
        spelled_out_number_as_digit = None

        if spelled_out_number in string_from_list:
            # set spelled_out_number_as_digit to be the spelled-out number as a digit
            # example: if spelled_out_number is "three", then spelled_out_number_as_digit will be 3
            spelled_out_number_as_digit = spelled_out_numbers_and_their_numerical_equivalents[spelled_out_number]

            if numbers_and_their_positions.get(spelled_out_number_as_digit) == None:
                numbers_and_their_positions[spelled_out_number_as_digit] = []
            
            # find every instance of the spelled out number in the string, going from left to right
            while index_of_spelled_out_number < len(string_from_list):
                if string_from_list[index_of_spelled_out_number:].find(spelled_out_number) == -1:
                    break

                elif string_from_list[index_of_spelled_out_number:].find(spelled_out_number) != -1:
                    if index_of_spelled_out_number == 0:
                        numbers_and_their_positions[spelled_out_number_as_digit].append(string_from_list[index_of_spelled_out_number:].find(spelled_out_number))

                        index_of_spelled_out_number += string_from_list[index_of_spelled_out_number:].find(spelled_out_number) + len(spelled_out_number)

                    elif index_of_spelled_out_number > 0:
                        numbers_and_their_positions[spelled_out_number_as_digit].append(string_from_list[index_of_spelled_out_number:].find(spelled_out_number)+index_of_spelled_out_number)
                        index_of_spelled_out_number += len(spelled_out_number) + string_from_list[index_of_spelled_out_number:].find(spelled_out_number)

    return numbers_and_their_positions

def find_first_and_last_number_in_string(string, spelled_out_numbers_and_their_numerical_equivalents):
    """ Returns a dictionary (first_and_last_numbers_in_current_line)
    that contains the first and last number in the string.
    The dictionary will contain:
    Keys: "first" and "last"
    Values: for "first" key: the first number; for "last" key: the last number
    """

    position_of_first_number_in_string = None
    first_number_in_string = None
    position_of_last_number_in_string = None
    last_number_in_string = None

    positions_of_numbers_in_current_line = {}
    positions_of_numbers_in_current_line = determine_position_of_each_number_in_a_string(string, spelled_out_numbers_and_their_numerical_equivalents)

    first_and_last_numbers_in_current_line = {}
    
    # Loop to find the first number in the line
    for number in positions_of_numbers_in_current_line:

        if first_number_in_string == None:
            first_number_in_string = number
            position_of_first_number_in_string = min(positions_of_numbers_in_current_line[number])

        elif position_of_first_number_in_string == 0:
            continue

        elif min(positions_of_numbers_in_current_line[number]) < position_of_first_number_in_string:
            first_number_in_string = number
            position_of_first_number_in_string = min(positions_of_numbers_in_current_line[number])

    first_and_last_numbers_in_current_line["first"] = first_number_in_string
    
    # Loop to find the last number in the line
    for number in positions_of_numbers_in_current_line:
        if last_number_in_string == None:
            last_number_in_string = number
            position_of_last_number_in_string = max(positions_of_numbers_in_current_line[number])

        elif max(positions_of_numbers_in_current_line[number]) > position_of_last_number_in_string:
            last_number_in_string = number
            position_of_last_number_in_string = max(positions_of_numbers_in_current_line[number])        

    first_and_last_numbers_in_current_line["last"] = last_number_in_string

    return first_and_last_numbers_in_current_line

def determine_calibration_values_part_two(lines_list, spelled_out_numbers_and_their_numerical_equivalents):

    """Given a list of strings (lines_list), returns a list (calibration_values_list)
    where each element is a calibration for a line in lines_list."""

    calibration_values_list = []

    # Loop over each line in the lines_list
    for line in lines_list:

        first_and_last_number_in_current_line = {}
        first_and_last_number_in_current_line = find_first_and_last_number_in_string(line, spelled_out_numbers_and_their_numerical_equivalents)

        # Combine the first and last digit (example: "2" and "3" are combined to form "23")
        calibration_value_in_current_line = first_and_last_number_in_current_line["first"] + first_and_last_number_in_current_line["last"]

        calibration_value_in_current_line = int(calibration_value_in_current_line)

        calibration_values_list.append(calibration_value_in_current_line)

    return calibration_values_list

def open_file_as_list_of_lines(name_of_file):
    try:
        calibration_value_document = open(name_of_file, "r")
        lines = calibration_value_document.readlines()
        calibration_value_document.close()
        return lines
    except FileNotFoundError:
        print("Error: input.txt file not found.")
        raise

def calculate_answer(file_name):
    spelled_out_numbers_and_their_numerical_equivalents = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    lines_from_input = part_1.open_file_as_list_of_lines(file_name)

    calibration_values_in_input = []
    calibration_values_in_input = determine_calibration_values_part_two(lines_from_input, spelled_out_numbers_and_their_numerical_equivalents)

    sum_of_all_calibration_values = int()
    for calibration_value in calibration_values_in_input:
        sum_of_all_calibration_values += calibration_value

    answer = sum_of_all_calibration_values

    return answer

def main():

    print("This program calculates the answer for part 2 of the Day 1 challenge from Advent of Code 2023.\n")

    file_name = "../input.txt"
    answer = calculate_answer(file_name)

    print("The answer (the sum of all calibration values in the document) is: " + str(answer))

if __name__ == "__main__":
    main()