# 논리 NOT 게이트: 입력이 0이면 1, 1이면 0을 반환
def logical_not(s: int) -> int:
    match s:
        case 0:
            return 1
        case 1:
            return 0
        case _:
            raise ValueError(f'{s}, Invalid signal')

# 논리 AND 게이트: 두 입력이 모두 1일 때만 1을 반환
def logical_and(s: int, t: int) -> int:
    if s not in {0, 1} or t not in {0, 1}:
        raise ValueError(f'{s}, {t}, Invalid signal')
    match s, t:
        case 1, 1:
            return 1
        case _:
            return 0

# 논리 OR 게이트: 두 입력 중 하나라도 1이면 1을 반환
def logical_or(s: int, t: int) -> int:
    if s not in {0, 1} or t not in {0, 1}:
        raise ValueError(f'{s}, {t}, Invalid signal')
    match s, t:
        case 0, 0:
            return 0
        case _:
            return 1