import fileinput

class Business(object):
	def __init__(self, name):
		self.name = name
		self.nearby_businesses = {}

def find_reachable_businesses(starting_business, distance):
    results = []

    helper(results, starting_business, distance)

    # remove duplicate
    results = list(set(results))
    # remove starting_business
    results.remove(starting_business.name)

    return results

def helper(results, starting_business, distance):
    for biz, dis in starting_business.nearby_businesses.items():
        if dis <= distance:
            results.append(biz.name)
            helper(results, biz, distance - dis)

    return results


if __name__ == '__main__':
    # lines = [line.strip() for line in list(fileinput.input())]
    # lines = ['a', '1', 'a b 2', 'a c 4', 'b d 5']
    # lines = ['a', '2', 'a b 2', 'a c 4', 'b d 5']
    # lines = ['a', '3', 'a b 2', 'a c 4', 'b d 5']
    # lines = ['a', '4', 'a b 2', 'a c 4', 'b d 5']
    # lines = ['a', '7', 'a b 2', 'a c 4', 'b d 5']
    lines = ['a', '5', 'a b 2', 'a c 4', 'b d 5', 'b e 3', 'd h 2', 'c f 1', 'c g 2', 'h i 3']
    starting_business = lines[0]
    distance_input = int(lines[1])
    businesses = {}
    for line in lines[2:]:
        biz_1, biz_2, distance = line.split(' ')
        distance = int(distance)
        if biz_1 not in businesses:
            businesses[biz_1] = Business(biz_1)
        if biz_2 not in businesses:
            businesses[biz_2] = Business(biz_2)
        businesses[biz_1].nearby_businesses[businesses[biz_2]] = distance
        businesses[biz_2].nearby_businesses[businesses[biz_1]] = distance

    reachable_businesses = find_reachable_businesses(
        starting_business=businesses[starting_business],
        distance=distance_input,
    )
    output = sorted(reachable_businesses)
    print(output)