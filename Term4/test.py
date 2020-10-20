#DECLARAING VARIABLES (global variables)
myVariable = 10

#IF STATEMENTS
if myVariable < 100: 
        print("this is less than 100")
else:
    print('this is more than 100')

#LOOPS
while myVariable > 0:
    print('counting down', myVariable)
    myVariable -= 1 # EQUIVALENT TO myVariable = myVariable - 1

for i in range(0,10): # 10 is exclusive, not included
    print('counting', i)

for i in range(0,5): #different i local variable, doesn't affect the result if it is declared again
    print('counting haha', i)

#LIST which can have different types of data. By default it will be all printed as strings without having to make it clear
myList = [123, 'hello', 'this is a test', 678, 356]

print(myList)

print('at index 0 it is', myList[0])

myList[0] = 'I changed this'
print(myList)

#READING AND WRITING FILES
myFile = open("text.txt", "r") #modes "r,w,a"
print(myFile.readlines().strip())
myFile.close() #ALWAYS CLOSE IT!

myFile - open("text.txt", "a")
myFile.write("ADDING a new line!")
myFile.close()