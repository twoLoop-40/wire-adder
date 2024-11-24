from wires import wire
from gates import logic_actions


def and_gate(w1: wire.Wire, w2: wire.Wire, output: wire.Wire) -> str:
    def and_action():
        new_value = logic_actions.logical_and(w1.signal_value, w2.signal_value)
        output.set_signal_value(new_value)

    w1.add_action(and_action)
    w2.add_action(and_action)
    return 'ok'
