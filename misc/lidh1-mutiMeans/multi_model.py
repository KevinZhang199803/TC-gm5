# *************** compare all combinations of traffic methods
# *************** and return the one with the least 
# *************** weighted sum (with brute force)

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
		"price": 0.4, 
		"speed": 50
	},

	"Bus": {
		"traiff": 2,
		"price": 0,
		"speed": 20,
	},

	"Bike": {
		"traiff": 0,
		"price": 0.1,
		"speed": 5,
	},

	"Drive": {
		"traiff": 1000000,
		"price": 0,
		"speed": 20,
	}
}

Graph = {
	1: { 1: 0, 2: 1, 3: 12 },
	2: { 2: 0, 3: 9, 4: 3 },
	3: { 3: 0, 5: 5 },
	4: { 3: 4, 4: 0, 5: 13, 6: 15 },
	5: { 5: 0, 6: 4 },
	6: { 6: 0 } 
}

def dijkstra(G, v0, INF = 9999999999999999999):
	book = set()
	minv = v0
	dis = dict((k,INF) for k in G.keys())
	dis[v0] = 0
	optimalPath = {a: [v0] for a in G.keys()}
	while len(book) < len(G):
		book.add(minv)
		for w in G[minv]:
			if dis[minv] + G[minv][w] < dis[w]:
				dis[w] = dis[minv] + G[minv][w]
				optimalPath[w] = optimalPath[minv][:]
				optimalPath[w].append(w)
		new = INF
		for v in dis.keys():
			if v in book:
				continue
			if dis[v] < new:
				new = dis[v]
				minv = v
	return (optimalPath, dis)

# get personal cost of 
# each travelling method
# (weight of each edge in G)
# write all changes into trafficInfo 
# or userInput
def getPersonalCosts(weather = "sunny"):
	global userInput, trafficInfo
	if weather == "rainy":
		userInput["means-preference"]["Walk"] -= 5
	return

def getGraph(map):
	global userInput, trafficInfo
	result = {}
	# search subway/ bus stops in a range 
	# centered with origin
	# (or: find the airport/ railway station in the city of origin)
	# search subway/ bus stops in a range 
	# centered with terminal 
	# (or: find the airport/ railway station in the city of origin)
	return result

# get the optimal method
# from origin to destination
# , and output the route and required time
def firstPlan(origin):
	G = getGraph(userInput, weather, trafficInfo)
	print(dijkstra(G, origin))
	return

# get the path plan 
# in the second step
# and output it
def secondPlan(origin, userInput, weather, trafficInfo):
	result = {}
	# search shops on the planned route
	# recommend them to the user
	return result

# correction and retry
def correct():
	return

def execute():
	while not satisfied:
		# origin = getOrigin()
		firstPlan(origin)
		secondPlan(origin)
		correct()
		print("satisfied")
		# satisfied = getSatisfied()
	return

# dis = dijkstra(G, v0 = 1)
# print(dis)