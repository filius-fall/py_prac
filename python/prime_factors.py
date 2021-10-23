# this can tell given number is prime or not. If not it will give factors


def num_is_prime(num):
    if num<2:
        print("Not prime")

    factors=[(1,num)]
    i=2

    while i*i<=num:
        if num%i==0:
            factors.append((i,num//i))
        i+=1

    if len(factors)>1:
        print(f"This is not prime and the factors are {factors}")

    if len(factors)==1:
        print(f"This is prime number")

num_is_prime(20)