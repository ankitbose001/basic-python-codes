import math
testcasenum=int(input())
testlist=[]
for _ in range(0,testcasenum):
    number=int(input(''))
    testlist.append(number)
for i in testlist:
    flag=0
    if i==1:
        print('Not prime')
    else:
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                #print(str(i) + ' is prime')
                flag=flag+1
                #print(i)
                break
            else:
                continue
        #print(flag)
        if flag!=0:
            print('Not prime')
        elif flag ==0 and i!=1:
            print('Prime')
    
