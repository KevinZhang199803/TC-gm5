from django.db import transaction, IntegrityError
from django.http import JsonResponse, Http404,HttpResponse
from django.db.models import Q
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
import json
from .serializers import *
from .models import *
from aip import AipNlp

import datetime
APP_ID = '10437334'
API_KEY = 'wnbWILkse5iQBMlfc0S9xrFx'
SECRET_KEY = '7dwOvserOKXL2560DDusDsFg5VXpu9t9'

def ParsedTimePoint(timeStr, currentTime):
	timeList = timeStr.replace("时", ":").replace("点", ":").replace("分", "").replace("一刻", "15").replace("三刻", "45").replace("上午", "").replace("早上", "").replace("下午", "12+").replace("晚上", "12+").split(":")
	intHour = eval(timeList[0])
	try:
		intMinute = eval(timeList[1])
	except:
		intMinute = 0 
	# print("this is list", strHour, strMinute)
	a = currentTime.replace(hour = intHour, minute = intMinute)
	timePointObj = {
		"startTime" : a, 
		"endTime" : a
		}
	return timePointObj

def String2TimeObj(timeStr):
	currentTime = datetime.datetime.now().replace(second = 0, microsecond = 0)
	timeIntervalDict = {
		"上午":{
			"startTime" : currentTime, 
			"endTime" : currentTime.replace(hour = 10, minute = 30)
		}, 
		"中午":{
			"startTime" : currentTime.replace(hour = 10, minute = 30), 
			"endTime" : currentTime.replace(hour = 13, minute = 30)
		}, 
		"下午":{
			"startTime" : currentTime.replace(hour = 13, minute = 30), 
			"endTime" : currentTime.replace(hour = 17, minute = 00)
		}, 
		"晚上":{
			"startTime" : currentTime.replace(hour = 17, minute = 00), 
			"endTime" : currentTime.replace(hour = 22, minute = 00)
		}, 
		}
	if timeStr in timeIntervalDict:
		return timeIntervalDict[timeStr]
	else:
		return ParsedTimePoint(timeStr, currentTime)

class QuizListViewForExaminee(viewsets.ReadOnlyModelViewSet):
	queryset = Quiz.objects.all()
	serializer_class = QuizSerializerForExaminee

def TakeQuizView(request, quiz_id):
	q = Quiz.objects.get(pk=quiz_id)
	ps = q.getProblemSet()
	ser = ProblemSerializerForExaminee(ps, many=True)
	return JsonResponse(ser.data, safe=False)

def QuizHandinView(request):
	# import json
	if request.method == 'POST':
		# ju=json.loads(request.body)
		body1=json.loads(str(request.body, encoding = "utf-8"))
		client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
		data = client.lexer(body1['content'])
		classified={'verb':[],'noun':[], 'time':[]}
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
						classified={'verb':[],'noun':[], 'time':[]}
					# print(classified)
			if i==len(listAll)-1:
				if (listAll[i]['pos']=='v')  and (listAll[i]['pos'] not in filter):
					classified['verb'].append(listAll[i])
					GeneralList.append(classified)
					classified={'verb':[],'noun':[], 'time':[]}
			if i!=len(listAll)-1:
				if (listAll[i]['pos'] in locationList) or (listAll[i]['ne'] in locationList):
					classified['noun'].append(listAll[i])
					if (listAll[i+1]['pos'] not in locationList) and  (listAll[i+1]['ne'] not in locationList):
						GeneralList.append(classified)
						classified={'verb':[],'noun':[], 'time':[]}
			if i==len(listAll)-1:
				if (listAll[i]['pos'] in locationList) or (listAll[i]['ne'] in locationList):
					classified['noun'].append(listAll[i])
					GeneralList.append(classified)
					classified={'verb':[],'noun':[], 'time':[]}
			i=i+1
		# print(GeneralList)
		def getlocation(str1):
			pass
		# 	if (str1=='吃'):
		# 		request()


		def OutputNaive(data, GeneralList):
			start, end = 0, 0
			a = 0
			naiveList = []
			while a < len(GeneralList):
				naiveList.append( [ [], [], [] ] )
				print('Part', a + 1)
				start = end
				endList = []
				v=0
				while v < len(GeneralList[a]['verb']):
					naiveList[a][0].append(GeneralList[a]['verb'][v]['item'])
					endList.append(GeneralList[a]['verb'][v]['byte_offset'])
					v = v + 1 
				n = 0;
				if len(GeneralList[a]['noun']) == 0:
					end = 100
				while n < len(GeneralList[a]['noun']):
					naiveList[a][1].append(GeneralList[a]['noun'][n]['item'])
					endList.append(GeneralList[a]['noun'][n]['byte_offset'])
					n = n + 1
				c = 0
				end = max(endList)
				while c < len(data['items']):
					if start <= data['items'][c]['byte_offset'] <= end:
						if data['items'][c]['ne'] == 'TIME' or (data['items'][c]['pos'] == "m" and '点' in data['items'][c]['basic_words']):
							naiveList[a][2].append(String2TimeObj(data['items'][c]['item']))
					c+=1
				a=a+1
			return naiveList




		outputList = OutputNaive(data, GeneralList)
		# print(outputList)
		def p2j(i):

			return json.dumps(i.isoformat())

		def extractAllowedTime(action):
			try:
				return [action[2][0]["startTime"], action[2][0]["endTime"]]
			except:
				return [datetime.datetime.now() for i in range(1)]

		def ParseAction(action):
			actionObj = {
				"type" : "togo" if (action[0][0] == "去") or (action[0][0] == "到") else "todo",
				"description" : action[0]+action[1],
				"allowedTime" : [p2j(i) for i in extractAllowedTime(action)]
			}
			return actionObj



		def Naive2JSON(naiveList):
			node = {"goals": [ParseAction(action) for action in naiveList]}
			return node

		print(Naive2JSON(outputList))
		return HttpResponse(Naive2JSON(outputList))