from __future__ import print_function
import collections
import datetime

ImmutableThingTuple = collections.namedtuple("ImmutableThingTuple", "a b c d")


class MutableThing(object):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


class ImmutableThing(object):
    __slots__ = ['a', 'b', 'c', 'd']

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


print("Uncomment just 1 of these 4 loops below")
print("after the program pauses on input, check the process memory")

count = 1000000
print("Working with {:,} instances".format(count))
data = []

t0 = datetime.datetime.now()

# loop 1: Tuples
# print("tuple")
# for n in range(count):
#     data.append((1 + n, 2 + n, 3 + n, 4 + n))

# Loop 2: Named tuple
# print("named tuple")
# for n in range(count):
#     data.append(ImmutableThingTuple(1 + n, 2 + n, 3 + n, 4 + n))

# Loop 3: Standard mutable class
# print("standard class")
# for n in range(count):
#     data.append(MutableThing(1 + n, 2 + n, 3 + n, 4 + n))

# Loop 4: Slot based immutable class
print("slot based class")
for n in range(count):
    data.append(ImmutableThing(1 + n, 2 + n, 3 + n, 4 + n))

t1 = datetime.datetime.now()
dt = (t1 - t0).total_seconds()

print("finished, waiting...done in {} sec".format(dt))
