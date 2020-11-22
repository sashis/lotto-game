from abc import ABC, abstractmethod

from .cards import Card
from .helpers import make_printable_card


class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.card = Card()
        self.marking = None
        self.has_lost = False

    def __str__(self):
        return make_printable_card(self.card.as_table, f' {self.name} ')

    @abstractmethod
    def make_decision(self, keg):
        pass

    def play_keg(self, keg):
        if self.marking:
            try:
                self.card.mark_number(keg)
            except ValueError:
                self.has_lost = True
        else:
            if keg in self.card:
                self.has_lost = True

    @property
    def has_won(self):
        return not self.has_lost and self.card.all_marked


class ComputerPlayer(Player):
    def make_decision(self, keg):
        decision = 'y' if keg in self.card else 'n'

        def interact():
            print(decision)
            return decision
        return interact


class HumanPlayer(Player):
    def make_decision(self, keg):
        return input
