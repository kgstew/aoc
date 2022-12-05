
def check_contained(range1, range2):
    first_set = set((range(int(range1[0]), int(range1[1]) + 1)))
    second_set = set(range(int(range2[0]), int(range2[1]) + 1))

    foo = first_set.intersection(second_set)

    return foo


with open("puzzle_4/puzzle_4_input.txt", 'r') as file:
    zones = [line.strip() for line in file.readlines()]

    def format_zones(zone):
        areas = zone.split(',')
        final = [area.split('-') for area in areas]
        return final

    # [((1,2),(1,4)), ((2,3),(2,6))]
    zones = map(format_zones, zones)

    contained = 0
    for zone in zones:
        area0 = zone[0]
        area1 = zone[1]
        if check_contained(area1, area0) or check_contained(area0, area1):
            contained = contained + 1

    print(contained)
