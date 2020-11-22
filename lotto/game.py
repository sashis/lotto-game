import random
from time import sleep

from .config import terminal_width
from .helpers import valid_input
from .players import Player


class Bag:
    def __init__(self):
        self._kegs = random.sample(range(1, 91), k=90)
        self.current = None

    @property
    def remained(self):
        return len(self._kegs)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            keg = self._kegs.pop()
        except IndexError:
            self.current = None
            raise StopIteration
        self.current = keg
        return keg


class Lotto:
    def __init__(self, players: list[Player]):
        self.players = players
        self.kegs = Bag()

    @property
    def players_in_game(self):
        return [player for player in self.players if not player.has_lost]

    @property
    def winners(self):
        players_in_game = self.players_in_game
        if len(players_in_game) == 1:
            return players_in_game
        return [player for player in self.players if player.has_won]

    def play_game(self):
        for _ in self.kegs:
            self._refresh_board()
            self._play_turn()
            self._finish_turn()
            if self.winners:
                break
        self._refresh_board()
        return self.winners

    def _refresh_board(self):
        half_size = terminal_width // 2
        stats = (f'Новый бочонок: {self.kegs.current}'.ljust(half_size) +
                 f'(осталось {self.kegs.remained})'.rjust(half_size))
        print(stats)
        print('=' * 46)
        for player in self.players_in_game:
            print(player)
        print('\n')

    def _play_turn(self):
        keg = self.kegs.current
        for player in self.players_in_game:
            decision = valid_input(
                prompt=f'{player.name}, зачеркнуть цифру? (y/n)',
                value_type=str,
                default_value='y',
                validate=lambda v: v in ('y', 'n'),
                interact_cb=player.make_decision(keg)
            )
            player.marking = decision == 'y'
            player.play_keg(keg)
            if player.has_lost:
                print(f'{player.name} выбывает из игры.')

    @staticmethod
    def _finish_turn():
        print('\n')
        sleep(.5)
