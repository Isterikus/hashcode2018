import DataContainer


def isFreeRides(dataContainer: DataContainer):
	for ride in dataContainer.ridesLst:
		if ride.busy: return True
	return False