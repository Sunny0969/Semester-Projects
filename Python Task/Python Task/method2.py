from random import randint

MaxRow = 10
MaxCol = 10
no = 0 

no = randint(1, 50)
i = 0 
j = 0 
k = 0 
minvar  = 0 
maxvar = 0 
n = 0 
row = col = flag = 0 

n = input('Enter Size of Array (2 - 10) : ')
n = int(n)


if n < 2 and n > 10:
    print('Error. Size should be 5 - 10')

myMatrix = []

for i in range(0,n):
    myMatrix.append([])

for i in range(0,n):
    for j in range(0,n):
        myMatrix[i].append(no)
        no = no + 1


#suffle elements        

for i in range(0,n):
    for j in range(0,n):
        rand1 = randint(0, n-1)
        rand2 = randint(0, n-1)
        temp = myMatrix[rand1][rand2]
        myMatrix[rand1][rand2] = myMatrix[i][j]
        myMatrix[i][j] =  temp

for i in range(0,n):
    for j in range(0,n):
        print(myMatrix[i][j] ,end=" ")
    print()
    
for i in range(0,n):
    row = 0
    minVal = myMatrix[i][0]
    for j in range(0,n):
        if minVal > myMatrix[i][j]:
            minVal = myMatrix[i][j]
            col = j
        
        
maxVal = myMatrix[i][col]

for i in range(0,n):
    for j in range(0,n):
        if maxVal < myMatrix[i][col]:
            maxVal = myMatrix[k][col]
            
if minVal == maxVal:
    print ('Saddle Point Found')
    flag = 1
    #print('Row %s' % i+1)
    #print('Col %s' % j+1)
    print('Number is : %d' % maxVal)

if flag == 0: 
    print('No Saddle Point Found in Array')