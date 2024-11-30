from collections.abc import Callable
import queue


class TimeSegment:
    def __init__(self, time: int):
        self.time = time
        self.segment_queue = queue.Queue()

    def add_action_to_queue(self, action: Callable):
        self.segment_queue.put(action)


class Segments:
    def __init__(self):
        self.segments: list[TimeSegment] = list()

    def is_null(self) -> bool:
        return self.segments is None or len(self.segments) == 0

    def first_segment(self):
        if self.is_null():
            raise Exception('Segment is null')

        return self.segments[0]

    def rest_segments(self):
        if self.is_null():
            return []
        return self.segments[1:]


def belongs_before(time: int, segs: Segments) -> bool:
    return segs.is_null() or time < segs.first_segment().time


def add_to_segments(time: int, action: Callable) -> Callable[[Segments], None]:
    def add_to(segments: Segments):
        if segments.is_null():
            raise ValueError('Segment is empty')

        first_seg = segments.first_segment()
        if time == first_seg.time:
            first_seg.segment_queue.put(action)
            return None

        segments.segments = segments.rest_segments()
        if belongs_before(time, segments):
            ts = TimeSegment(time)
            ts.add_action_to_queue(action)
            rest_segs = segments.rest_segments()
            rest_segs.insert(0, ts)
        else:
            add_to(segments)

    return add_to


class Agenda:
    def __init__(self):
        self.current_time = 0
        segs = Segments()
        self.segments: Segments = segs

    def set_current_time(self, current_time: int) -> None:
        self.current_time = current_time

    def set_segments(self, segments: Segments) -> None:
        self.segments = segments

    def remove_first_agenda_item(self) -> None:
        first_seg_q = self.segments.first_segment().segment_queue
        print(f"q_size: {first_seg_q.qsize()}")
        if first_seg_q.empty():
            self.segments.segments = self.segments.rest_segments()

    def is_empty_agenda(self) -> bool:
        return self.segments.is_null()

    def first_segment(self):
        return self.segments.first_segment()

    # 첫번째 seg에서 첫번째 작업을 뽑고 current_time 을 첫번째 seg 타임으로 맞춤
    def first_agenda_item(self):
        if self.is_empty_agenda():
            raise ValueError('Agenda is empty')

        first_seg = self.first_segment()
        print(f"seg_time: {first_seg.time}")
        self.set_current_time(first_seg.time)
        return first_seg.segment_queue.get()

    def add_to_agenda(self, time: int, action: Callable) -> None:

        segs = self.segments
        if belongs_before(time, segs):
            ts = TimeSegment(time)
            ts.add_action_to_queue(action)
            segs.segments.insert(0, ts)
            self.set_segments(segs)

        else:
            add_to = add_to_segments(time, action)
            add_to(segs)
