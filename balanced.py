class Stack:
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        if len(self.stack)<=0:
            return True
        else:
            return False
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if (len(self.stack)>0):
            return self.stack.pop()
    def __str__(self):
        print("The stack is")
        print(self.stack)

def findBalanced(expression):
    print(expression)
    newStack=Stack()
    for i in expression:
        if i in ['{','(','[']:
            newStack.push(i)
        else:
            if newStack.isEmpty():
                return False
            temp=newStack.pop()
            if temp=='(' and i !=')' or temp=='{' and i!='}' or temp=='[' and i!=']':
                return False
    return newStack.isEmpty()

def reduce(expression):
    string=''
    ex=''
    for i in expression:
        if i.isalnum():
            string=string+i
        elif i=='+' or i=='-' or i=='*' or i=='/':
            string=string+i
        else:
            ex=ex+i
    print(ex)
    z=findBalanced(ex)
    if z:
        print('Balanced')
    else:
        print('Not Balanced')

if __name__ == "__main__":
    expression="{7-(3-2)+[8+(99-11)]}"
    reduce(expression)
    