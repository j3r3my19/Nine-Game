from pydealer.const import TOP

new_ranks_for_count_hand = {
    "values": {
        "Ace": 1,
        "King": 10,
        "Queen": 10,
        "Jack": 10,
        "10": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
        "Joker": -1
    }
}


class Player:
    def __init__(self, name):
        """
        Initialize a Player object.

        Parameters:
        - name (str): The name of the player.
        """
        self.hand = None
        self.name = name
        self.score = 0
        self.number_of_pass = 0
        self.is_eliminate = False
        self.ranking = 0
        self.finish_round = False
        self.score_round = 0

    def count_hand(self):
        """
        Calculate the total value of cards in the player's hand.

        Returns:
        - int: The total value of the cards in the hand.
        """
        count_cards_value = 0
        for card in self.hand:
            count_cards_value += new_ranks_for_count_hand['values'].get(card.value)
        return count_cards_value

    def pass_turn(self):
        """
        Increment the number of times the player has passed ots turn.
        """
        self.number_of_pass += 1

    def finish_round(self, players_list):
        """
        Finish the current round and calculate scores.

        Parameters:
        - players_list (list): List of Player objects.

        Returns:
        - bool: True if the round is finished, False otherwise.
        """

        # Initialize finish_round flag to True
        finish_round = True

        # Update the player's round-specific attributes
        self.finish_round = True
        self.score_round = 0

        # Iterate through each player in the players_list
        for player in players_list:
            # Display the score only if the player is not already eliminated
            # and is not the one who chose to finish the round
            if (player.name != self.name) and (player.is_eliminate is False):

                # If the player who played has a score greater or equal to other players
                if (self.count_hand()) >= int(player.count_hand()):
                    # Add 25 points to the player who played
                    self.score += 25
                    self.score_round = 25

                    # If the other player's score is less than 0, subtract that amount; otherwise, add 0 points
                    if int(player.count_hand()) < 0:
                        player.score += int(player.count_hand())
                        player.score_round = int(player.count_hand())

                # If the player who played has a score lower than other players,
                # add their scores to the other players
                else:
                    player.score += int(player.count_hand())
                    player.score_round = int(player.count_hand())

            else:
                # Calculate the score of the player who played if they won
                counter = 0

                # Check if the player is not the one who chose to finish the round and is not already eliminated
                if (player.name != self.name) and not player.is_eliminate:

                    # If the player who played has a score greater or equal to other players, increment the counter
                    if (self.count_hand()) >= int(player.count_hand()):
                        counter += 1

                # If the counter is 0, no player has a score greater than or equal to the player who played
                if counter == 0 and not player.is_eliminate:
                    # If the player who played has a score less than 0, subtract that amount; otherwise, add 0 points
                    if int(self.count_hand()) < 0:
                        self.score += self.count_hand()
                        self.score_round = self.count_hand()

        return finish_round

    def play_card(self, pile, cards_played):
        """
        Add the card played to the top of the pile and remove from player's hand.

        Parameters:
        - pile (pydealer.Stack): The pile of cards played in the round.
        - list_cards_to_play (list): List of cards to play.
        """
        for card_to_play in cards_played:
            for card in self.hand:
                if str(card) == card_to_play:
                    self.hand.get(str(card))
                    pile.add(card, end=TOP)

    def play(self, deck, pile, cards_played, pile_chose, deck_chose):
        """
        Play a card from the player's hand, update the pile, and pick a card from the deck or pile.

        Parameters:
        - deck (pydealer.Deck): The deck of cards.
        - pile (pydealer.Stack): The pile of cards.
        - cards_played (list): List of cards played by the player.
        - pile_chose (list): The first card from the pile.
        - deck_chose (list): The first card from the deck.
        """

        # Play a card from the player's hand and update the pile
        self.play_card(pile, cards_played)

        # Pick a card from the deck or pile
        self.pick_card(deck, pile, cards_played, pile_chose, deck_chose)

    def pick_card(self, deck, pile, cards_played, pile_chose, deck_chose):
        """
        Allow the player to pick a card from the deck or pile.

        Parameters:
        - deck (pydealer.Deck): The deck of cards.
        - pile (pydealer.Stack): The pile of cards.
        - cards_played (list): List of cards played by the player.
        - pile_chose (list): The first card from the pile.
        - deck_chose (list): The first card from the deck.
        """

        # If a card is chosen from the deck
        if len(deck_chose) == 1:
            # Get the last card from the deck and add it to the player's hand
            cards = deck.get(f'{deck.cards[int(len(deck.cards) - 1)]}')
            self.hand.add(cards)

        # If a card is chosen from the pile
        elif len(pile_chose) == 1:
            # Get the last card from the pile and add it to the player's hand
            cards = pile.get(f'{pile.cards[int(len(pile.cards) - len(set(cards_played))) - 1]}')
            self.hand.add(cards)
