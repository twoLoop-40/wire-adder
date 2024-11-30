from collections.abc import Callable

from schedules.agenda import Agenda
from wires import wire

agenda = Agenda()

def after_delay(delay: int, action: Callable):
    agenda.add_to_agenda(time=delay + agenda.current_time, action=action)


def propagate(count: int = 0) -> None:
    if agenda.is_empty_agenda():
        print('agenda is done')
    else:
        first_item = agenda.first_agenda_item()
        first_item()
        try:
            agenda.remove_first_agenda_item()
            # print(f'{count=}')
            return propagate(count + 1)
        except Exception as e:
            print(f"error: {e}")
            return 'done'


def probe(name: str, wire: wire.Wire):
    wire.add_action(
        lambda: print(f"{name} {agenda.current_time}, new value = {wire.signal_value}")
    )
