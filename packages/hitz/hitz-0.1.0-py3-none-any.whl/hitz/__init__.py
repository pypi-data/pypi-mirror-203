from coordz import Coord, TimeCoord, Quantity, g_C_water
from typing import Set, List


class Hit:
    def __init__(self, coord: Coord, t: float, q: float):
        self.coord = coord
        self.t = t
        self.q = q

    def time_residual(self, time_coord: TimeCoord, speed_of_light: Quantity = g_C_water):
        return self.t + time_coord.t - self.coord.distance(time_coord) / speed_of_light.convert(time_coord.space_unit, time_coord.time_unit).value

    def __str__(self):
        return 'Hit: ' + str(self.coord) + ', t: ' + str(self.t) + ', q: ' + str(self.q)

    def __repr__(self):
        return self.__str__()


class HitSet:
    def __init__(self,
                 eid: int,
                 speed_of_light: Quantity = g_C_water):
        self.eid = eid
        self.hits = set()
        self.speed_of_light = speed_of_light

    def __str__(self):
        return f"HitSet for EID={self.eid}, with {len(self.hits)} hits"

    def __repr__(self):
        return f"HitSet(eid={self.eid}, hits={self.hits}, speed_of_light={self.speed_of_light})"

    def add_hit(self, hit: Hit):
        self.hits.add(hit)

    def remove_hit(self, hit: Hit):
        self.hits.remove(hit)

    def update_hits(self, hits: List[Hit]):
        self.hits.update(hits)

    def get_hits(self) -> Set[Hit]:
        return self.hits

    def num_hits(self) -> int:
        return len(self.hits)

    def sort_hits(self, sort_key=None, reference=None):
        self.hits = sorted(self.hits, key=lambda hit: (sort_key or self.sort_key)(hit, reference or self.reference))