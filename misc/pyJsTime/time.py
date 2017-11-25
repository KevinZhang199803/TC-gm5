import json
from datetime import datetime
def j2p(j):
	return datetime.strptime(j, '%Y-%m-%dT%H:%M:%S.%fZ')

def p2j(i):
	return json.dumps(i.isoformat())

print(j2p('2011-05-25T20:34:05.787Z'))


print(p2j(datetime(2015, 4, 19, 12, 20)))


