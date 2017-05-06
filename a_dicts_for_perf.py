from __future__ import print_function
import collections
import sys
import random
import datetime

DataPoint = collections.namedtuple("DataPoint", "id x y temp quality")


def main():
    # ##################
    print("Creating data...", end='')
    sys.stdout.flush()

    data_list = []
    random.seed(0)
    for d_id in range(500000):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        temp = random.randint(-10, 50)
        quality = random.random()
        data_list.append(DataPoint(d_id, x, y, temp, quality))

    print("done.")
    sys.stdout.flush()

    # ######################
    print('Simulating randomized data...', end='')
    sys.stdout.flush()

    data_list.sort(key=lambda d: d.quality)

    print("done")

    # Create a list of random IDs locate without duplication
    interesting_ids = list({random.randint(0, len(data_list)) for _ in range(0, 100)})
    print("Creating {} interesting IDs to seek.".format(len(interesting_ids)))

    # #####################
    print("Locating data in list...", end='')
    sys.stdout.flush()

    t0 = datetime.datetime.now()
    interesting_points = []
    for i in interesting_ids:
        pt = find_point_by_id_in_list(data_list, i)
        interesting_points.append(pt)

    t1 = datetime.datetime.now()
    dt_list = (t1 - t0).total_seconds()

    print("done.")
    sys.stdout.flush()

    print('DT: {} sec'.format(dt_list))
    print(interesting_points)

    # ######################
    t0 = datetime.datetime.now()
    print("Creating dictionnary...", end='')
    data_lookup = {d.id: d for d in data_list}

    print("done.")
    sys.stdout.flush()

    print("Locating data in dictionary...", end=' ')
    sys.stdout.flush()

    interesting_points = []
    for i in interesting_ids:
        item = data_lookup[i]
        interesting_points.append(item)

    t1 = datetime.datetime.now()

    dt_dict = (t1 - t0).total_seconds()

    print('done.')
    sys.stdout.flush()

    print('DT: {} sec'.format(dt_dict))
    print(interesting_points)
    print("Speedup from dict: {:,.0f}".format(round(dt_list / dt_dict)))


def find_point_by_id_in_list(data_list, id):
    for d in data_list:
        if d.id == id:
            return d
    return None


if __name__ == '__main__':
    main()
