# each user can change parameters
# in this scope freely
userInput = {

	"user-preference": {
		"price-sensitivity": 50, 
		"time-sensitivity": 50,
		"less-walk": 0
	}, 

	"means-preference": {
		"Walk": 100, 
		"Metro": 100,
		"Bus": 100,
		"Bike": 100,
		"Drive": 100
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

def personalWeightedSum(path):
	result = 0
	return result

# paths is provided by Gaode API
def optimalPath(paths):
	min = 1000000000000000000
	result = paths[0]
	for path in paths:
		if personalWeightedSum(path) < min:
			result = path
	return path