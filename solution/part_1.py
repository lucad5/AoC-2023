# Solution for part 1 of the Day 1 challenge of Advent of Code 2023.

def determine_calibration_values(lines_list, calibration_values_list):

    """Given a list of strings (lines_list), returns a list (calibration_values_list)
    where each element is a calibration for a line in lines_list."""

    for line in lines_list:

        numbers_in_current_line = []
        calibration_value_in_current_line = None

        for character_index, character in enumerate(line):

            if character.isnumeric() == True:
                numbers_in_current_line.append(character)

            # if the end of the line is reached and there is at least one number in the line
            if character_index == (len(line)-1) and len(numbers_in_current_line) > 0:
                # If there are multiple digits in the current line, combine the first and last number to get the calibration value
                # Example: "1" and "5" are combined to get "15"
                if len(numbers_in_current_line) > 1:
                    calibration_value_in_current_line = int(numbers_in_current_line[0] + numbers_in_current_line[len(numbers_in_current_line)-1])

                # If there is only one number in the current line, set the calibration value to the number where that digit occurs twice
                # Example: if the only number in the current line is "7", set the calibration value to "77"
                elif len(numbers_in_current_line) == 1:
                    calibration_value_in_current_line = int(numbers_in_current_line[0]+numbers_in_current_line[0])

                calibration_values_list.append(calibration_value_in_current_line)

                continue

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

def calculate_sum_of_all_calibration_values(calibration_values):
    sum_of_all_calibration_values = int()
    for calibration_value in calibration_values:
        sum_of_all_calibration_values += calibration_value
    return sum_of_all_calibration_values

def calculate_answer(file_name):

    list_of_lines_from_input = open_file_as_list_of_lines(file_name)

    calibration_values = []
    calibration_values = determine_calibration_values(list_of_lines_from_input, calibration_values)

    answer = calculate_sum_of_all_calibration_values(calibration_values)

    return answer

def main():

    print("This program calculates the sum of the calibration values for \
    part 1 of the Day 1 challenge from Advent of Code 2023.\n")

    file_name = "../input.txt"

    answer = calculate_answer(file_name)

    print("The answer (the sum of all calibration values in the document) is: " + str(answer))

if __name__ == "__main__":
    main()
