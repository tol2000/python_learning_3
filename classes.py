class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, point: str):
        if not isinstance(point, Point):
            raise TypeError('Not Point instance')
        return Point(self.x + point.x, self.y + point.y)

    def __str__(self):
        return f'<Point {self.x}, {self.y}>'


p = Point(2, 3)
p2 = Point(5, -7)

# 1:12 time in video

# p + p2

l = [1, 2, 3]

print(p.add(l))
print(p.add(p2))
