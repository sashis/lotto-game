from pytest import mark, fixture, raises
from lotto import cards


@fixture
def lotto_card(monkeypatch):
    def mock_card():
        return [
            [0, 17,  0, 34, 45, 54, 62,  0,  0],
            [1, 14,  0,  0, 49, 56,  0,  0, 90],
            [5,  0, 27, 37,  0,  0, 63, 70,  0]
        ]
    monkeypatch.setattr(cards, 'make_lotto_card', mock_card)
    return cards.Card()


@mark.parametrize("column_numbers, is_valid", [
    ([0, 0, 0], False),
    ([0, 0, 1], True),
    ([0, 1, 2], True),
    ([1, 2, 3], False),
    ([0, 1, 1], False)
])
def test_valid_column(column_numbers, is_valid):
    assert cards.valid_column(column_numbers) == is_valid


@mark.parametrize("variant", range(10))
def test_make_row_five_numbers_in_row(variant):
    row = cards.make_row()
    assert len(row) == 9
    assert row.count(0) == 4


@mark.parametrize("variant", range(10))
def test_make_row_cell_values(variant):
    row = cards.make_row()
    assert 1 <= row[0] <= 9 or row[0] == 0
    assert 10 <= row[1] <= 19 or row[1] == 0
    assert 20 <= row[2] <= 29 or row[2] == 0
    assert 30 <= row[3] <= 39 or row[3] == 0
    assert 40 <= row[4] <= 49 or row[4] == 0
    assert 50 <= row[5] <= 59 or row[5] == 0
    assert 60 <= row[6] <= 69 or row[6] == 0
    assert 70 <= row[7] <= 79 or row[7] == 0
    assert 80 <= row[8] <= 90 or row[8] == 0


@mark.parametrize('variant', range(10))
def test_make_lotto_card_valid(variant):
    card = cards.make_lotto_card()

    assert len(card) == 3
    for column in zip(*card):
        assert cards.valid_column(column)


def test_new_lotto_card(lotto_card):
    assert len(lotto_card._rows) == 3
    assert len(lotto_card._numbers) == 15
    assert not lotto_card.all_marked


def test_number_in_card(lotto_card):
    assert 5 in lotto_card


def test_number_not_in_card(lotto_card):
    assert 100 not in lotto_card


def test_mark_number_in_card(lotto_card):
    lotto_card.mark_number(5)
    assert 5 not in lotto_card


def test_mark_number_not_in_card(lotto_card):
    with raises(ValueError):
        lotto_card.mark_number(100)


def test_all_marked_card(lotto_card):
    for number in list(lotto_card._numbers):
        lotto_card.mark_number(number)
    assert lotto_card.all_marked


def test_card_table_view(lotto_card):
    test_table = [
        ['  ', '17', '  ', '34', '45', '54', '62', '  ', '  '],
        [' 1', '14', '  ', '  ', '49', '56', '  ', '  ', '90'],
        [' 5', '  ', '27', '37', '  ', '  ', '63', '70', '  ']
    ]
    for card_row, test_row in zip(lotto_card.as_table, test_table):
        assert card_row == test_row


def test_marked_card_table_view(lotto_card):
    test_table = [
        ['  ', 'XX', '  ', 'XX', 'XX', 'XX', 'XX', '  ', '  '],
        ['XX', 'XX', '  ', '  ', 'XX', 'XX', '  ', '  ', 'XX'],
        ['XX', '  ', 'XX', 'XX', '  ', '  ', 'XX', 'XX', '  '],
    ]
    for number in list(lotto_card._numbers):
        lotto_card.mark_number(number)

    for card_row, test_row in zip(lotto_card.as_table, test_table):
        assert card_row == test_row
