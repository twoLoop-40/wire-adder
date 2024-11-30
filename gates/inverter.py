from schedules.run_agenda import after_delay
from wires import wire
from gates import logic_actions


# NOT 게이트: 입력(input_sig)의 신호 값을 NOT 연산 후 출력(output)에 설정
def inverter(input_sig: wire.Wire, output: wire.Wire) -> str:
    INVERTER_DELAY = 2

    def inverter_action():
        new_value = logic_actions.logical_not(input_sig.signal_value)
        after_delay(INVERTER_DELAY, lambda: output.set_signal_value(new_value))

    input_sig.add_action(inverter_action)

    return 'ok'
