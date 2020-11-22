import math

class Vector:

    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __add__(self, other):
        return Vector({self.x + other.x}, {self.y + other.y}, {self.z + other.z})

    def __sub__(self, other):
        return Vector({self.x - other.x}, {self.y - other.y}, {self.z - other.z})

    def __and__(self, other):
        return Vector({self.y*other.z - other.y*self.z}, {other.x*self.z - self.x*other.z}, {self.x*other.y - self.y*other.x})

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
'''
x = Vector('1,2,3')
y = Vector('2,3,4')
print(x+y, x-y, x&y, sep = '\n')

N = int(input())
s = 1
vectors = []
while s <= N:
    vectors.append(Vector(input()))
    s += 1

dist = 0
most_remote_vector = 0
for i in range(N):
    if vectors[i].distance() > dist:
        dist = vectors[i].distance()
        most_remote_vector = i


print(vectors[most_remote_vector])
'''
