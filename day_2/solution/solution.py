# workflow:

# open file

# create_dictionary_based_on_input()
# put content of file into a dictionary with the following structure:
# key: game ID (an integer)
# value: list (each list item contains a dictionary showing what cubes were shown in that round of the game; example:)
    # list item: {"red": 1, "green": 5, "blue": 6}

# determine_ids_of_possible_games()
# Determine which game IDs were possible given a bag with 12 red cubes, 13 green cubes, and 14 blue cubes
# That is, game IDs where more than 12 red cubes at a time, 13 green cubes at a time, or 14 blue cubes at a time were shown are not possible
# Put the game IDs of the possible games into a list
# return ids_of_possible_games

# calculate_answer()
# answer = sum_of_ids_of_possible_games
# return answer

# print answer

def open_file_as_list_of_lines(file_name):
    with open(file_name, "r") as f:
        list_of_lines = f.readlines()
        return list_of_lines

def create_dictionary_based_on_input(list_of_lines_from_input):
# put content of file into a dictionary with the following structure:
# key: game ID (an integer)
# value: list (each list item contains a dictionary showing what cubes were shown in that round of the game; example:)
    # list item: {"red": 1, "green": 5, "blue": 6}

    dictionary_of_games = {}


    for line in list_of_lines_from_input:
        rounds_in_game = []

        list_of_game_and_rounds = line.split(": ")
#        print("Game and rounds:", list_of_game_and_rounds)

        list_of_game_string_and_id = list_of_game_and_rounds[0].split("Game ")
        game_id = int(list_of_game_string_and_id[1])

        dictionary_of_games[game_id] = []

        list_of_rounds = list_of_game_and_rounds[1].split("; ")
#        print("Rounds: ", list_of_rounds)

        round_index = 0
        for round in list_of_rounds:

            dictionary_of_games[game_id].append({})

            list_of_numbers_and_colors_in_round = round.split(", ")

            for index, string in enumerate(list_of_numbers_and_colors_in_round):
                list_of_numbers_and_colors_in_round[index] = list_of_numbers_and_colors_in_round[index].rstrip("\n")
#            print(list_of_numbers_and_colors_in_round)

            for number_and_color in list_of_numbers_and_colors_in_round:
                list_of_number_and_color = number_and_color.split(" ")

                number = list_of_number_and_color[0]
                color = list_of_number_and_color[1]
#                print("color:", color, "number:", number, list_of_number_and_color)

                if color == "green":
                    dictionary_of_games[game_id][round_index][color] = int(number)
                elif color == "red":
                    dictionary_of_games[game_id][round_index][color] = int(number)
                elif color == "blue":
                    dictionary_of_games[game_id][round_index][color] = int(number)

            round_index += 1
#    print("Dictionary of games", dictionary_of_games[99])
    return dictionary_of_games


def determine_ids_of_possible_games(dictionary_of_games):
# Determine which game IDs were possible given a bag with 12 red cubes, 13 green cubes, and 14 blue cubes
# That is, game IDs where more than 12 red cubes at a time, 13 green cubes at a time, or 14 blue cubes at a time were shown are not possible
# Put the game IDs of the possible games into a list

#    print(dictionary_of_games["0"])
    list_of_ids_of_possible_games = []

    maximum_number_of_red_cubes = 12
    maximum_number_of_green_cubes = 13
    maximum_number_of_blue_cubes = 14

    #TODO: in progress
    for game_id in dictionary_of_games:
        game_is_possible = False
        for round in dictionary_of_games[game_id]:
#            print("Round:", round)
            if "blue" in round:
                if round["blue"] > maximum_number_of_blue_cubes:
                    number_of_blue_cubes_is_possible = False
                    break
                else:
                    number_of_blue_cubes_is_possible = True
            if "red" in round:
                if round["red"] > maximum_number_of_red_cubes:
                    number_of_red_cubes_is_possible = False
                    break
                else:
                    number_of_red_cubes_is_possible = True

            if "green" in round:
                if round["green"] > maximum_number_of_green_cubes:
                    number_of_green_cubes_is_possible = False
                    break
                else:
                    number_of_green_cubes_is_possible = True

        if number_of_blue_cubes_is_possible == True and number_of_red_cubes_is_possible == True and number_of_green_cubes_is_possible == True:
            list_of_ids_of_possible_games.append(game_id)

#    print("possible games:", list_of_ids_of_possible_games)
    return list_of_ids_of_possible_games

def calculate_sum_of_ids_of_possible_games(possible_games):
    answer = int()
    for id in possible_games:
        answer += id
    return answer

def determine_minimum_sets_of_cubes_in_input(dictionary_of_games):

    minimum_sets_of_cubes_in_input = {}

    for game_id in dictionary_of_games:

        minimum_necessary_number_of_cubes_of_each_color_for_current_game = {}

        for round in dictionary_of_games[game_id]:
            for color in round:
                if color not in minimum_necessary_number_of_cubes_of_each_color_for_current_game:
                    minimum_necessary_number_of_cubes_of_each_color_for_current_game[color] = round[color]
                elif round[color] > minimum_necessary_number_of_cubes_of_each_color_for_current_game[color]:
                    minimum_necessary_number_of_cubes_of_each_color_for_current_game[color] = round[color]
                elif round[color] < minimum_necessary_number_of_cubes_of_each_color_for_current_game[color]:
                    continue

        minimum_sets_of_cubes_in_input[game_id] = minimum_necessary_number_of_cubes_of_each_color_for_current_game

    return minimum_sets_of_cubes_in_input

def determine_sum_of_powers_of_minimum_sets_of_cubes_in_input(dictionary_of_minimum_sets_of_cubes_in_input):

    powers_of_minimum_sets_of_cubes_in_input = []

    for game_id in dictionary_of_minimum_sets_of_cubes_in_input:
        minimum_number_of_cubes_of_each_color_in_current_game = []

        for color in dictionary_of_minimum_sets_of_cubes_in_input[game_id]:
            minimum_number_of_cubes_of_each_color_in_current_game.append(dictionary_of_minimum_sets_of_cubes_in_input[game_id][color])

        power_of_minimum_number_of_cubes_of_each_color_in_current_game = int()

        for number_of_cubes in minimum_number_of_cubes_of_each_color_in_current_game:

            if power_of_minimum_number_of_cubes_of_each_color_in_current_game == 0:
                power_of_minimum_number_of_cubes_of_each_color_in_current_game += number_of_cubes

            else:
                power_of_minimum_number_of_cubes_of_each_color_in_current_game *= number_of_cubes

        powers_of_minimum_sets_of_cubes_in_input.append(power_of_minimum_number_of_cubes_of_each_color_in_current_game)

    sum_of_powers_of_minimum_sets_of_cubes_in_input = int()
    
    for number in powers_of_minimum_sets_of_cubes_in_input:
        sum_of_powers_of_minimum_sets_of_cubes_in_input += number
    
    return sum_of_powers_of_minimum_sets_of_cubes_in_input


def main():
    file_name = "../input.txt"
    list_of_lines_from_input = open_file_as_list_of_lines(file_name)

    dictionary_of_games = {}
    dictionary_of_games = create_dictionary_based_on_input(list_of_lines_from_input)

    possible_games = []
    possible_games = determine_ids_of_possible_games(dictionary_of_games)

    part_one_answer = calculate_sum_of_ids_of_possible_games(possible_games)

    print("The answer (the sum of the IDs of all possible games) for part 1 is:", part_one_answer)

    # Part 2

    dictionary_of_minimum_sets_of_cubes_in_input = []
    dictionary_of_minimum_sets_of_cubes_in_input = determine_minimum_sets_of_cubes_in_input(dictionary_of_games)

    part_two_answer = determine_sum_of_powers_of_minimum_sets_of_cubes_in_input(dictionary_of_minimum_sets_of_cubes_in_input)

    print("The answer (the sum of the powers of the minimum sets of cubes for each game) is: ", part_two_answer)

if __name__ == "__main__":
    main()