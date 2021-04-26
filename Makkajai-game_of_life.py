import random

arr=[[random.randint(0,1) for i in range(5)]for j in range(5)]
next_life=[[0 for i in range (5)]for j in range (5)]
n=5
state=0

print(arr)
def countneighbours(arr,x,y):
    sum=0
    for i in range(-1,2):
        for j in range(-1,2):
            sum+=arr[x+i][y+j]
    return sum


for i in range(5):
    for j in range(5):
        state=arr[i][j]
        if(i==0 or i==4 or j==0 or j==4):
            next_life[i][j]=state
        else:
            neighbours = countneighbours(arr,i,j)

            if (state==0 and neighbours==3):
                next_life[i][j]=1
            elif (state==1 and (neighbours<2 or neighbours>3)):
                next_life[i][j]=0
            else :
                next_life[i][j]=state
print(next_life)