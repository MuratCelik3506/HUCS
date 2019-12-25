# Murat Celik 21827263
import math
import sys
def delta():   # calculate discriminant
    return b**2 - 4*a*c
def solutions(): # calculate roots
    result1 = (-b + math.sqrt(delta()))/(2 * a)
    result2 = (-b - math.sqrt(delta()))/(2 * a)
    if result1 != result2:
        return str(format(result1,'.2f'))+" " + str(format(result2,'.2f'))
    else:
        return str(format(result1,'.2f'))
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if delta() > 0: # A positive discriminant
    print("There are two solutions")
    print("Solutions : ",solutions())
elif delta() == 0: # A discriminant of zero
    print("There are one solutions")
    print("Solution:",solutions())
else:# A negative discriminant
    print("There aren't solution")
