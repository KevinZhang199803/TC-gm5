# class user_input:
# 	def __init__():
# 		return

userInput = {
	"user-preference": {
		"price-sensitivity": 50, 
		"time-sensitivity": 50,
		"less-walk": 0
	}, 

	"means-preference": {
		"Walk": 0, 
		"Metro": 0,
		"Bus": 0,
		"Bike": 0,
		"Drive": 0
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

G = {
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

# get personal costs of 
# travelling methods
# (weight of each edge in G)
def getCosts(userInput, weather, trafficInfo):
	result = {}
	return result

def getGraph(userInput, weather, trafficInfo):
	result = {}
	return result

# return the optimal method
# from origin to destination
def firstPlan(userInput, weather, trafficInfo):
	result = {}
	return result

# return the path plan 
# in the second step
def secondPlan(userInput, weather, trafficInfo):
	result = {}
	return result

# correction and retry
def correct():
	return

def execute():
	return

# dis = dijkstra(G, v0 = 1)
# print(dis)