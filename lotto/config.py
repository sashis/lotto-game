from typing import TypeVar, Callable, Type

T = TypeVar('T')


def valid_input(prompt: str,
                value_type: Type[T],
                default_value: T,
                validate: Callable[[T], bool] = lambda v: True) -> T:
    prompt_with_default = f'{prompt} [{default_value}]: '
    is_valid = False
    while not is_valid:
        raw_value = input(prompt_with_default)
        try:
            value = value_type(raw_value) if raw_value else default_value
        except ValueError:
            continue
        is_valid = validate(value)
    return value


def choose_players():
    count = valid_input(
        prompt='Сколько будет игроков (2-5)',
        value_type=int,
        default_value=2,
        validate=lambda v: 2 <= v <= 5
    )
    return [configure_player(i + 1) for i in range(count)]


def configure_player(num):
    print(f'Параметры игрока #{num}')
    type_ = choose_player_type()
    name = choose_player_name(f'Игрок{num}')
    return type_, name


def choose_player_type():
    types = ['человек', 'компьютер']
    type_ = valid_input(
        prompt=f'Тип игрока ({"/".join(types)})',
        value_type=int,
        default_value=1,
        validate=lambda v: v in (1, 2)
    )
    return types[type_ - 1]


def choose_player_name(default):
    return valid_input(
        prompt='Имя игрока',
        value_type=str,
        default_value=default
    )