from .helpers import valid_input
from .players import ComputerPlayer, HumanPlayer, Player

terminal_width = 46


class LottoConfig:
    def __init__(self):
        self.max_count = 5
        self.player_types = {
            'человек': HumanPlayer,
            'компьютер': ComputerPlayer
        }
        self._players: list[Player] = []
        for _ in range(self._set_player_count()):
            self._set_player()

    def _set_player_count(self):
        return valid_input(
            prompt=f'Сколько будет игроков (2-{self.max_count})',
            value_type=int,
            default_value=2,
            validate=lambda v: 2 <= v <= self.max_count
        )

    def _set_player(self):
        idx_player = len(self._players) + 1
        print(f'Параметры игрока #{idx_player}')
        type_cls = self._choose_player_type()
        name = self._choose_player_name()
        self._players.append(type_cls(name))

    def _choose_player_type(self):
        types_name = list(self.player_types.keys())
        types_cnt = len(types_name)
        type_idx = valid_input(
            prompt=f'Тип игрока ({"/".join(types_name)})',
            value_type=int,
            default_value=1,
            validate=lambda v: 1 <= v <= types_cnt
        )
        return self.player_types[types_name[type_idx - 1]]

    def _choose_player_name(self):
        used_names = [p.name for p in self._players]
        default_name = f'Игрок{len(used_names) + 1}'
        return valid_input(
            prompt='Имя игрока',
            value_type=str,
            default_value=default_name,
            validate=lambda v: v not in used_names
        )

    @property
    def as_params(self):
        return {'players': self._players}
