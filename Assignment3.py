def isequal(x,y,z):
    if x == y and x <= z or x >= z:
        result = True
    elif x == z and y >= x or y <= x:
        result = True
    elif x != y != z:
        result = False
    return result

val1 = input("Enter first num:")
val2 = input("Enter second num:")
val3 = input("Enter third num:")

print(isequal(val1, val2, val3))
@skapo14
