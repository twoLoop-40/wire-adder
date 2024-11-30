from adders.half_adder import half_adder
from schedules.run_agenda import propagate, probe
from wires import wire

input_1 = wire.Wire()
input_2 = wire.Wire()
sum_wire = wire.Wire()
carry = wire.Wire()

probe('sum', sum_wire)

probe('carry', carry)

half_adder(input_1, input_2, sum_wire, carry)

input_1.set_signal_value(1)

propagate()
