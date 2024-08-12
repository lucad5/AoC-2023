def open_file_as_list_of_lines(file_name):
    with open(file_name, "r") as f:
        list_of_lines = f.readlines()
        return list_of_lines

def create_dictionary_based_on_input(list_of_lines_from_input):

    dictionary_of_games = {}


    for line in list_of_lines_from_input:
        rounds_in_game = []

        list_of_game_and_rounds = line.split(": ")

        list_of_game_string_and_id = list_of_game_and_rounds[0].split("Game ")
        game_id = int(list_of_game_string_and_id[1])

        dictionary_of_games[game_id] = []

        list_of_rounds = list_of_game_and_rounds[1].split("; ")

        round_index = 0
        for round in list_of_rounds:

            dictionary_of_games[game_id].append({})

            list_of_numbers_and_colors_in_round = round.split(", ")

            for index, string in enumerate(list_of_numbers_and_colors_in_round):
                list_of_numbers_and_colors_in_round[index] = list_of_numbers_and_colors_in_round[index].rstrip("\n")

            for number_and_color in list_of_numbers_and_colors_in_round:
                list_of_number_and_color = number_and_color.split(" ")

                number = list_of_number_and_color[0]
                color = list_of_number_and_color[1]

                if color == "green":
                    dictionary_of_games[game_id][round_index][color] = int(number)
                elif color == "red":
                    dictionary_of_games[game_id][round_index][color] = int(number)
                elif color == "blue":
                    dictionary_of_games[game_id][round_index][color] = int(number)

            round_index += 1

    return dictionary_of_games


def determine_ids_of_possible_games(dictionary_of_games):
    """ Determine which game IDs were possible given a bag with 12 red cubes, 13 green cubes, and 14 blue cubes """

    list_of_ids_of_possible_games = []

    maximum_number_of_red_cubes = 12
    maximum_number_of_green_cubes = 13
    maximum_number_of_blue_cubes = 14

    for game_id in dictionary_of_games:

        game_is_possible = False

        # Determine if any of the rounds cannot be played given the maximum numbers of each type of cube listed above
        for round in dictionary_of_games[game_id]:

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

        # If the number of each type of cube for this round is possible, add the game_id to the list of possible games
        if number_of_blue_cubes_is_possible == True and number_of_red_cubes_is_possible == True and number_of_green_cubes_is_possible == True:
            list_of_ids_of_possible_games.append(game_id)

    return list_of_ids_of_possible_games

def calculate_sum_of_ids_of_possible_games(possible_games):
    answer = int()
    for id in possible_games:
        answer += id
    return answer

def determine_minimum_sets_of_cubes_in_input(dictionary_of_games):
    """For each game in the input, determine the minimum number of each type (red, green, blue) of cube
    necessary for the game to be playable.
    """
    minimum_sets_of_cubes_in_input = {}

    for game_id in dictionary_of_games:

        minimum_necessary_number_of_cubes_of_each_color_for_current_game = {}

        for round in dictionary_of_games[game_id]:

            for color in round:
                
                # If the current color has not previously been found in this round,
                # add it to the minimum_necessary_number_of_cubes_of_each_color_for_current_game dictionary
                if color not in minimum_necessary_number_of_cubes_of_each_color_for_current_game:
                    minimum_necessary_number_of_cubes_of_each_color_for_current_game[color] = round[color]

                # To accommodate a larger number of cubes found in the current round,
                # update the minimum necessary number of cubes
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

        # Determine the power of the set of the minimum number of cubes in the current game
        for number_of_cubes in minimum_number_of_cubes_of_each_color_in_current_game:

            # If no numbers have been added to power_of_minimum_number_of_cubes_of_each_color_in_current_game yet,
            # add the current number of cubes to that variable
            if power_of_minimum_number_of_cubes_of_each_color_in_current_game == 0:
                power_of_minimum_number_of_cubes_of_each_color_in_current_game += number_of_cubes

            else:
                power_of_minimum_number_of_cubes_of_each_color_in_current_game *= number_of_cubes

        # Add the power of the set of the minimum number of cubes in the current game
        # to the list of all powers of sets in the input
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
