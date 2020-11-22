from .config import LottoConfig, terminal_width
from .game import Lotto


def run():
    print('Лото (консольная версия).'.center(terminal_width), '\n')
    cfg = LottoConfig()
    lotto = Lotto(**cfg.as_params)
    winners = lotto.play_game()
    if not winners:
        print('Нет победителей.\n')
    else:
        names = ', '.join(p.name for p in winners)
        print(f'Поздравляем, {names}, с победой!!!\n')
