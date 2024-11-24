def logical_not(s: int) -> int:
    match s:
        case 0:
            return 1
        case 1:
            return 0
        case _:
            raise ValueError(f'{s}, Invalid signal')

def logical_and(s: int, t: int) -> int:
    if s not in {0, 1} or t not in {0, 1}:
        raise ValueError(f'{s}, {t}, Invalid signal')
    match s, t:
        case 1, 1:
            return 1
        case _:
            return 0

def logical_or(s: int, t: int) -> int:
    pass