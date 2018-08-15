#!/usr/bin/python
#from sys import argv
import requests
import json
import os
import time
import sys
import random
import unittest

host = "http://39.104.109.10"
port = "6000"

class Testvse(unittest.TestCase):
	def get(self,url):
            resp = requests.get(url)
            if resp.content == "":
                return None,resp.status_code
            else:
                return resp,resp.status_code
	def post(self,url,body):
	    resp = requests.post(url,data=json.dumps(body))
	    if resp.content == "":
                return None,resp.status_code
	    else:
                return resp,resp.status_code
	def test_case01_ping(self):
#            print("case1_ping:")
            url = "%s:%s/demo/ping" % (host,port)
            resp,status=self.get(url)
            self.assertEqual(resp.text,u'{\n  "message": "OK"\n}')
            self.assertEqual(status,200)
	def test_case02_1vs1(self):
#	    print("case2_1vs1:")
            url = "%s:%s/demo/1vs1" %(host,port)
            body = {
	"face_id_1": "1",
	"image_url_1": "http://file.dg-atlas.com:3003/images/face/yangmi1.jpg",
	"face_id_2": "2",
	"image_url_2": "http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
}
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
#	def test_case06_new(self):
#            print("case6_new_file_h264:")
#            url = "%s:%s/%s/task/new" % (host,port,project#)
#            task_type = 'file'
#            uri_rtsp = 'file:///data/Videos/t1060.mp4'
#            task_id = 'h264_1'
#            body = new(task_id,task_type,uri_rtsp)
#            resp,status=self.post(url,body)
#            resp = json.loads(resp.content.decode('utf-8'))
#            message = resp['message']
#            self.assertEqual(message,"OK")
#            self.assertEqual(status,200)       


if __name__ == '__main__' :
    unittest.main()

