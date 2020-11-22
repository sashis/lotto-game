from typing import TypeVar, Callable, Type

from terminaltables import SingleTable

T = TypeVar('T')


def valid_input(prompt: str,
                value_type: Type[T],
                default_value: T,
                validate: Callable[[T], bool] = lambda v: True,
                interact_cb: Callable[[], str] = None) -> T:
    prompt_with_default = f'{prompt} [{default_value}]:'
    is_valid = False
    while not is_valid:
        print(prompt_with_default, end=' ')
        raw_value = (interact_cb or input)()
        try:
            value = value_type(raw_value) if raw_value else default_value
        except ValueError:
            continue
        is_valid = validate(value)
    return value


def make_printable_card(card_table, card_title):
    card = SingleTable(card_table, card_title)
    card.inner_row_border = True
    return card.table
