from __future__ import division                                                                         
#!/usr/bin/env python
import requests
import json
import os
import time
import sys
import threading
import logging
from sys import argv
# -*- coding: utf8 -*-
url='http://39.104.109.10:6000/demo/1vs1'
url='http://localhost:6001/rec/image'
counts = [0,0,0,0,0,0,0,0,0,0]
costs = [0,0,0,0,0,0,0,0,0,0]


def post(threadID):
	count = 0
	cost = 0
	while True:
		#data =  {"Face_id_1":"face1","Image_url_1":"http://file.dg-atlas.com:3003/images/face/yangmi2.jpg","Face_id_2":"face2","Image_url_2":"http://file.dg-atlas.com:3003/images/face/yangmi6.jpg"} 
		data = {
	"face_id_1": "1",
	"image_url_1": "http://file.dg-atlas.com:3003/images/face/rank_face/3/3-1.jpg",
	"face_id_2": "2",
	"image_url_2": "http://file.dg-atlas.com:3003/images/face/rank_face/3/3-2.jpg"
  "Context": {
  	"SessionId":"all-single",
	"Type": 2,
    "Functions": [200, 201, 202, 203, 204, 205]
  },
  "Image":
    {
    	"Data": {
        	"URI": "file:///images/1.jpg"
    	}
    }
}
		begin = time.time() * 1000
		r = requests.post(url=url,data=json.dumps(data))
		end = time.time() * 1000
		cost_this = end - begin
		count += 1
		cost += cost_this
		costs [threadID] = cost
		counts [threadID] = count
#		os.system('clear')
#		print "threadName	count	avg_cost"
#		for i in range(0,10) :
#			try :
#				print "thread-" + str(i) + "	" + str(counts[i]) + "	" + str(costs[i] / counts[i]) + " ms"
#			except :
#				print "thread-" + str(i) + "	" + str(counts[i]) + "	" + "0 ms" 
		os.system('clear')
		print "threadName	count	avg_cost"
		for i in range(0,10) :
			try :
				print "thread-" + str(i) + "	" + str(counts[i]) + "	" + str(costs[i] / counts[i]) + " ms"
			except :
				print "thread-" + str(i) + "	" + str(counts[i]) + "	" + "0 ms" 
		#print threadName + "  : %d"%count
class myThread(threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
	def run(self):
#		print "Starting " + self.name
		self.result = post(self.threadID)
#		print "Exiting "+ self.name
threads = []
for i in range (0,10):
		print "Starting " + self.name
		self.result = post(self.threadID)
		print "Exiting "+ self.name
threads = []
for i in range (0,N):
	thread = myThread(i,"thread-%d"%i)
	threads.append(thread)
for t in threads:
	t.start()
for t in threads:
	t.join()
print("complete")
