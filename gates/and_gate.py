from schedules.run_agenda import after_delay
from wires import wire
from gates import logic_actions


def and_gate(w1: wire.Wire, w2: wire.Wire, output: wire.Wire) -> str:
    def and_action():
        AND_GATE_DELAY = 3
        new_value = logic_actions.logical_and(w1.signal_value, w2.signal_value)
        after_delay(AND_GATE_DELAY, lambda: output.set_signal_value(new_value))

    w1.add_action(and_action)
    w2.add_action(and_action)
    print('ok')
