# encoding: utf-8  
from aip import AipNlp
import json
APP_ID = '10437334'
API_KEY = 'wnbWILkse5iQBMlfc0S9xrFx'
SECRET_KEY = '7dwOvserOKXL2560DDusDsFg5VXpu9t9'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
data = client.lexer('6点去食堂吃早饭8点去教室上课12点去长泰看电影14点去公交车站坐公交车')
# with open("./data.json",'r') as load_f:
	# data = json.load(load_f)
print(data)
classified={'verb':[],'noun':[]}
listAll=[]
locationList=['nz','n','nw','nt','nr','LOC','ORG']
j=0
while j<len(data['items']):
	if data['items'][j]['pos']=='v':
		listAll.append(data['items'][j])
	if (data['items'][j]['pos']in locationList ) or (data['items'][j]['ne']in locationList ):
		listAll.append(data['items'][j])
	if data['items'][j]['pos']=='TIME':
		pass
	j=j+1

filter=['想','想要','要','还要']

# criticalVerbs = ["去看", "看", "去", "回", "到", "唱", "参加", "开会", "上班", "上学", "上课", "买", "喝", "吃", "玩"]
i=0;
GeneralList=[]
while i<len(listAll):
	# if (i+1)!=len(listAll):
	# print(listAll[i]['item'])
	if i!=len(listAll)-1:

		if (listAll[i]['pos']=='v') and (listAll[i+1]['pos']!='v') and (listAll[i]['item'] not in filter):
			classified['verb'].append(listAll[i])
		if (listAll[i]['pos']=='v') and (listAll[i+1]['pos']=='v') and (listAll[i]['item'] not in filter):
			if (listAll[i]['item']=='去'):
				pass
			else:
				classified['verb'].append(listAll[i])
				GeneralList.append(classified)
				classified={'verb':[],'noun':[]}
			# print(classified)
	if i==len(listAll)-1:
		if (listAll[i]['pos']=='v')  and (listAll[i]['pos'] not in filter):
			classified['verb'].append(listAll[i])
			GeneralList.append(classified)
			classified={'verb':[],'noun':[]}
	if i!=len(listAll)-1:
		if (listAll[i]['pos'] in locationList) or (listAll[i]['ne'] in locationList):
			classified['noun'].append(listAll[i])
			if (listAll[i+1]['pos'] not in locationList) and  (listAll[i+1]['ne'] not in locationList):
				GeneralList.append(classified)
				classified={'verb':[],'noun':[]}
	if i==len(listAll)-1:
		if (listAll[i]['pos'] in locationList) or (listAll[i]['ne'] in locationList):
			classified['noun'].append(listAll[i])
			GeneralList.append(classified)
			classified={'verb':[],'noun':[]}
	i=i+1
# print(GeneralList)
def getlocation(str1):
	pass
# 	if (str1=='吃'):
# 		request()
a=0
while a<len(GeneralList):
	print('Part',a+1)
	v=0;

	while v<len(GeneralList[a]['verb']):
		print('动词',GeneralList[a]['verb'][v]['item'])
		getlocation(GeneralList[a]['verb'][v]['item'])
		v=v+1
	n=0;
	while n<len(GeneralList[a]['noun']):
		print('名词',GeneralList[a]['noun'][n]['item'])
		n=n+1
	a=a+1

