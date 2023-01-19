#Basic - Print all integers from 0 to 150. 
for i in range(150):
    print(i)

#Multiples of Five - 
for i in range(5, 1000, 5): 
    print(i)

#Counting, the Dojo Way 

def countingTheDojoWay():
    for i in range (1, 101): 
        if i % 10 == 0:
            print('Coding Dojo')
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)

countingTheDojoWay()

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0
for i in range (1, 500000, 2): 
    sum += i 
print(sum)

#Countdown by Fours - Print Positive Numbers starting at 2018, counting down by four

for i in range(2018, 0, -4):
    print(i)

#Flexible Counter - See three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a nultiple of mult. For example, if lowNum=2, highNum=9 and mult=3, the loop should print 3,6,9 (on successive lines)

lowNum = 4
highNum = 12
mult = 2 

for i in range (lowNum, highNum+1):
    if i % mult == 0: 
        print(i)







