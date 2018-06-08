#encoding=utf-8
#!/usr/bin/env python
import requests
import json
import os
import time
import sys
import random
#from sys import argv

url = 'http://39.104.109.10:6000'
inte_ping = url + '/demo/ping'
inte_an = url + '/demo/an'
inte_1vs1 = url + '/demo/1vs1'

def one(face_url,e_status):
    begin = time.time()*1000
    inte = inte_an
    data = {"Face":face_url}
    try :
        result = requests.post(url=inte,data=json.dumps(data))
        end = time.time()*1000
        cost = end - begin
        ret = json.loads(result.content)
        rtn = ret['rtn']
        message = ret['message']
	sex = ret['sex']
	if sex == "男":
            sex = "man"
	else: 
	    sex = "women"
	age = ret['age']
	
        if int(rtn) == int(e_status) :
            return "PASS  (status:%s = expect status, message: %s)    \nface:%s  age:%s  sex:%s\n%.2f ms\n"%(rtn,message,face_url,age,sex,cost)
        else :
            return "FAILED  (status:%s != expect status:%s,message: %s)   %.2fms\n"%(rtn,e_status,message,cost)
    except :
        return "connection refused\n"
def oto(face_url1,face_url2,e_status):
    begin = time.time()*1000
    inte = inte_1vs1
    data = { "Face_id_1":"face1","Image_url_1":face_url1,"Face_id_2":"face2","Image_url_2":face_url2
}
    try :
        result = requests.post(url=inte,data=json.dumps(data))
        end = time.time()*1000
        cost = end - begin
        ret = json.loads(result.content)
        rtn = ret['rtn']
        message = ret['message']
        similarity = ret['similarity']

        if int(rtn) == int(e_status) :
            return "PASS  (status:%s = expect status, message: %s)    \nsimilarity: %s\n%.2f ms\n"%(rtn,message,similarity,cost)
        else :
            return "FAILED  (status:%s != expect status:%s,message: %s)  \n%.2fms\n"%(rtn,e_status,message,cost)
    except :
        return "connection refused\n"

#with open('/root/work/testLog','w+r') as f:
#	f.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
res = one("http://file.dg-atlas.com:3003/images/face/2.jpg",200)
print res
#with open('/root/work/testLog','a') as f:
#        f.write(res)
res = one("http://file.dg-atlas.com:3003/images/face/yangmi1.jpg",200)
print res
#with open('/root/work/testLog','a') as f:
#        f.write(res)
res = one("http://file.dg-atlas.com:3003/images/face/yangmi1.jpg",200)
print res
#with open('/root/work/testLog','a') as f:
#        f.write(res)
res = one("http://file.dg-atlas.com:3003/images/face/yangmi2.jpg",200)
print res
res = one("http://file.dg-atlas.com:3003/images/face/none.jpg",400)
print res
#res = one("http://file.dg-atlas.com:3003/images/face/none.jpg",200)
#print res
#with open('/root/work/testLog','a') as f:
#        f.write(res)
res = oto("http://file.dg-atlas.com:3003/images/face/yangmi2.jpg","http://file.dg-atlas.com:3003/images/face/yangmi4.jpg",200)
print res
#with open('/root/work/testLog','a') as f:
#        f.write(res)
res = oto("http://file.dg-atlas.com:3003/images/face/yangmi5.jpg","http://file.dg-atlas.com:3003/images/face/yangmi4.jpg",200)
print res
res = oto("http://file.dg-atlas.com:3003/images/face/none.jpg","http://file.dg-atlas.com:3003/images/face/yangmi4.jpg",400)
print res
#res = oto("http://file.dg-atlas.com:3003/images/face/none.jpg","http://file.dg-atlas.com:3003/images/face/yangmi4.jpg",200)
#print res
