import pydealer
from interface_function import display_game_board, display_end_of_game_window
from player_class import Player
import pandas as pd


ELIMINATION_SCORE_THRESHOLD = 30
MAXIMUM_NUMBER_OF_PLAYERS = 6


def calculate_players_score(data_score, players_list, round_number):
    """
    Calculate and display the scores of players for each round.

    Parameters:
    - data (list): A list containing data for each player, round, and score.
    - players_list (list): A list of Player objects, each representing a player in the game.
    - round_number (int): The current round number for which the scores are calculated.

    Returns:
    - str: A formatted string representing the scores of players for each round.
    """

    # Iterate through each player in the provided list
    for player in players_list:
        # Create a row for each player containing round_number - 1, player name, and player score for the previous round
        player_row = [player.name, int(round_number - 1), int(player.score_round)]
        data_score.append(player_row)

    # Create a DataFrame with the data
    df = pd.DataFrame(data_score, columns=["Player", "Round", "Score"])

    # Pivot the DataFrame to arrange data by rounds and players
    df_pivoted = df.pivot(index='Round', columns='Player', values='Score')

    # Fill missing values with an empty string
    df_pivoted.fillna('', inplace=True)

    # Calculate the total score for each player and append a row to the DataFrame
    df_pivoted.loc[''] = df_pivoted.sum()

    # Reset the index to make rounds a regular column
    df_pivoted.reset_index(inplace=True)

    # Display the DataFrame as a formatted string
    message_for_score_button = df_pivoted.to_string(index=False)
    return message_for_score_button


def check_duplicates_players(player_name, players_list):
    """
        Check if a player with the given name already exists in the list.

        Parameters:
        - player_name (str): The name of the player to check.
        - players_list (list): List of Player objects.

        Returns:
        - bool: True if a player with the given name already exists, False otherwise.
        """
    return any(player.name == player_name for player in players_list)


def init_players():
    """
        Initialize the list of players for the game.

        Returns:
        - list: List of Player objects.
        """
    while True:
        try:
            number_of_players = int(input('Enter number of players:\n'))
            if number_of_players == 1 or number_of_players == 0 or number_of_players < 0:
                print("Wrong number of players (0, 1 or negative numbers are not allowed.")
            elif number_of_players <= MAXIMUM_NUMBER_OF_PLAYERS:
                players_list = []
                for i in range(1, number_of_players + 1):
                    while True:
                        player_name = input(f"Enter name of Player{i}:\n")
                        if check_duplicates_players(player_name, players_list):
                            print(f"{player_name} already exists and 2 players cannot have the same name")
                        else:
                            player = Player(player_name)
                            players_list.append(player)
                            break
                print([player.name for player in players_list])
                answer_validate_players = str(input(f"{len(players_list)} players will play, do you confirm ? (Y/N)\n"))
                if answer_validate_players == 'Y':
                    return players_list
                else:
                    pass

            else:
                print(f"Maximum number of players for this game is {MAXIMUM_NUMBER_OF_PLAYERS}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def init_jokers(deck):
    """
        Initialize and add Joker cards to the deck.

        Parameters:
        - The deck to which Jokers will have been added.
        """
    jokers = {}
    count = 1
    for i in range(1, 3):
        jokers[f'joker{i}'] = pydealer.Card('Joker', 'Hearts')
    for cards in jokers:
        cards = jokers[cards]
        cards.name = f'Joker{count}'
        cards.abbrev = f'J{count}'
        deck.add(cards)
        count += 1


def draw_cards_to_players(players_list, deck):
    """
        Draw cards from the deck and assign them to players still on game.

        Parameters:
        - players_list (list): List of Player objects.
        - deck (pydealer.Deck): The deck from which cards are drawn.
        """
    deck.shuffle()
    for player in players_list:
        if not player.is_eliminate:
            player.hand = deck.deal(5)
            player.hand.sort()


def draw_card_to_pile(deck):
    """
        Draw cards from the deck and form a pile.

        Parameters:
        - deck (pydealer.Deck): The deck from which cards are drawn.

        Returns:
        - pydealer.Stack: The pile of cards drawn.
        """
    pile = pydealer.Stack()
    pile = deck.deal(1)
    return pile


def reset_finish_round_for_each_player(players_list):
    """
        Reset finish_round for all players to False after each round

        Parameters:
        - players_list (list): List of Player objects.
    """
    for player in players_list:
        player.finish_round = False


def action(deck, pile, players_list, round_number, message_for_score_button):
    """
    Execute the game actions for each player in a round.

    Parameters:
    - deck (Deck): The deck of cards used in the game.
    - pile (Pile): The pile of cards discarded by players.
    - players_list (list): A list of Player objects, each representing a player in the game.
    - round_number (int): The current round number.
    - message_for_score_button (str): A formatted string representing the scores of players for each round.

    Returns:
    None
    """

    # Continue the game until one player has finished the round
    while all(not player.finish_round for player in players_list):
        for player in players_list:
            player_have_play = False

            # Check if the player is eliminated
            if not player.is_eliminate:
                # while the player has not played, we repeat this
                while not player_have_play:
                    pile_chose = []
                    deck_chose = []
                    display_type = 'normal'

                    # Display the game board and get player's move: cards played, pile or deck chose, player pass
                    cards_played, pile_chose, deck_chose, player_pass = display_game_board(players_list, pile, deck,
                                                                                           round_number, display_type,
                                                                                           pile_chose, deck_chose,
                                                                                           message_for_score_button)
                    # We check if the player has not decided to end the round
                    if not player.finish_round:
                        # We check if the player has not passed
                        if player_pass[0] == 'False':
                            # Execute the player's move
                            player.play(deck, pile, cards_played, pile_chose, deck_chose)
                            # Sort the updated hand of the player
                            player.hand.sort()
                            # Set the display type to temp, means that a light board game (no buttons on it)
                            # will be display to see which card the player has picked.
                            display_type = 'temp'

                            # Move cards from pile to deck if the deck is empty
                            if len(deck) == 0:
                                for cards in reversed(pile[:-1]):
                                    print(cards)
                                    deck.add(cards)
                                    pile.get(str(cards))

                            # Display the updated game board to see the card the player has picked from deck or pile
                            display_game_board(players_list, pile, deck, round_number, display_type, pile_chose,
                                               deck_chose, message_for_score_button)

                            # Rotate the player order
                            players_list = [players_list[(i + 1) % len(players_list)] for i in
                                            range(len(players_list))]

                            player_have_play = True

                        else:
                            # Skip player's turn if they pass
                            players_list = [players_list[(i + 1) % len(players_list)] for i in range(len(players_list))]
                            player_have_play = True
                    else:
                        # Finish the round and update player status
                        player_have_play = True
                        for each_player in players_list:
                            if each_player.score >= ELIMINATION_SCORE_THRESHOLD and not each_player.is_eliminate:
                                each_player.is_eliminate = True

                            # Update player rankings
                            eliminated_count = sum(1 for player in players_list if player.is_eliminate)
                            if each_player.ranking == 0 and each_player.is_eliminate:
                                each_player.ranking = (len(players_list) - eliminated_count) + 1

                        # Reset the round number for the next round
                        round_number = 1

                break


def play_game(players_list):
    """
        Main function to play the card game.

        Parameters:
        - players_list (list): List of Player objects.
        """

    # Initialization of round number count
    round_number = 1
    # Initialization of the list to keep track of scores for each_round
    data_score = []
    # We do those actions until all players excecpt one are eliminated (means until end of the game)
    while sum(player.is_eliminate for player in players_list) < len(players_list) - 1:
        # Deck, pile, joker and player's hand initialization
        deck = pydealer.Deck()
        init_jokers(deck)
        draw_cards_to_players(players_list, deck)
        pile = draw_card_to_pile(deck)

        # Creation of the message used to display score for each round
        if round_number > 1:
            # If round_number is greater than 1, create a message_for_score_button
            message_for_score_button = calculate_players_score(data_score, players_list, round_number)
        # If round_number is not greater than 1, assign an empty string to message_for_score_button
        else:
            message_for_score_button = ''

        # Perform action of all the players for one round
        action(deck, pile, players_list, round_number, message_for_score_button)

        # Reset finish round to False
        reset_finish_round_for_each_player(players_list)

        # Switch players order for next round
        players_list = [players_list[(i + 1) % len(players_list)] for i in range(len(players_list))]

        round_number += 1

    # When the game is finished we display the final score table
    display_end_of_game_window(players)


if __name__ == "__main__":
    players = init_players()
    play_game(players)