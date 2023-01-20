import cv2
import numpy as np
import os

orb=cv2.ORB_create(nfeatures=10000)

#for making images container and their names
images=[] #stores images in it
classnames=[] #stores name or label
path = "DATA_SET_F"
mylist=os.listdir(path )#it gives the name of the file with jpg extension
l1={}
for i in mylist: #this is to convert names into label and map them to a dictionary
    a=""
    for j in range(0,len(i)):
        if 65<=ord(i.upper()[j])<=90:
            if i[j]!=".":
                a=a+i[j]
            else:
                break
            l1[i]=a[:len(a)-3]
for i in mylist:
    imgcur=cv2.imread(f'{path}/{i}',0)
    images.append(imgcur)
    classnames.append(l1[i])


#for making key and descriptor of the training data set
def finkeydes(images):
    deslist=[]
    for img in images:
        k,d=orb.detectAndCompute(img,None)
        deslist.append(d)
    return deslist#(list of descriptor present in images)

#to make a descriptor list of data sets
deslist=finkeydes(images)

print(len(deslist))
#to find descriptor of camera and also matches

def findid(img,deslist):
    k2,d2=orb.detectAndCompute(img,None)
    bf=cv2.BFMatcher()
    goodlist=[]
    for d in deslist:
        matches=bf.knnMatch(d,d2,k=2)
        good=[]
        for m,n in matches:
            if m.distance< 0.76*n.distance:
                good.append([m])
        goodlist.append(len(good))
    return goodlist


#to get the maximum match image
def findlabel(l):
    a=max(l)
    for i in range(0,len(l)):
        if a==l[i]:
            return classnames[i]

cap=cv2.VideoCapture(0)

d={"Clear":"Clear Weather ahead drive on usual speed limit","Cloudy":"Clouds ahead, may rain go slowly","Fog":"Fog ahead go slowly,very low visibility","Rain":"Weather is rainy ahead please pay caution","RainFog":"Low visibility and rain ahead pay extra caution"}
l=[]

while True:
    IMG=np.ones([80,900,3],np.int8)
    success, img2=cap.read()
    imgoriginal=img2.copy()
    img2=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    cv2.imshow("img2", imgoriginal)
    a=(findlabel(findid(img2, deslist)))
    b=str(d[a])
    cv2.putText(IMG,d["RainFog"] ,(10,40) , cv2.FONT_HERSHEY_COMPLEX,1,[0,0,255],1)
    #cv2.putText(IMG, b,(10,40) , cv2.FONT_HERSHEY_COMPLEX,1,[0,0,255],1)
    cv2.imshow("IMG",IMG)
    print(d["RainFog"])
    cv2.waitKey(1)
