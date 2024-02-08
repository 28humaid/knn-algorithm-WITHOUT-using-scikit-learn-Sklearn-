import random #to generate random numbers
import matplotlib.pyplot as plt #to draw the scatter plot
import math #to calculate euclidean distance

#creating a randomly generated dataset
datasetDict={}
for i,j in zip(range(100),range(200)):
  toTuple=(random.randrange(0,i+1),random.randrange(0,j+1))
  datasetDict[toTuple]=random.randrange(0,2)

print(datasetDict)

count0=0
count1=0

for i in datasetDict:
  if datasetDict[i]==0:
    count0+=1
  elif datasetDict[i]==1:
    count1+=1
print('count of 0 : ',count0)
print('count of 1 : ',count1)

#plot the points on graph for visualization
x_0=[]
y_0=[]
x_1=[]
y_1=[]
for i in datasetDict:
  if datasetDict[i] == 0:
    x_0.append(i[0])
    y_0.append(i[1])
  elif datasetDict[i] == 1:
    x_1.append(i[0])
    y_1.append(i[1])
plt.scatter(x_0,y_0,color='red')
plt.scatter(x_1,y_1,color='violet')
plt.show()  

#dividing the dataset into training and testing part
trainingDataset={}
testingDataset={}
for i in datasetDict:
  if len(trainingDataset) <= 0.8*len(datasetDict):
    trainingDataset[i]=datasetDict[i]
  else:
    testingDataset[i]=datasetDict[i]

#no. of elements in training and testing dataset
print('no. of elements in training dataset : ',len(trainingDataset))
print('no. of elements in testing dataset : ',len(testingDataset))

#function to calculate the euclidean distance
def euclideanDistance(A,B):
  sum=0
  for a,b in zip(A,B):
    sum+=(a-b)**2
  
  return sum**0.5

def knnAlgorithm(dataItem,k):
  #"key" for this dictionary will be the dataIten and the "value" will be the distance from training set elements
  distanceDictionary={}
  for i in trainingDataset:
    distanceDictionary[i]=euclideanDistance(dataItem,i)
  #now sort this dictionary in increasing order of the distance
  sortedDistanceDictionary=dict(sorted(distanceDictionary.items(),key=lambda x:x[1]))

  #now assign the values of classes to this sorted dictionary
  for i in sortedDistanceDictionary:
    for j in trainingDataset:
      if i == j:
        sortedDistanceDictionary[i]=trainingDataset[j]

  #now take into consideration the nearest 'k' neighbours based on this sorted dictionary
  knnDictionary={}
  for i in sortedDistanceDictionary:
    if len(knnDictionary)<k:
      knnDictionary[i]=sortedDistanceDictionary[i]

  #do the majority voting
  count_0=0
  count_1=0
  for i in knnDictionary:
    if knnDictionary[i]==0:
      count_0+=1
    else:
      count_1+=1

  if count_0 > count_1:
    return 0
  else:
    return 1

#train the model to find the value of 'k'
accuracy_list=[]
for i in range(15):
  predictedCorrectly=0
  for item in testingDataset:
      if testingDataset[item]==knnAlgorithm(item,i):
        predictedCorrectly+=1
  print('accuracy = ',(predictedCorrectly/len(testingDataset))*100)
  accuracy_list.append((predictedCorrectly/len(testingDataset))*100)

k=accuracy_list.index(max(accuracy_list))+1
print('value of k is ',k)

#take user input data point to determine its class
x=int(input('Enter x coordinate : '))
y=int(input('Enter y coordinate : '))

UserDefinedTuple=(x,y)

#show it on scatter plot along with training and testing dataset
plt.scatter(x,y,color='green')
plt.scatter(x_0,y_0,color='red')
plt.scatter(x_1,y_1,color='violet')

plt.show()

print('class of ',UserDefinedTuple,' : ',knnAlgorithm(UserDefinedTuple,k))
