#encoding=utf-8
#!/usr/bin/python
#from sys import argv
import requests
import json
import os
import time
import sys
import random
import unittest

host = "http://localhost"
port = "6000"
def anBody(face_uri):
    an_body={"face": face_uri}
    return an_body
def otoBody(face1,face2):
    oto_body={"face_id_1":"1","image_url_1":face1,"face_id_2":"2","image_url_2":face2}
    return oto_body
class TestDemo(unittest.TestCase):
	def anBody(face_uri):
            an_body={"face": face_uri}
            return an_body
	def otoBody(id1,face1,id2,face2):
            oto_body={"face_id_1":id1,"image_url_1":face1,"face_id_2":id2,"image_url_2":face2}
            return otoBody
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
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
	def test_case03_an(self):
            url = "%s:%s/demo/an" %(host,port)
            face="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = anBody(face)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            sex = resp['sex']
            age = resp['age']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(sex,u'\u5973')
            self.assertEqual(age,22)
        def test_case04_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case05_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case06_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case07_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case08_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case09_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case10_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case11_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case12_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case13_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case14_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case15_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case16_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case17_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case18_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case19_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case20_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case21_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case22_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case23_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case24_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case25_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case26_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
        def test_case27_oto(self):
            url = "%s:%s/demo/1vs1" %(host,port)
            face1="http://file.dg-atlas.com:3003/images/face/yangmi1.jpg"
            face2="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = otoBody(face1,face2)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            similarity = resp['similarity']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(similarity,0.87044555)
	def test_case28_an(self):
            url = "%s:%s/demo/an" %(host,port)
            face="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = anBody(face)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            sex = resp['sex']
            age = resp['age']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(sex,u'\u5973')
            self.assertEqual(age,22)
	def test_case29_an(self):
            url = "%s:%s/demo/an" %(host,port)
            face="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = anBody(face)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            sex = resp['sex']
            age = resp['age']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(sex,u'\u5973')
            self.assertEqual(age,22)
	def test_case30_an(self):
            url = "%s:%s/demo/an" %(host,port)
            face="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = anBody(face)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            sex = resp['sex']
            age = resp['age']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(sex,u'\u5973')
            self.assertEqual(age,22)
	def test_case31_an(self):
            url = "%s:%s/demo/an" %(host,port)
            face="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = anBody(face)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            sex = resp['sex']
            age = resp['age']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(sex,u'\u5973')
            self.assertEqual(age,22)
	def test_case32_an(self):
            url = "%s:%s/demo/an" %(host,port)
            face="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = anBody(face)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            sex = resp['sex']
            age = resp['age']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(sex,u'\u5973')
            self.assertEqual(age,22)
        def test_case33_an(self):
            url = "%s:%s/demo/an" %(host,port)
            face="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = anBody(face)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            sex = resp['sex']
            age = resp['age']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(sex,u'\u5973')
            self.assertEqual(age,22)
	def test_case34_an(self):
            url = "%s:%s/demo/an" %(host,port)
            face="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = anBody(face)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            sex = resp['sex']
            age = resp['age']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(sex,u'\u5973')
            self.assertEqual(age,22)
        def test_case35_an(self):
            url = "%s:%s/demo/an" %(host,port)
            face="http://file.dg-atlas.com:3003/images/face/yangmi4.jpg"
            body = anBody(face)
            resp,status=self.post(url,body)
            resp = json.loads(resp.content.decode('utf-8'))
            rtn = resp['rtn']
            message = resp['message']
            sex = resp['sex']
            age = resp['age']
            self.assertEqual(rtn,200)
            self.assertEqual(message,"OK")
            self.assertEqual(sex,u'\u5973')
            self.assertEqual(age,22)
if __name__ == '__main__' :
    unittest.main()

