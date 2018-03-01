import read

class Cars:
	def __init__(self, i):
		self.coords = {'i': 0, 'j': 0}
		self.busy = 0
		self.rides = []
		self.id = i


def manh(p1, p2):
	return abs(p1['i'] - p2['i']) + abs(p1['j'] - p2['j'])


def sort_by_earliest(dc, car, time):
	good = []
	for ride in dc.ridesLst:
		if ride.busy:
			continue
		if ride.e >= time + manh(car.coords, ride.start):
			good.append(ride)
	return good


def count_busy(car, ride, time):
	dist = manh(car.coords, ride.start)
	if time + dist < ride.e:
		dist += ride.e - time + dist
	return dist + manh(ride.start, ride.finish)


def get_can_finish(car, dc, time):
	good = []
	for ride in dc.ridesLst:
		if ride.busy:
			continue
		if time + manh(car.coords, ride.start) + manh(ride.start, ride.finish) <= ride.l:
			good.append(ride)
	return good


def sort_by_good_earliest(early, car):
	pass


files = ["a_example.in", "b_should_be_easy.in", "c_no_hurry.in", "d_metropolis.in", "e_high_bonus.in"]


for file in files:
	dc = read.getDataContainer('data/' + file)
	for i in range(dc.vehicles):
		dc.cars.append(Cars(i + 1))


	for time in range(dc.t):
		for car in dc.cars:
			if car.busy > 0:
				continue
			early = sort_by_earliest(dc, car, time)
			# print(early)
			if not len(early):
				early = get_can_finish(car, dc, time)
			closest = sorted(early, key=lambda x: manh(x.start, car.coords)) # get better
			# closest = sorted(early, key=lambda x: abs(manh(x.start, car.coords) + time - x.e)) # get better
			if not closest:
				break
			car.busy = count_busy(car, closest[0], time)
			closest[0].busy = True
			car.rides.append(closest[0].id)
			# print(car.id + ' ' + )

		for car in dc.cars:
			if car.busy > 0:
				car.busy -= 1

	with open("answer/" + file[:-2] + 'out', 'w') as f:
		for car in dc.cars:
			f.write(str(len(car.rides)) + ' ' + ' '.join([str(s) for s in car.rides]) + '\n')
	# for car in dc.cars:
	# 	print(str(car.id) + ' ' + ' '.join([str(s) for s in car.rides]))
