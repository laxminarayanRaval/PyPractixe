from typing import List


class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination


class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    def __repr__(self):
        """
        :return: String in format of DPT -> DST
        """
        stops = [self.segments[0].departure, self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)
        return " -> ".join(stops)

    @property
    def departure_point(self) -> str:
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, val):
        dest = self.segments[0].destination
        self.segments[0] = Segment(departure=val, destination=dest)

    @property
    def via_point(self) -> List:
        return self.segments

    @via_point.setter
    def via_point(self, dept):
        i = len(self.segments) - 1
        dest = self.segments[i].destination
        self.segments[i].destination = dept
        self.segments.append(Segment(departure=dept, destination=dest))


f = Flight([Segment('CHN', 'KLT')])
f.via_point = 'BMY'
f.via_point = 'DLH'
f.via_point = 'PTN'
# f.departure_point = 'MGL'
print(f)
