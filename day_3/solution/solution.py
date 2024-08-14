def create_dictionary_of_numbers_and_symbols_in_input(list_of_lines_in_input):
    """
    Returns a dictionary with the following structure (values are given as examples).
    {
        # Each key is a line number from the input
        "0":
            # List containing each number or symbol in the line.
            # The values are the indexes of the first and last characters of the number or symbol within the line
            [
            {"324": {"start": 1, "end": 3 }}
            {"%": {"start": 7, "end": 7}}
            ]

        "1":
            [
            {"5": {"start": 8, "end": 8 }}
            {"&": {"start": 2, "end": 2}}
            ]

        etc.

    }
    """

    dictionary_of_numbers_and_symbols_in_input = {}

    for line_number, line in enumerate(list_of_lines_in_input):

        dictionary_of_numbers_and_symbols_in_input[line_number] = []

        index = 0
        while index < len(line):

            # Skip periods and newlines
            if line[index] in [".", "\n"]:
                index += 1

            # If the current character is a symbol (excluding ".")
            elif line[index] != "." and line[index].isnumeric() != True:
                symbol = line[index]
                value_and_position_of_symbol = {}
                value_and_position_of_symbol[symbol] = {}
                value_and_position_of_symbol[symbol]["start"] = index
                value_and_position_of_symbol[symbol]["end"] = index

                dictionary_of_numbers_and_symbols_in_input[line_number].append(value_and_position_of_symbol)

                index += 1 

            # If the current character is a number
            elif line[index].isnumeric() == True:
                value_and_position_of_number = {}

                # If the number only has one digit (!= followed by more digits)
                if line[index+1].isnumeric() == False:
                    value_and_position_of_number[line[index]] = {}
                    value_and_position_of_number[line[index]]["start"] = index
                    value_and_position_of_number[line[index]]["end"] = index

                    dictionary_of_numbers_and_symbols_in_input[line_number].append(value_and_position_of_number)
                    
                    index += 1
                
                # If the number has multiple digits (is followed by at least one more digit)
                elif line[index+1].isnumeric() == True:
                
                    # Iterate over the remaining digits of the number
                    # to determine the position of the last digit of the number
                    index_of_start_of_number = index
                    for i, character in enumerate(line[index_of_start_of_number:]):

                        # If the last digit of the number is reached, add the position of the last digit to the dictionary for the number
                        if line[index_of_start_of_number+i].isnumeric() == True and line[index_of_start_of_number+i+1].isnumeric() == False:
                            index_of_end_of_number = index_of_start_of_number+i

                            number = int(line[index_of_start_of_number:(index_of_end_of_number+1)])

                            value_and_position_of_number[number] = {}
                            value_and_position_of_number[number]["start"] = index_of_start_of_number
                            value_and_position_of_number[number]["end"] = index_of_end_of_number

                            dictionary_of_numbers_and_symbols_in_input[line_number].append(value_and_position_of_number)

                            # Change the index so it is the position of the character that occurs after the final digit of the number
                            index = index_of_start_of_number+i+1
                            break
                        else:
                            continue
                    
    return dictionary_of_numbers_and_symbols_in_input

def create_list_of_valid_part_numbers(dictionary_of_numbers_and_symbols_in_input):

    list_of_valid_part_numbers = []

    for line_number in dictionary_of_numbers_and_symbols_in_input:

        list_of_lines_to_parse = [line_number]

        if len(dictionary_of_numbers_and_symbols_in_input) > 1:

            # If it is the first line, the only adjacent line is the following line
            if line_number == 0:
                line_number_of_following_line = line_number+1
                list_of_lines_to_parse.append(line_number_of_following_line)

            # If it is the last line, the only adjacent line is the previous line
            elif line_number == len(dictionary_of_numbers_and_symbols_in_input)-1:
                line_number_of_previous_line = line_number-1
                list_of_lines_to_parse.append(line_number_of_previous_line)
            
            else:
                line_number_of_previous_line = line_number-1
                line_number_of_following_line = line_number+1
                list_of_lines_to_parse.append(line_number_of_previous_line)
                list_of_lines_to_parse.append(line_number_of_following_line)

        for dictionary_for_item in dictionary_of_numbers_and_symbols_in_input[line_number]:

            for key in dictionary_for_item:

                key_is_a_valid_part_number = False

                # If the item is a number
                if str(key).isnumeric() == True:

                    for line_number_to_parse in list_of_lines_to_parse:
                        # Iterate over all items in the current line and any adjacent lines to see if any of the items are symbols
                        for dictionary_of_second_item in dictionary_of_numbers_and_symbols_in_input[line_number_to_parse]:
                            for key_of_second_item in dictionary_of_second_item:

                                if str(key_of_second_item).isnumeric() != True:
                                    # See if the second item is adjacent to the number

                                    range_of_number = range(dictionary_for_item[key]["start"], dictionary_for_item[key]["end"]+1)
                                    index_of_symbol = dictionary_of_second_item[key_of_second_item]["start"]

                                    for i in range_of_number:
                                        if i in [index_of_symbol-1, index_of_symbol, index_of_symbol+1]:
                                            key_is_a_valid_part_number = True
                                            break
                                        else:
                                            continue
                    
                # If the item is a non-numeric symbol, skip it
                elif str(key).isnumeric() == False:
                    continue

                if key_is_a_valid_part_number == True:
                    list_of_valid_part_numbers.append(key)

    return list_of_valid_part_numbers

def calculate_sum_of_valid_part_numbers(list_of_valid_part_numbers):

    sum_of_valid_part_numbers = int()

    for number in list_of_valid_part_numbers:
        sum_of_valid_part_numbers += int(number)

    return sum_of_valid_part_numbers

def main():

    file_name = "../input.txt"

    list_of_lines_in_input = []
    with open(file_name) as f:
        list_of_lines_in_input = f.readlines()

    dictionary_of_numbers_and_symbols_in_input = create_dictionary_of_numbers_and_symbols_in_input(list_of_lines_in_input)

    list_of_valid_part_numbers = create_list_of_valid_part_numbers(dictionary_of_numbers_and_symbols_in_input)

    answer = calculate_sum_of_valid_part_numbers(list_of_valid_part_numbers)

    print("The answer for part one is:", answer)

if __name__ == "__main__":
    main()