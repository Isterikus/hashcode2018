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



def can_in_time(cars, ride):
	good = []
	for car in cars:
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


def	mine_sort_cars_manh(ride, cars):
	min_car = cars[0]
	min_manh = manh(cars[0].coords, ride.start)
	for car in cars:
		mh = manh(car.coords, ride.start)
		if mh < min_manh:
			min_manh = mh
			min_car = car
	return min_car


def mine_sort_cars_abs(ride, cars, time):
	min_car = cars[0]
	min_manh = manh(cars[0].coords, ride.start)
	for car in cars:
		mh = abs(manh(ride.start, car.coords) - (ride.e - time))
		if mh < min_manh:
			min_manh = mh
			min_car = car
	return min_car


for file in files:
	dc = read.getDataContainer('data/' + file)
	for i in range(dc.vehicles):
		dc.cars.append(Cars(i + 1))

	# not_busy_c = dc.cars
	not_cycle = False
	ln = 0
	for time in range(dc.t):
		for car in dc.cars:
			if car.busy > 0:
				continue
			early = sort_by_earliest(dc, car, time)
			# print(early)

			if not early:
				early = get_can_finish(car, dc, time)
				closest = sorted(early, key=lambda x: (manh(x.start, x.finish), manh(x.start, car.coords)))
			else:
				closest = sorted(early, key=lambda x: abs(manh(x.start, car.coords) - (x.e - time)))
			if not early:
				break
			# closest = sorted(early, key=lambda x: manh(x.start, car.coords)) # get better
			car.busy = count_busy(car, closest[0], time)
			closest[0].busy = True
			car.rides.append(closest[0].id)
			# print(car.id + ' ' + )








		# if ln == dc.rides - 1:
		# 	break
		#
		# done_something = False
		#
		# # ride_id = 0
		# # if not not_cycle:
		# # 	while ride_id < len(dc.ridesLst):
		# # 		ride = dc.ridesLst[ride_id]
		# # 		if ride.busy:
		# # 			ride_id += 1
		# # 			continue
		# # 		can_in_time_c = can_in_time(dc.cars, ride)
		# # 		if not can_in_time_c:
		# # 			ride_id += 1
		# # 			continue
		# # 		# can_in_time_c = sorted(can_in_time_c, key=lambda x: abs(manh(ride.start, x.coords) - (ride.e - time))) # get better
		# # 		can_in_time_c = mine_sort_cars_abs(ride, can_in_time_c, time)  # get better
		# # 		can_in_time_c.busy = count_busy(can_in_time_c, ride, time)
		# # 		ride.busy = True
		# # 		can_in_time_c.rides.append(ride.id)
		# # 		del dc.ridesLst[ride_id]
		#
		# if not not_cycle:
		# 	for ride in dc.ridesLst:
		# 		if ride.busy:
		# 			continue
		# 		can_in_time_c = can_in_time(dc.cars, ride)
		# 		if not can_in_time_c:
		# 			continue
		# 		# can_in_time_c = sorted(can_in_time_c, key=lambda x: abs(manh(ride.start, x.coords) - (ride.e - time))) # get better
		# 		can_in_time_c = mine_sort_cars_abs(ride, can_in_time_c, time) # get better
		# 		can_in_time_c.busy = count_busy(can_in_time_c, ride, time)
		# 		ride.busy = True
		# 		can_in_time_c.rides.append(ride.id)
		# 		ln += 1
		#
		# if done_something == False:
		# 	not_cycle = True
		#
		# # ride_id = 0
		# # while ride_id < len(dc.ridesLst):
		# # 	ride = dc.ridesLst[ride_id]
		# # 	if ride.busy:
		# # 		ride_id += 1
		# # 		continue
		# # 	cars_not_b = car_not_busy(dc.cars)
		# # 	if not cars_not_b:
		# # 		break
		# # 	# car_time = sorted(cars_not_b, key=lambda x: manh(x.coords, ride.start))
		# # 	car_time = mine_sort_cars_manh(ride, cars_not_b)
		# # 	if time + manh(car_time.coords, ride.start) + manh(ride.start, ride.finish) <= ride.l:
		# # 		car_time.busy = count_busy(car_time, ride, time)
		# # 		ride.busy = True
		# # 		car_time.rides.append(ride.id)
		# # 	del dc.ridesLst[ride_id]
		#
		# for ride in dc.ridesLst:
		# 	if ride.busy:
		# 		continue
		# 	cars_not_b = car_not_busy(dc.cars)
		# 	if not cars_not_b:
		# 		break
		# 	# car_time = sorted(cars_not_b, key=lambda x: manh(x.coords, ride.start))
		# 	car_time = mine_sort_cars_manh(ride, cars_not_b)
		# 	if time + manh(car_time.coords, ride.start) + manh(ride.start, ride.finish) <= ride.l:
		# 		car_time.busy = count_busy(car_time, ride, time)
		# 		ride.busy = True
		# 		car_time.rides.append(ride.id)
		# 		ln += 1


		for car in dc.cars:
			if car.busy > 0:
				car.busy -= 1
		if time % 1000 == 0:
			print("Time " + str(time / dc.t))
		if file == "b_should_be_easy.in" and time / dc.t >= 0.97:
			break
		elif file == "c_no_hurry.in" and time / dc.t >= 0.996:
			break
		elif file == "d_metropolis.in" and time / dc.t >= 0.96:
			break
		elif file == "e_high_bonus.in" and time / dc.t >= 0.97:
			break

	print("File " + file + " ended")

	with open("answer3/" + file[:-2] + 'out', 'w') as f:
		for car in dc.cars:
			f.write(str(len(car.rides)) + ' ' + ' '.join([str(s) for s in car.rides]) + '\n')
	# for car in dc.cars:
	# 	print(str(car.id) + ' ' + ' '.join([str(s) for s in car.rides]))
