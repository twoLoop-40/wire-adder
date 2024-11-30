from wires import wire
from gates.or_gate import (or_gate)
from adders.half_adder import half_adder

# 전가산기: 3개의 입력(a, b, c_in)을 받아 합(sum_out)과 자리 올림(c_out)을 생성
def full_adder(a: wire.Wire, b: wire.Wire, c_in: wire.Wire, sum_out: wire.Wire, c_out: wire.Wire):
    s = wire.Wire()   # 첫 번째 반가산기에서 합을 저장
    c1 = wire.Wire()  # 첫 번째 반가산기에서 자리 올림을 저장
    c2 = wire.Wire()  # 두 번째 반가산기에서 자리 올림을 저장
    half_adder(b, c_in, s, c1)  # 첫 번째 반가산기
    half_adder(a, s, sum_out, c2)  # 두 번째 반가산기
    or_gate(c1, c2, c_out)  # 두 자리 올림을 OR 연산하여 최종 자리 올림 생성
    print("ok")