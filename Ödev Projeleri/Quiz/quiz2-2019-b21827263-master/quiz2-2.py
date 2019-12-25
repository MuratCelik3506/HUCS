# Murat Celik 21827263
import sys
def convert(list):
    return tuple(list)
i = 1
EvenNumbers = []
S = sys.argv[1] # command line arguments
SumOfAllNumbers = 0
for z in S.split(","): #Which number are in string(S) ? Which one is even or  which one is not even?
    NumberinS = int(z)
    if NumberinS >= 0:
        SumOfAllNumbers = SumOfAllNumbers + NumberinS # Sum of All Numbers
        zero = NumberinS % 2
        if zero == 0 and NumberinS != 0 :
            EvenNumbers.append(NumberinS)
mytuple= convert(EvenNumbers)
print('Even Number:"'+str(mytuple)[1:-1]+'"')
SumOfEven=0
for y in EvenNumbers:
    SumOfEven = SumOfEven + y #Sum of All Even Numbers
print("Sum of Even Numbers:",SumOfEven)

total = SumOfEven/SumOfAllNumbers #calculating the even number rate
print("Even Number Rate:",round(total,3))
