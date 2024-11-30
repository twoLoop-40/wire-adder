from wires import wire
from gates.or_gate import or_gate
from gates.and_gate import and_gate
from gates.inverter import inverter

# 반가산기: 입력(a, b)을 받아 합(s)과 자리 올림(c)을 생성
def half_adder(a: wire.Wire, b: wire.Wire, s: wire.Wire, c: wire.Wire):
    d = wire.Wire()  # OR 게이트 결과 저장
    e = wire.Wire()  # NOT 게이트 결과 저장
    or_gate(a, b, d)  # a OR b 결과 저장
    and_gate(a, b, c)  # a AND b 결과 저장 (자리 올림)
    inverter(c, e)  # 자리 올림(c)의 반전 결과 저장
    and_gate(d, e, s)  # 최종 합 계산

    print('half_adder ok')