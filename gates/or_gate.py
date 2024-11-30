from schedules.run_agenda import after_delay
from wires import wire
from gates import logic_actions


# OR 게이트: 두 입력(w1, w2)의 신호 값을 OR 연산 후 출력(out)에 설정
def or_gate(w1: wire.Wire, w2: wire.Wire, output: wire.Wire):
    OR_GATE_DELAY = 5

    def or_action():
        new_value = logic_actions.logical_or(w1.signal_value, w2.signal_value)
        after_delay(OR_GATE_DELAY, lambda: output.set_signal_value(new_value))

    w1.add_action(or_action)
    w2.add_action(or_action)
    return 'or_gate ok'
