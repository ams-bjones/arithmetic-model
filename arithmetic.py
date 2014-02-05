def add(a,b):
    ans = a+b
    return(ans)

def sub(a,b):
    ans = a-b
    return(ans)
    
def mult(a,b):
    ans = a*b
    return(ans)
    
def div(a,b):
    ans = a/b
    return(ans)
    
def sqr(a):
    ans = a*a
    return(ans)
    
def rem(a,b):
    return (a%b)
    
def power(a,b):
    return (a**b)
    
def bid1(a):
    a = a*3
    a = a+4
    return (a)
    
def bid2(a):
    a = a+4
    a = a*3
    return (a)
   
c = 7
d = 5 
print("addition test")
print(add(c,d))
print("subtraction test")
print(sub(c,d))
print("Multiplication test")
print(mult(c,d))
print("Square test")
print(sqr(c))
print("Remainder test")
print(rem(c,d))
print("Power test")
print(power(c,d))
print("Bidmas test")
print(bid1(c,d))
print("Bidmas test 2")
print(bid2(c,d))


    
