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



def can_in_time(dc, ride):
	good = []
	for car in dc.cars:
		if car.busy:
			continue
		if ride.e >= time + manh(car.coords, ride.start):
			good.append(car)
	return good


def isFreeRides(dataContainer):
	for ride in dataContainer.ridesLst:
		if ride.busy: return True
	return False


files = ["a_example.in", "b_should_be_easy.in", "c_no_hurry.in", "d_metropolis.in", "e_high_bonus.in"]


def car_not_busy(cars):
	good = []
	for car in cars:
		if not car.busy:
			good.append(car)
	return good


for file in files:
	dc = read.getDataContainer('data/' + file)
	for i in range(dc.vehicles):
		dc.cars.append(Cars(i + 1))


	for time in range(dc.t):
		# for car in dc.cars:
		# 	if car.busy > 0:
		# 		continue
		# 	early = sort_by_earliest(dc, car, time)
		# 	# print(early)
		# 	if not len(early):
		# 		early = get_can_finish(car, dc, time)
		# 	# closest = sorted(early, key=lambda x: manh(x.start, car.coords)) # get better
		# 	closest = sorted(early, key=lambda x: abs(manh(x.start, car.coords) - (x.e - time))) # get better
		# 	if not closest:
		# 		break
		# 	car.busy = count_busy(car, closest[0], time)
		# 	closest[0].busy = True
		# 	car.rides.append(closest[0].id)
		# 	# print(car.id + ' ' + )

		for ride in dc.ridesLst:
			if ride.busy:
				continue
			can_in_time_c = can_in_time(dc, ride)
			if not can_in_time_c:
				continue
			can_in_time_c = sorted(can_in_time_c, key=lambda x: abs(manh(ride.start, x.coords) - (ride.e - time))) # get better
			can_in_time_c[0].busy = count_busy(can_in_time_c[0], ride, time)
			ride.busy = True
			can_in_time_c[0].rides.append(ride.id)

		for ride in dc.ridesLst:
			if ride.busy:
				continue
			cars_not_b = car_not_busy(dc.cars)
			if not cars_not_b:
				break
			car_time = sorted(cars_not_b, key=lambda x: manh(x.coords, ride.start))
			if time + manh(car_time[0].coords, ride.start) + manh(ride.start, ride.finish) <= ride.l:
				car_time[0].busy = count_busy(car_time[0], ride, time)
				ride.busy = True
				car_time[0].rides.append(ride.id)

		for car in dc.cars:
			if car.busy > 0:
				car.busy -= 1

	with open("answer/" + file[:-2] + 'out', 'w') as f:
		for car in dc.cars:
			f.write(str(len(car.rides)) + ' ' + ' '.join([str(s) for s in car.rides]) + '\n')
	# for car in dc.cars:
	# 	print(str(car.id) + ' ' + ' '.join([str(s) for s in car.rides]))
