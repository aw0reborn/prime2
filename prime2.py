### YOUR CODE FOR output_prime_factors() FUNCTION GOES HERE ###
def is_prime(x):
    num=0
    num=int(x)
    if(num!=x):
        return False
    if x==1:
        return False
        
    if x== 2:
        return True

     
    for i in range(2,x):
        
        if x%i==0:
            return False
    else:
        return True
def output_prime_factors(x):
    if x < 1:
        return None
    x = int(round(x))
    for i in range(1,x+1):
        if x%i == 0:
            y = i
            y = is_prime(y)
            if y== True:
                print i
#### End OF MARKER


### YOUR CODE FOR get_nth_prime() FUNCTION GOES HERE ###
def get_nth_prime(x):
    if type(x)==float:
        return None
    
    if x <= 0:
        return None
    list1 = [2]
    number = 3
    while len(list1) < x:
        for i in list1:
            if number % i == 0:
                break        
        else:
            list1.append(number)        
        number += 2    
    return list1[-1]
#### End OF MARKER
