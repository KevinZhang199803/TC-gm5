def personalWeightedSum(path):
	result = 0
	for step in path["steps"].values():
		# print(step)
		method = step["type"]
		cost1 = step["duration"] * userInput["user-preference"]["time-sensitivity"]
		cost2 = step["distance"] * trafficInfo[method]["price"] * userInput["user-preference"]["price-sensitivity"]
		cost3 = trafficInfo[method]["traiff"]
		# print(method, "*****")
		if userInput["means-preference"][method] < 50:
			# print("DFFDFDFD")
			cost1, cost2 = 10000000000, 1000000000
		if userInput["means-preference"][method] > 50:
			cost1, cost2 = -1000, -1000
		result += cost1 + cost2 + cost3
	return result

# paths is provided by Gaode API
def optimalPath(paths):
	min = 1000000000000000000
	result = paths[0]
	for i in paths:
		# print(personalWeightedSum(paths[i]), paths[i])
		if personalWeightedSum(paths[i]) < min:
			# print(paths[i], "LLLLLLLLLLLLLLLL")
			min = personalWeightedSum(paths[i])
			result = paths[i]
	return result

# this function is to get data 
# provided by Gaode API
# (this function is very possible to be implemented with Javascript interface
# , and thus unnecessary)
def getPaths(origin, distination):
	result = {}
	return result

# return the optimal path 
# considering personal
# preferences
def firstPlan(origin, distination):
	# get paths from Gaode API
	paths = getPaths(origin, distination)
	result = optimalPath(paths)
	# print(result)
	return result

def secondPlan(origin, distination):
	# to be implemented!!!!!!!!!!!!!!!!!!!!!!!!
	# get the optimal path
	# choose four nodes on the optimal path
	# search specific locations near these nodes
	# (according to personal preferences)
	# recommend them to the user
	# (make money by this)
	return

def execute(origin, distination):
	print(firstPlan(origin, distination))
	if userInput["user-preference"]["time-sensitivity"] < 60:
		print(secondPlan(origin, distination))
	return

# each user can change parameters
# in this scope freely
userInput = {

	"user-preference": {
		"price-sensitivity": 50, 
		"time-sensitivity": 50,
		"less-walk": 0
	}, 

	"means-preference": {
		"Walk": 50, 
		"Metro": 50,
		"Bus": 50,
		"Bike": 50,
		"Drive": 50
	}
}

# price is the money
# cost per kilometer 
# in certain means
trafficInfo = {

	"Walk": {
		"traiff": 0, 
		"price": 0, 
		"speed": 1
	},

	"Metro": {
		"traiff": 3,
		"price": 0.1, 
		"speed": 50
	},

	"Bus": {
		"traiff": 2,
		"price": 0,
		"speed": 20,
	},

	"Bike": {
		"traiff": 0,
		"price": 0.01,
		"speed": 5,
	},

	"Drive": {
		"traiff": 100000,
		"price": 0,
		"speed": 20,
	}
}

paths = {
	0: { 
		"steps": {
			0: {"duration": 5, "type": "Walk", "distance": 13},
			1: {"duration": 5, "type": "Bus", "distance": 40}
		}, 
	},

	1: {
		"steps": {
			0: {"duration": 3, "type": "Metro", "distance": 40}, 
			1: {"duration": 3, "type": "Bus", "distance": 20}, 
			2: {"duration": 1.5, "type": "Bus", "distance": 10}, 
			3: {"duration": 3, "type": "Walk", "distance": 0.3}
		}
	},

	2: {
		"steps": {
			0: {"duration": 1, "type": "Walk", "distance": 0.1}, 
			1: {"duration": 3, "type": "Metro", "distance": 70}
		}
	}
}

print(optimalPath(paths))

# each user can change parameters
# in this scope freely
# this user hate to take the plane
# very much
# so we filter out all option
# containing a plane
userInput = {

	"user-preference": {
		"price-sensitivity": 50, 
		"time-sensitivity": 50,
		"less-walk": 0
	}, 

	"means-preference": {
		"Walk": 50, 
		"Metro": 50,
		"Bus": 50,
		"Railway": 50,
		# do not want to take a plane
		"Plane": 0
	}
}

# price is the money
# cost per kilometer 
# in certain means
trafficInfo = {

	"Walk": {
		"traiff": 0, 
		"price": 0, 
		"speed": 1
	},

	"Metro": {
		"traiff": 3,
		"price": 0.1, 
		"speed": 50
	},

	"Bus": {
		"traiff": 2,
		"price": 0,
		"speed": 20,
	},

	"Railway": {
		"traiff": 10,
		"price": 0.8,
		"speed": 20,
	},

	"Plane": {
		"traiff": 30,
		"price": 4,
		"speed": 20,
	},
}

paths = {
	0: { 
		"steps": {
			0: {"duration": 5, "type": "Walk", "distance": 13},
			1: {"duration": 5, "type": "Bus", "distance": 40},
			2: {"duration": 5, "type": "Railway", "distance": 2230},
		}, 
	},

	1: {
		"steps": {
			0: {"duration": 3, "type": "Metro", "distance": 40}, 
			1: {"duration": 2, "type": "Plane", "distance": 2230},
		}
	},

	# 2: {
	# 	"steps": {
	# 		0: {"duration": 1, "type": "Walk", "distance": 0.1}, 
	# 		1: {"duration": 3, "type": "Metro", "distance": 70}
	# 	}
	# }
}

print(optimalPath(paths))