import logging


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        logging.basicConfig(
            level=logging.INFO,
            format="%(filename)s [LINE:%(lineno)-10d] # %(levelname)-8s [%(asctime)s] %(message)s"
        )

    def add(self, point: object):
        if not isinstance(point, Point):
            raise TypeError('Not Point instance')
        return Point(self.x + point.x, self.y + point.y)

    def __add__(self, other):
        return self.add(other)

    def __str__(self) -> str:
        return f'<Point {self.x}, {self.y}>'

    def self_print(self):
        print(self)


p = Point(2, 3)
p2 = Point(5, -7)

# 1:17:43 time in video
# inheriting

# p + p2

dummy = [1, 2, 3]

try:
    (p + dummy).self_print()
    pass
except TypeError:
    logging.exception("Exception")

(p + p2).self_print()
