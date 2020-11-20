from random import randint, sample


class Card:
    def __init__(self):
        self._rows = make_lotto_card()
        self._numbers = set(n for row in self._rows for n in row if n != 0)
        self._marked = set()

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self._numbers == other._numbers

    def __contains__(self, item):
        return item in self._numbers

    def mark_number(self, number):
        try:
            self._numbers.remove(number)
        except KeyError:
            raise ValueError(f'{number} is not in card.')
        self._marked.add(number)


def make_lotto_card():
    card = [[0], [0], [0]]
    while not all(map(valid_column, zip(*card))):
        card = [make_row() for _ in range(3)]
    return card


def make_row() -> list[int]:
    def get_rand(column: int) -> int:
        min_ = column * 10 or 1
        max_ = column * 10 + 9 if column < 8 else 90
        return randint(min_, max_)

    row = sample([0, 1], counts=[4, 5], k=9)
    return [get_rand(col) * i for col, i in enumerate(row)]


def valid_column(column: list[int]) -> bool:
    only_nums = [x for x in column if x != 0]
    no_repeats = len(only_nums) == len(set(only_nums))
    return no_repeats and 0 < len(only_nums) < 3
