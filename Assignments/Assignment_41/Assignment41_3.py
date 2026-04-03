import numpy as np
import math


def EulicedianDistance(P1,P2):
    distance=math.sqrt((P1["Study hours"]-P2["Study hours"])**2+(P1["Attendance"]-P2["Attendance"])**2)
    return distance

Data=[{"Study hours":2,"Attendance":60,"Result":"Fail"},
   {"Study hours":5,"Attendance":80,"Result":"Pass"},
   {"Study hours":6,"Attendance":85,"Result":"Pass"},
   {"Study hours":1,"Attendance":50,"Result":"Fail"}
   ]

print("Training Data :")

for i in Data:
    print(i)


print("Enter Study hours : ")
X=int(input())

print("Enter Attendance: ")
Y=int(input())

testdata={"Study hours":X,"Attendance":Y}
print(testdata)




for i in Data:
    i["Distance"]=EulicedianDistance(i,testdata)
print(Data)
   


sorteddistances=sorted(Data,key=lambda i:i["Distance"])
print("sorted distance : ",sorteddistances)

k=3

nearest=sorteddistances[0:k]
print("nearest : ",nearest)

#voting
votes={}
for i in nearest:
    print("result : ",i["Result"])
    print("distance : ",i["Distance"])
    labels=i["Result"]
    votes[labels]=votes.get(labels,0)+1

print("Votes : ")
print(votes)

predicted_class=max(votes,key=votes.get)
print("prediced result  : ",predicted_class)
    
    
    
    











