import numpy as np
import math


def EulicedianDistance(P1,P2):
    distance=math.sqrt((P1["X"]-P2["X"])**2+(P1["Y"]-P2["Y"])**2)
    return distance

Data=[{"Point":"A","X":1,"Y":2,"label":"RED"},
   {"Point":"B","X":2,"Y":3,"label":"RED"},
   {"Point":"C","X":3,"Y":1,"label":"BLUE"},
   {"Point":"D","X":6,"Y":5,"label":"BLUE"}
   ]

print("Training Data :")

for i in Data:
    print(i)


print("Enter the X cordinate : ")
X=int(input())

print("Enter the Y cordinate : ")
Y=int(input())

testdata={"X":X,"Y":Y}
print(testdata)




for i in Data:
    i["Distance"]=EulicedianDistance(i,testdata)
print(Data)
   


sorteddistances=sorted(Data,key=lambda i:i["Distance"])
print("sorted distance : ",sorteddistances)

k=3

nearest=sorteddistances[0:3]
print("nearest : ",nearest)

#voting
votes={}
for i in nearest:
    print("label : ",i["label"])
    print("distance : ",i["Distance"])
    labels=i["label"]
    votes[labels]=votes.get(labels,0)+1

print("Votes : ")
print(votes)

predicted_class=max(votes,key=votes.get)
print("prediced class of (",X,",",Y,") : ",predicted_class)
    
    
    
    











