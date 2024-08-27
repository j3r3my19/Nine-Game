import tkinter as tk
from PIL import Image, ImageTk
import player_class
from tkinter import ttk
import random
from tabulate import tabulate
import sys
from tkinter import messagebox
import locale



NUMBER_TO_END_ROUND = 9

ELIMINATION_SCORE_THRESHOLD = 150


def close_window(root):
    """
        Closes the given Tkinter root window.

        Parameters:
        - root (Tk): The Tkinter root window to be closed.
    """
    root.destroy()


def display_button_pile(card_images_tk, pile, root, pile_chose, display_type, image_width, image_height,
                        minimum_cards_to_make_list, cards_played):
    """
    Displays a button representing the top card of the pile.

    Parameters:
    - card_images_tk: List to store Tkinter PhotoImage references for card images.
    - pile: The card pile to be displayed.
    - root: The Tkinter root window.
    - pile_chose: List to store the chosen pile.
    - display_type: Type of display ('temp' for temporary display, 'final' for clickable display).
    - image_width: Width of the board game image.
    - image_height: Height of the board game image.
    - minimum_cards_to_make_list: A list containing a single boolean flag indicating the minimum cards to form a list.
    - cards_played: List of cards currently played in the round.
    """

    card_pile = pile.cards[int(len(pile.cards)) - 1]
    card_image_path = f"./images/{card_pile}.png"
    card_image = Image.open(card_image_path)
    card_image = card_image.resize((100, 125))
    center_x = image_width // 2
    center_y = image_height // 2
    y_decalage = 100
    x_decalage = 80

    # Convert the card image to a Tkinter PhotoImage and store the reference
    card_image_tk = ImageTk.PhotoImage(card_image)
    card_images_tk.append(card_image_tk)

    if display_type == 'temp':
        # Display a temporary button without any functionality
        button_pile = tk.Button(root, image=card_image_tk, command=lambda: None)

        # Set the position of the button
        button_pile.place(x=center_x + x_decalage, y=center_y - y_decalage)

    else:
        # Display a clickable button for picking the pile
        button_pile = tk.Button(root, image=card_image_tk,
                                command=lambda: click_to_pick_pile(root, pile_chose, card_pile,
                                                                   minimum_cards_to_make_list, cards_played,
                                                                   image_width, image_height))
        # Set the position of the button
        button_pile.place(x=center_x + x_decalage, y=center_y - y_decalage)


def click_to_pick_pile(root, pile_chose, card_pile, minimum_cards_to_make_list, cards_played, image_width,
                       image_height):
    """
    Handles the logic when a player clicks to pick cards from a pile.

    Parameters:
    - root: The Tkinter root window.
    - pile_chose: List to store the chosen pile.
    - card_pile: The card pile to be chosen.
    - minimum_cards_to_make_list: A list containing a single boolean flag indicating the minimum cards to form a list.
    - cards_played: List of cards currently played in the round.
    - image_width: Width of the card image.
    - image_height: Height of the card image.
    """

    if minimum_cards_to_make_list[0]:
        # Minimum cards condition is met

        if len(cards_played) >= 1:
            # Close the current window and add the chosen pile to the list
            close_window(root)
            pile_chose.append(card_pile)
        else:
            # Display an error message if no cards are played
            display_no_card_played_message(image_width, image_height)
    else:
        # Minimum cards condition is not met

        if len(cards_played) == 0:
            # Display an error message if no cards are played
            display_no_card_played_message(image_width, image_height)
        else:
            # Display an error message if the wrong card combination is played
            display_wrong_card_message(image_width, image_height)


def display_button_deck(card_images_tk, deck, root, deck_chose, display_type, image_width, image_height,
                        minimum_cards_to_make_list, cards_played):
    """
    Displays a button representing the top card of the deck.

    Parameters:
    - card_images_tk: List to store Tkinter PhotoImage references for card images.
    - deck: The card deck to be displayed.
    - root: The Tkinter root window.
    - deck_chose: List to store the chosen deck.
    - display_type: Type of display ('temp' for temporary display, 'final' for clickable display).
    - image_width: Width of the board game image.
    - image_height: Height of the board game image.
    - minimum_cards_to_make_list: A list containing a single boolean flag indicating the minimum cards to form a list.
    - cards_played: List of cards currently played in the round.
    """

    card_deck = deck.cards[int(len(deck.cards) - 1)]
    card_image_path = f"./images/Back.png"
    card_image = Image.open(card_image_path)
    card_image = card_image.resize((100, 125))
    center_x = image_width // 2
    center_y = image_height // 2
    y_decalage = 100
    x_decalage = 40

    card_image_tk = ImageTk.PhotoImage(card_image)
    card_images_tk.append(card_image_tk)

    if display_type == 'temp':
        # Display a temporary button without any functionality
        button_deck = tk.Button(root, image=card_image_tk, command=lambda: None)

        # Set the position of the button
        button_deck.place(x=center_x - x_decalage, y=center_y - y_decalage)

    else:
        # Display a clickable button for picking the deck
        button_deck = tk.Button(root, image=card_image_tk,
                                command=lambda: click_to_pick_deck(root, deck_chose, card_deck,
                                                                   minimum_cards_to_make_list, cards_played,
                                                                   image_width, image_height))

        # Set the position of the button
        button_deck.place(x=center_x - x_decalage, y=center_y - y_decalage)


def click_to_pick_deck(root, deck_chose, card_deck, minimum_cards_to_make_list, cards_played, image_width,
                       image_height):
    """
    Handles the logic when a player clicks to pick cards from the deck.

    Parameters:
    - root: The Tkinter root window.
    - deck_chose: List to store the chosen deck.
    - card_deck: The card deck to be chosen.
    - minimum_cards_to_make_list: A list containing a single boolean flag indicating the minimum cards to form a list.
    - cards_played: List of cards currently played in the round.
    - image_width: Width of the board game image.
    - image_height: Height of the board game image.
    """

    if minimum_cards_to_make_list[0]:
        # Minimum cards condition is met

        if len(cards_played) >= 1:
            # Close the current window and add the chosen deck to the list
            close_window(root)
            deck_chose.append(card_deck)
        else:
            # Display an error message if no cards are played
            display_no_card_played_message(image_width, image_height)
    else:
        # Minimum cards condition is not met

        if len(cards_played) == 0:
            # Display an error message if no cards are played
            display_no_card_played_message(image_width, image_height)
        else:
            # Display an error message if the wrong card combination is played
            display_wrong_card_message(image_width, image_height)


def display_finish_button(root, player, players_list, display_type, left_panel, round_number):
    """
    Displays a "FINISH" button for a player if they have fewer cards than a specified minimum.

    Parameters:
    - root: The Tkinter root window.
    - player: The current player.
    - players_list: List of players in the game.
    - display_type: Type of display ('normal' for regular display).
    - left_panel: Tkinter frame where the button is displayed.
    - round_number: Current round number.
    """

    style = ttk.Style()
    style.configure("TButton", padding=10, relief="flat", background="white", foreground="black", font=('Arial', 12))

    if player_class.Player.count_hand(player) <= NUMBER_TO_END_ROUND:
        # Check if the player has fewer cards than the minimum to end the round

        if display_type == 'normal':
            # Display the "FINISH" button
            button_finish = ttk.Button(left_panel, text="END ROUND",
                                       command=lambda: click_to_finish(player, players_list, root, round_number),
                                       style='TButton')
            button_finish.pack(pady=10)


def click_to_finish(player, players_list, root, round_number):
    """
    Handles the logic when a player clicks to finish their turn.

    Parameters:
    - player: The current player.
    - players_list: List of players in the game.
    - root: The Tkinter root window.
    - round_number: Current round number.
    """

    # Close the current window
    close_window(root)

    # Finish the player's round and update the scores
    player_class.Player.finish_round(player, players_list)

    # Display the end-of-round scores
    display_end_of_round_window(players_list, round_number)


def display_pass_button(root, player, display_type, player_pass, left_panel):
    """
    Displays a "PASS" button for a player if they have passes available.

    Parameters:
    - root: The Tkinter root window.
    - player: The current player.
    - display_type: Type of display ('normal' for regular display).
    - player_pass: List to store information about player passes.
    - left_panel: Tkinter frame where the button is displayed.
    """

    style = ttk.Style()
    style.configure("TButton", padding=10, relief="flat", background="white", foreground="black", font=('Arial', 12))

    if player.number_of_pass < 1:
        # Check if the player has passes available

        if display_type == 'normal':
            # Display the "PASS" button
            text = 'True'
            button_pass = ttk.Button(left_panel, text="PASS",
                                     command=lambda: click_to_pass(player, root, player_pass, text), style='TButton')
            button_pass.pack(pady=10)


def click_to_pass(player, root, player_pass, text):
    """
    Handles the logic when a player clicks to pass their turn.

    Parameters:
    - player: The current player.
    - root: The Tkinter root window.
    - player_pass: List to store information about player passes.
    - text: A string indicating the pass action.
    """

    # Close the current window
    close_window(root)

    # Append pass information to the list
    player_pass.append(text)

    # Update player's pass count
    player_class.Player.pass_turn(player)


def display_score_button(root, left_panel, message):
    """
    Displays a "SCORE" button.

    Parameters:
    - root: The Tkinter root window.
    - left_panel: Tkinter frame where the button is displayed.
    - message: The message to display when the button is clicked: historical of scores of each player and each round
    """

    style = ttk.Style()
    style.configure("TButton", padding=10, relief="flat", background="white", foreground="black")

    # Display the "SCORE" button
    button_score = ttk.Button(left_panel, text="SCORE", command=lambda: click_score_button(root, message),
                              style="TButton")
    button_score.pack(pady=10)


def click_score_button(root, message):
    """
    Handles the logic when the "SCORE" button is clicked.

    Parameters:
    - root: The Tkinter root window.
    - message: The message to display in the new window.
    """

    # Create a new window
    message_window = tk.Toplevel(root)

    # Set the message in the window
    label = tk.Label(message_window, text=message)
    label.pack(padx=20, pady=20)


def display_quit_button(root, left_panel):
    """
    Displays a "QUIT" button.

    Parameters:
    - root: The Tkinter root window.
    - left_panel: Tkinter frame where the button is displayed.
    - message: The message to display when the button is clicked: historical of scores of each player and each round
    """

    style = ttk.Style()
    style.configure("TButton", padding=10, relief="flat", background="white", foreground="black")

    # Display the "SCORE" button
    button_score = ttk.Button(left_panel, text="QUIT GAME", command=lambda: click_quit_button(root),
                              style="TButton")
    button_score.pack(pady=10)


def click_quit_button(root):
    """
    Handles the logic when the "QUIT" button is clicked.

    Parameters:
    - root: The Tkinter root window.
    - message: The message to display in the new window.
    """
    response = messagebox.askyesno("Confirm Quit", "Are you sure you want to quit?")
    if response:  # If the user clicked "Yes"
        root.destroy()  # Closes the Tkinter window
        sys.exit()      # Terminates the Python program completely



def display_players_score_left_panel(players_list, left_panel):
    """
    Displays a table of players' scores in the left panel.

    Parameters:
    - players_list: List of players in the game.
    - left_panel: Tkinter frame where the table is displayed.
    """

    # Create a table with player names and scores
    table = []
    for player in players_list:
        player_table = [player.name, player.score]
        table.append(player_table)

    # Sort the table based on scores in descending order
    sorted_table = sorted(table, key=lambda x: x[1], reverse=True)
    col_names = ["Player", "Score"]

    # Display the table in the left panel
    label = ttk.Label(left_panel, text=tabulate(sorted_table, headers=col_names), justify='left', font=('Arial', 13))
    label.pack(side='bottom', pady=100)


def display_end_of_round_window(players_list, round_number):
    """
    Displays a window at the end of the round showing scores and relevant information.

    Parameters:
    - players_list: List of players in the game.
    - round_number: Current round number.
    """

    # Create the Tkinter root window
    root = tk.Tk()
    root.title(f"END OF ROUND {round_number}")

    # Create a frame to hold the table
    frame = ttk.Frame(root)
    frame.pack()

    # Create a label for displaying the round number
    message = ttk.Label(frame, text=f"END OF ROUND {round_number}\n")
    message.pack(pady=10)

    # Create a label for displaying the round number
    message = ttk.Label(frame, text=f"{players_list[0].name} decided to end the round.")
    message.pack(pady=10)

    # Display information about each player's hand
    for player in players_list:
        if not player.is_eliminate:
            player.count_hand()
            text = f'{player.name} has {player.count_hand()}'
            additional_text = ttk.Label(frame, text=text)
            additional_text.pack()

    # Display elimination information for players with scores above the threshold
    for each_player in players_list:
        if each_player.score >= ELIMINATION_SCORE_THRESHOLD and not each_player.is_eliminate:
            text = f'{each_player.name} has {each_player.score} and is eliminated'
            additional_text = ttk.Label(frame, text=text)
            additional_text.pack()

    # Display the table of player scores
    table = table_players_score_end_of_round_and_game(players_list)
    table_label = ttk.Label(frame, text=table)
    table_label.pack()

    # Start the main loop to display the window
    root.mainloop()


def display_end_of_game_window(players_list):
    """
    Displays a window at the end of the game showing final player scores and rankings.

    Parameters:
    - players_list: List of players in the game.
    """

    # Create the Tkinter root window
    root = tk.Tk()
    root.title("END OF GAME: Player Scores")

    # Create a frame to hold the table
    frame = ttk.Frame(root)
    frame.pack()

    # Create a label for displaying the end-of-game message
    message = ttk.Label(frame, text="END OF GAME: Player Scores")
    message.pack(pady=10)

    # Display the table of player scores
    table = table_players_score_end_of_round_and_game(players_list)
    table_label = ttk.Label(frame, text=table)
    table_label.pack()

    # Display information about each player's final ranking and score
    score_table = []
    for player in players_list:
        score_tuple = (player.score, player.name, player.ranking)
        score_table.append(score_tuple)

    for element in sorted(score_table, key=lambda x: x[2]):
        if element[2] == 0:
            text = f"{element[1]} finishes in position 1 with a score of {element[0]}"
            additional_text = ttk.Label(frame, text=text)
        else:
            text = f"{element[1]} finishes in position {element[2]} with a score of {element[0]}"
            additional_text = ttk.Label(frame, text=text)

        additional_text.pack()

    # Start the main loop to display the window
    root.mainloop()


def table_players_score_end_of_round_and_game(players_list):
    """
    Creates and formats a table of player names and scores.

    Parameters:
    - players_list: List of players in the game.

    Returns:
    A formatted table of player names and scores.
    """
    # Create a table with player names and scores
    table = []
    for player in players_list:
        player_table = [player.name, player.score]
        table.append(player_table)

    # Sort the table based on scores in descending order
    sorted_table = sorted(table, key=lambda x: x[1], reverse=True)
    col_names = ["Player", "Score"]

    # Format the table using the tabulate function
    final_table = tabulate(sorted_table, headers=col_names)

    # Return the formatted table
    return final_table


def display_current_round_left_panel(left_panel, round_number):
    """
    Displays the current round number in the left panel.

    Parameters:
    - left_panel: Tkinter frame where the round number is displayed.
    - round_number: The current round number.
    """

    # Create a label to display the current round number
    label_text = tk.Label(left_panel, text=f"ROUND {round_number}")
    label_text.configure(font=("Arial", 20))  # Increase the font size for better visibility
    label_text.pack(pady=10)


def display_button_to_switch_players(root, display_type):
    """
    Displays a full window button to close the window in temporary mode, and switch to the other player.

    Parameters:
    - root: Tkinter root window.
    - display_type: Type of display mode ('temp' for temporary).
    """

    if display_type == 'temp':
        # Create a button to close the window
        button = tk.Button(root, text="Close Window", command=root.destroy)
        button.pack()

        # Bind the button to a left-click event, effectively closing the window
        root.bind("<Button-1>", lambda event: button.invoke())


def calculate_card_positions(num_players, img_width, img_height):
    """
    Calculate the initial positions for players' cards based on the number of players.

    Parameters:
    - num_players: Number of players in the game.
    - img_width: Width of the board game image.
    - img_height: Height of the board game image.

    Returns:
    A list of tuples representing the initial positions for players' cards.
    """
    decalage = 40  # Adjustment for spacing between positions

    if num_players == 2:
        return [(img_width // 2, img_height // 4), (img_width // 2, 3 * img_height // 4)]
    elif num_players == 3:
        return [(img_width // 2, img_height // 4), (img_width // 4, (img_height // 2) + 180),
                (3 * img_width // 4, (img_height // 2) + 180)]
    elif num_players == 4:
        return [(img_width // 4, img_height // 4), (3 * img_width // 4, img_height // 4),
                (img_width // 4, 3 * img_height // 4), (3 * img_width // 4, 3 * img_height // 4)]
    elif num_players == 5:
        return [(img_width // 2, img_height // 4 - decalage),
                (3 * img_width // 4, img_height // 2 - decalage),
                (img_width // 4, 3 * img_height // 4 - decalage),
                (3 * img_width // 4, 3 * img_height // 4 - decalage),
                (img_width // 4, (img_height // 2) - decalage)]
    elif num_players == 6:
        return [(img_width // 4, img_height // 4), (img_width // 2, img_height // 4),
                (3 * img_width // 4, img_height // 4),
                (img_width // 4, 3 * img_height // 4), (img_width // 2, 3 * img_height // 4),
                (3 * img_width // 4, 3 * img_height // 4)]
    else:
        return []


def display_player_environment(root, player, position, card_images_tk, players_list, cards_played, display_type,
                               player_pass, left_panel, index_player, round_number, pile_chose, deck_chose,
                               cards_played_for_check_multiple_cards, minimum_cards_to_make_list, image_width,
                               image_height):
    """
    Display the player's environment including their cards, name, and action buttons.

    Parameters:
    - root: Tkinter root window.
    - player: Player object representing the current player.
    - position: Tuple representing the initial position for displaying the player's cards.
    - card_images_tk: List to store Tkinter PhotoImage references for card images.
    - players_list: List of Player objects in the game.
    - cards_played: List of cards played in the current round.
    - display_type: Type of display mode ('temp' for temporary).
    - player_pass: List to track player pass actions.
    - left_panel: Tkinter frame for displaying player-related information.
    - index_player: Index of the current player in the players_list.
    - round_number: Current round number.
    - pile_chose: List to track pile choices.
    - deck_chose: List to track deck choices.
    - cards_played_for_check_multiple_cards: List to track played cards for checking multiple cards.
    - minimum_cards_to_make_list: List to track the minimum cards needed to make a move.
    - image_width: Width of the board game image.
    - image_height: Height of the board game image.
    """
    counter = 1
    x, y = position
    for index, card in enumerate(player.hand):
        # We show the cards in visible side for the player which plays (index = 0)
        if index_player == 0:
            # Load card image
            card_image_path = f"./images/{card}.png"
            card_image = Image.open(card_image_path)
            card_image = card_image.resize((100, 125))

            # Convert the card image to a Tkinter PhotoImage and store the reference
            card_image_tk = ImageTk.PhotoImage(card_image)
            card_images_tk.append(card_image_tk)
            # We display the first card of the hand and the buttons finish and pass only one time (for the first card
            # of the hand)
            if index == 0:
                x = display_player_cards(root, card_image_tk, card, x, y, cards_played, display_type, pile_chose,
                                         deck_chose, cards_played_for_check_multiple_cards, minimum_cards_to_make_list,
                                         image_width, image_height, player)
                display_finish_button(root, player, players_list, display_type, left_panel, round_number)
                display_pass_button(root, player, display_type, player_pass, left_panel)

                display_player_name_adapt_to_number_of_cards(root, player, x, y)

            # We dislay the rest of the cards of the player's hand
            else:
                x = display_player_cards(root, card_image_tk, card, x, y, cards_played, display_type, pile_chose,
                                         deck_chose, cards_played_for_check_multiple_cards, minimum_cards_to_make_list,
                                         image_width, image_height, player)
        else:
            # We show the cards in hidden side for the other players
            if counter == 1:
                # Load card image
                card_image_path = f"./images/back.png"
                card_image = Image.open(card_image_path)
                card_image = card_image.resize((100, 125))

                # Convert the card image to a Tkinter PhotoImage and store the reference
                card_image_tk = ImageTk.PhotoImage(card_image)
                card_images_tk.append(card_image_tk)
                display_type = 'temp'
                x = display_player_cards(root, card_image_tk, card, x, y, cards_played, display_type, pile_chose,
                                         deck_chose, cards_played_for_check_multiple_cards, minimum_cards_to_make_list,
                                         image_width, image_height, player)

                display_player_name_adapt_to_number_of_cards(root, player, x, y)

                counter += 1

            else:
                # Load card image
                card_image_path = f"./images/back.png"
                card_image = Image.open(card_image_path)
                card_image = card_image.resize((100, 125))

                # Convert the card image to a Tkinter PhotoImage and store the reference
                card_image_tk = ImageTk.PhotoImage(card_image)
                card_images_tk.append(card_image_tk)
                display_type = 'temp'
                x = display_player_cards(root, card_image_tk, card, x, y, cards_played, display_type, pile_chose,
                                         deck_chose, cards_played_for_check_multiple_cards, minimum_cards_to_make_list,
                                         image_width, image_height, player)


def display_player_cards(root, card_image_tk, card, x, y, cards_played, display_type, pile_chose, deck_chose,
                         cards_played_for_check_multiple_cards, minimum_cards_to_make_list, image_width, image_height,
                         player):
    """
    Display a player's card on the user interface.

    Parameters:
    - root: Tkinter root window.
    - card_image_tk: Tkinter PhotoImage reference for the card image.
    - card: Card object representing the displayed card.
    - x, y: Initial position coordinates for displaying the card.
    - cards_played: List of cards played in the current round.
    - display_type: Type of display mode ('temp' for temporary).
    - pile_chose: List to track pile choices.
    - deck_chose: List to track deck choices.
    - cards_played_for_check_multiple_cards: List to track played cards for checking multiple cards.
    - minimum_cards_to_make_list: List to track the minimum cards needed to make a move.
    - image_width: Width of the board game image.
    - image_height: Height of the board game image.
    - player: Player object representing the current player.

    Returns:
    Updated x-coordinate value for the next card position.
    """
    twinkling_colors = ["black", "black"]
    if display_type == 'temp':
        # Create a Button widget with the card image as the background
        button_card = tk.Button(root, image=card_image_tk, command=lambda: None)

        # Set the position of the button
        if len(pile_chose) == 1:
            if card.name == pile_chose[0].name:
                display_button_card_adapt_to_number_of_cards(player, button_card, x, y)
                twinkling_effect(button_card, twinkling_colors)
            else:
                display_button_card_adapt_to_number_of_cards(player, button_card, x, y)
        elif len(deck_chose) == 1:
            if card.name == deck_chose[0].name:
                twinkling_effect(button_card, twinkling_colors)
                display_button_card_adapt_to_number_of_cards(player, button_card, x, y)
            else:
                display_button_card_adapt_to_number_of_cards(player, button_card, x, y)
        else:
            display_button_card_adapt_to_number_of_cards(player, button_card, x, y)

        x += 40  # Adjust the value to control the spacing between cards
        return x
    else:
        clicked_flag = [False]
        # Create a Button widget with the card image as the background
        button_card = tk.Button(root, image=card_image_tk,
                                command=lambda: click_to_play_cards(card, cards_played, button_card, clicked_flag,
                                                                    cards_played_for_check_multiple_cards,
                                                                    minimum_cards_to_make_list, image_width,
                                                                    image_height))

        display_button_card_adapt_to_number_of_cards(player, button_card, x, y)

        x += 40  # Adjust the value to control the spacing between cards

        return x


def display_button_card_adapt_to_number_of_cards(player, button_card, x, y):
    """
    Adjust the position of the card button based on the number of cards in the player's hand.

    Parameters:
    - player: Player object representing the current player.
    - button_card: Tkinter Button widget representing the card button.
    - x, y: Initial position coordinates for displaying the card.

    Returns:
    None.
    """
    if len(player.hand) == 1:
        # Set the position of the button
        button_card.place(x=x + 20, y=y - 100)
    elif len(player.hand) == 2:
        # Set the position of the button
        button_card.place(x=x, y=y - 100)
    elif len(player.hand) == 3:
        # Set the position of the button
        button_card.place(x=x - 20, y=y - 100)
    elif len(player.hand) == 4:
        # Set the position of the button
        button_card.place(x=x - 40, y=y - 100)
    else:
        button_card.place(x=x - 60, y=y - 100)


def display_player_name_adapt_to_number_of_cards(root, player, x, y):
    """
    Display the player's name on the GUI window and adjust its position based on the number of cards in the player's hand.

    Parameters:
    - root: Tkinter root window object.
    - player: Player object representing the current player.
    - x, y: Initial position coordinates for displaying the player's name.

    Returns:
    None.
    """
    if len(player.hand) == 5:
        label_text = tk.Label(root, text=f"{player.name}")
        label_text.place(x=x, y=y + 40)
        label_text.configure(font=("Arial", 12), foreground="black")
    if len(player.hand) == 4:
        label_text = tk.Label(root, text=f"{player.name}")
        label_text.place(x=x + 10, y=y + 40)
        label_text.configure(font=("Arial", 12), foreground="black")
    if len(player.hand) == 3:
        label_text = tk.Label(root, text=f"{player.name}")
        label_text.place(x=x + 10, y=y + 40)
        label_text.configure(font=("Arial", 12), foreground="black")
    if len(player.hand) == 2:
        label_text = tk.Label(root, text=f"{player.name}")
        label_text.place(x=x + 10, y=y + 40)
        label_text.configure(font=("Arial", 12), foreground="black")
    if len(player.hand) == 1:
        label_text = tk.Label(root, text=f"{player.name}")
        label_text.place(x=x + 20, y=y + 40)
        label_text.configure(font=("Arial", 12), foreground="black")


def twinkling_effect(button, colors):
    """
    Apply a twinkling effect to a Tkinter Button by randomly changing its background color.

    Parameters:
    - button: Tkinter Button widget to apply the twinkling effect.
    - colors: List of colors to randomly choose from for the twinkling effect.

    Returns:
    None.
    """

    def change_color():
        new_color = random.choice(colors)
        button.configure(background=new_color)

    change_color()


def click_to_play_cards(card, cards_played, button_card, clicked_flag,
                        cards_played_for_check_multiple_cards, minimum_cards_to_make_list, image_width, image_height):
    """
    Handles the logic when a player clicks to play a card.

    Parameters:
    - card: The card object clicked by the player.
    - cards_played: List of cards currently played in the round.
    - button_card: The Tkinter button associated with the played card.
    - clicked_flag: A list containing a single boolean flag indicating whether a card is currently clicked.
    - cards_played_for_check_multiple_cards: List of cards played, used for checking multiple card plays.
    - minimum_cards_to_make_list: A list containing a single boolean flag indicating the minimum cards to form a list.
    - image_width: Width of the board game image.
    - image_height: Height of the board game image.
    """

    # Dictionary to map card ranks to numerical values for comparison
    new_ranks_for_suit = {
        "values": {
            "Ace": 1,
            "King": 13,
            "Queen": 12,
            "Jack": 11,
            "10": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2,
        }
    }

    if not clicked_flag[0]:
        # Player is clicking to play a card

        cards_played.append(str(card))
        cards_played_for_check_multiple_cards.append(card)

        if len(cards_played) > 1:
            # Checking for valid card plays with multiple cards

            cards_value = []
            for card in set(cards_played_for_check_multiple_cards):
                temp_dict = {'value': card.value, 'suit': card.suit}
                cards_value.append(temp_dict)

            if all(card['value'] == cards_value[0]['value'] for card in cards_value):
                # All cards have the same rank
                new_x = button_card.winfo_x()  # Adjust the value as needed
                new_y = button_card.winfo_y() - 20  # Adjust the value as needed
                button_card.place(x=new_x, y=new_y)
                clicked_flag[0] = True
                minimum_cards_to_make_list[0] = True

            elif (all(card['suit'] == cards_value[0]['suit'] for card in cards_value)) and len(cards_value) == 2:
                # Cards have the same suit and form a sequence of 2
                value = [new_ranks_for_suit['values'].get(card['value']) for card in cards_value]
                if int(max(value)) - int(min(value)) == int(len(value)) - 1:
                    new_x = button_card.winfo_x()  # Adjust the value as needed
                    new_y = button_card.winfo_y() - 20  # Adjust the value as needed
                    button_card.place(x=new_x, y=new_y)
                    clicked_flag[0] = True
                    minimum_cards_to_make_list[0] = False
                else:
                    # Invalid sequence, display error message
                    cards_played.pop(-1)
                    cards_played_for_check_multiple_cards.pop(-1)
                    display_wrong_card_message(image_width, image_height)
                    if len(cards_played) == 1:
                        minimum_cards_to_make_list[0] = True
                    else:
                        minimum_cards_to_make_list[0] = False

            elif (all(card['suit'] == cards_value[0]['suit'] for card in cards_value)) and len(cards_value) > 2:
                # Cards have the same suit and form a sequence of more than 2
                value = [new_ranks_for_suit['values'].get(card['value']) for card in cards_value]
                if int(max(value)) - int(min(value)) == int(len(value)) - 1:
                    new_x = button_card.winfo_x()  # Adjust the value as needed
                    new_y = button_card.winfo_y() - 20  # Adjust the value as needed
                    button_card.place(x=new_x, y=new_y)
                    clicked_flag[0] = True
                    minimum_cards_to_make_list[0] = True
                else:
                    # Invalid sequence, display error message
                    cards_played.pop(-1)
                    cards_played_for_check_multiple_cards.pop(-1)
                    display_wrong_card_message(image_width, image_height)
                    minimum_cards_to_make_list[0] = assign_minimum_cards_to_make_list_for_playing_card(cards_played,
                                                                                                       cards_played_for_check_multiple_cards,
                                                                                                       minimum_cards_to_make_list,
                                                                                                       new_ranks_for_suit)
            else:
                # Invalid combination, display error message
                cards_played.pop(-1)
                cards_played_for_check_multiple_cards.pop(-1)
                display_wrong_card_message(image_width, image_height)
                minimum_cards_to_make_list[0] = assign_minimum_cards_to_make_list_for_playing_card(cards_played,
                                                                                                   cards_played_for_check_multiple_cards,
                                                                                                   minimum_cards_to_make_list,
                                                                                                   new_ranks_for_suit)

        else:
            # Single card play
            new_x = button_card.winfo_x()  # Adjust the value as needed
            new_y = button_card.winfo_y() - 20  # Adjust the value as needed
            button_card.place(x=new_x, y=new_y)
            clicked_flag[0] = True
            minimum_cards_to_make_list[0] = True

    else:
        # Player is clicking to remove a card from the played cards

        cards_played.remove(str(card))
        cards_played_for_check_multiple_cards.remove(card)
        button_card.winfo_x()
        new_y = button_card.winfo_y() + 20
        new_x = button_card.winfo_x()  # Adjust the value as needed
        button_card.place(x=new_x, y=new_y)
        clicked_flag[0] = False
        minimum_cards_to_make_list[0] = assign_minimum_cards_to_make_list_for_removing_card(cards_played,
                                                                                            cards_played_for_check_multiple_cards,
                                                                                            minimum_cards_to_make_list,
                                                                                            new_ranks_for_suit,
                                                                                            image_width, image_height)


def assign_minimum_cards_to_make_list_for_playing_card(cards_played, cards_played_for_check_multiple_cards,
                                                       minimum_cards_to_make_list, new_ranks_for_suit):
    """
    Determines the minimum number of cards required to form a valid play based on the cards played.

    Parameters:
    - cards_played: List of cards currently played in the round.
    - cards_played_for_check_multiple_cards: List of cards played, used for checking multiple card plays.
    - minimum_cards_to_make_list: A list containing a single boolean flag indicating the minimum cards to form a list.
    - new_ranks_for_suit: Dictionary mapping card ranks to numerical values for comparison.

    Returns:
    - bool: The updated value of the minimum_cards_to_make_list flag.
    """

    if len(cards_played) > 1:
        # Checking for valid card plays with multiple cards

        cards_value = []
        for card in set(cards_played_for_check_multiple_cards):
            temp_dict = {'value': card.value, 'suit': card.suit}
            cards_value.append(temp_dict)

        if all(card['value'] == cards_value[0]['value'] for card in cards_value):
            # All cards have the same rank
            minimum_cards_to_make_list[0] = True
            return minimum_cards_to_make_list[0]

        elif (all(card['suit'] == cards_value[0]['suit'] for card in cards_value)) and len(cards_value) == 2:
            # Cards have the same suit and form a sequence of 2
            value = [new_ranks_for_suit['values'].get(card['value']) for card in cards_value]
            if int(max(value)) - int(min(value)) == int(len(value)) - 1:
                minimum_cards_to_make_list[0] = False
                return minimum_cards_to_make_list[0]

        elif (all(card['suit'] == cards_value[0]['suit'] for card in cards_value)) and len(cards_value) > 2:
            # Cards have the same suit and form a sequence of more than 2
            value = [new_ranks_for_suit['values'].get(card['value']) for card in cards_value]
            if int(max(value)) - int(min(value)) == int(len(value)) - 1:
                minimum_cards_to_make_list[0] = True
                return minimum_cards_to_make_list[0]
            else:
                minimum_cards_to_make_list[0] = False
                return minimum_cards_to_make_list[0]

    else:
        # Single card play
        minimum_cards_to_make_list[0] = True
        return minimum_cards_to_make_list[0]


def assign_minimum_cards_to_make_list_for_removing_card(cards_played, cards_played_for_check_multiple_cards,
                                                        minimum_cards_to_make_list, new_ranks_for_suit, image_width,
                                                        image_height):
    """
    Determines the minimum number of cards required to form a valid play when removing a card.

    Parameters:
    - cards_played: List of cards currently played in the round.
    - cards_played_for_check_multiple_cards: List of cards played, used for checking multiple card plays.
    - minimum_cards_to_make_list: A list containing a single boolean flag indicating the minimum cards to form a list.
    - new_ranks_for_suit: Dictionary mapping card ranks to numerical values for comparison.
    - image_width: Width of the board game image.
    - image_height: Height of the board game image.

    Returns:
    - bool: The updated value of the minimum_cards_to_make_list flag.
    """

    if len(cards_played) > 1:
        # Checking for valid card plays with multiple cards

        cards_value = []
        for card in set(cards_played_for_check_multiple_cards):
            temp_dict = {'value': card.value, 'suit': card.suit}
            cards_value.append(temp_dict)

        if all(card['value'] == cards_value[0]['value'] for card in cards_value):
            # All cards have the same rank
            minimum_cards_to_make_list[0] = True
            return minimum_cards_to_make_list[0]

        elif (all(card['suit'] == cards_value[0]['suit'] for card in cards_value)) and len(cards_value) == 2:
            # Cards have the same suit and form a sequence of 2
            value = [new_ranks_for_suit['values'].get(card['value']) for card in cards_value]
            if int(max(value)) - int(min(value)) == int(len(value)) - 1:
                minimum_cards_to_make_list[0] = False
                return minimum_cards_to_make_list[0]

        elif (all(card['suit'] == cards_value[0]['suit'] for card in cards_value)) and len(cards_value) > 2:
            # Cards have the same suit and form a sequence of more than 2
            value = [new_ranks_for_suit['values'].get(card['value']) for card in cards_value]
            if int(max(value)) - int(min(value)) == int(len(value)) - 1:
                minimum_cards_to_make_list[0] = True
                return minimum_cards_to_make_list[0]
            else:
                minimum_cards_to_make_list[0] = False
                return minimum_cards_to_make_list[0]
        else:
            # Invalid combination, display error message
            display_wrong_card_message(image_width, image_height)
    elif len(cards_played) == 1:
        # One card left after removal
        minimum_cards_to_make_list[0] = True
        return minimum_cards_to_make_list[0]
    else:
        # No cards left  after removal, set to False
        minimum_cards_to_make_list[0] = False
        return minimum_cards_to_make_list[0]


def display_wrong_card_message(image_width, image_height):
    """
    Display a Tkinter window with an error message indicating that the played cards are invalid.

    Parameters:
    - image_width: Width of the board game image.
    - image_height: Height of the board game image.

    Returns:
    None.
    """
    root = tk.Tk()
    root.title("WRONG CARDS PLAYED ERROR")

    # Create a frame to hold the table
    frame = ttk.Frame(root)
    frame.pack()

    # Create a label or any other widget for displaying a message if needed
    message = ttk.Label(frame, text="ERROR: You cannot play those cards, you can play cards with same values, "
                                    "or suits with at least 3 cards.")
    message.pack(pady=10)

    x = (image_width - root.winfo_reqwidth()) / 2
    y = (image_height - root.winfo_reqheight()) / 2

    # Set the window position
    root.geometry("+%d+%d" % (x - 40, y))
    # Start the main loop to display the window
    root.mainloop()


def display_no_card_played_message(image_width, image_height):
    """
    Display a Tkinter window with an error message indicating that no card has been played before attempting
    to pick a card from the deck or pile.

    Parameters:
    - image_width: Width of the board game image.
    - image_height: Height of the board game image.

    Returns:
    None.
    """
    root = tk.Tk()
    root.title("NO CARDS PLAYED ERROR")

    # Create a frame to hold the table
    frame = ttk.Frame(root)
    frame.pack()

    # Create a label or any other widget for displaying a message if needed
    message = ttk.Label(frame, text="You must play a card before picking a card from the deck or pile")
    message.pack(pady=10)

    x = (image_width - root.winfo_reqwidth()) / 2
    y = (image_height - root.winfo_reqheight()) / 2

    # Set the window position
    root.geometry("+%d+%d" % (x + 50, y))

    # Start the main loop to display the window
    root.mainloop()


def display_game_board(players_list, pile, deck, round_number, display_type, pile_chose, deck_chose,
                       message_for_score_button):
    """
    Display the game board with players' cards, pile, and deck.

    Parameters:
    - players_list: List of Player objects representing the players in the game.
    - pile: Pile object representing the pile of cards.
    - deck: Deck object representing the deck of cards.
    - round_number: Current round number in the game.
    - display_type: Type of display, e.g., 'normal' or 'temp'.
    - pile_chose: List to store chosen pile cards.
    - deck_chose: List to store chosen deck cards.
    - message_for_score_button: Message to display on the score button.

    Returns:
    Tuple containing lists of cards played, chosen pile cards, chosen deck cards, and player pass status.
    """
    cards_played = []
    cards_played_for_check_multiple_cards = []
    player_pass = []
    minimum_cards_to_make_list = [True]

    # setup board game
    root = tk.Tk()
    root.title("Game Board")

    left_panel = tk.Frame(root, width=200, height=500, bg="lightgray")  # Adjust dimensions as needed
    left_panel.pack(side="left", fill="y")

    # Load the game board image
    game_board_path = "./images/Game_Board_Image.png"  # Replace with the actual path to your game board image
    game_board_image = Image.open(game_board_path)

    # Create a list to store PhotoImage objects
    card_images_tk = []

    image_width, image_height = game_board_image.size
    # Calculate positions based on the number of players
    card_positions = calculate_card_positions(len([player for player in players_list if not player.is_eliminate]),
                                              image_width, image_height)

    # Convert the final image to a Tkinter PhotoImage
    game_board_image_tk = ImageTk.PhotoImage(game_board_image)

    # Display the final image
    game_board_label = tk.Label(root, image=game_board_image_tk)
    game_board_label.image = game_board_image_tk
    game_board_label.pack()

    display_current_round_left_panel(left_panel, round_number)

    # Display the cards for players
    for index_player, player in enumerate([player for player in players_list if not player.is_eliminate]):
        position = card_positions[index_player]
        display_player_environment(root, player, position, card_images_tk, players_list, cards_played,
                                   display_type, player_pass, left_panel, index_player, round_number, pile_chose,
                                   deck_chose, cards_played_for_check_multiple_cards, minimum_cards_to_make_list,
                                   image_width, image_height)

    # Display the cards for pile and deck
    display_button_pile(card_images_tk, pile, root, pile_chose, display_type, image_width, image_height,
                        minimum_cards_to_make_list, cards_played)
    display_button_deck(card_images_tk, deck, root, deck_chose, display_type, image_width, image_height,
                        minimum_cards_to_make_list, cards_played)
    display_button_to_switch_players(root, display_type)
    display_players_score_left_panel(players_list, left_panel)

    if message_for_score_button:
        display_score_button(root, left_panel, message_for_score_button)

    display_quit_button(root, left_panel)

    root.mainloop()

    if len(player_pass) == 0:
        player_pass.append('False')

    return cards_played, pile_chose, deck_chose, player_pass
