# Looks for prime numbers between 1 and 30 (inclusive)

# for i in range(1,31,1):
#     for j in range(2,int(i/2)+1,1):
#         if i % j == 0:
#             print(i, "is not prime.")
#             break
#     else:
#         if i == 1:
#             print(i, "is not prime.")
#         else:
#             print(i, "is prime.")


## This does the same as the code above, but in a way that allows other code to reuse the "is_prime" check without having to duplicate the code.
#### Important note for using functions: python is an interpreted language, which means it is read from top to bottom. 
#### Therefore, the function definition has to be earlier in the file than any code that calls it, or the interpreter will not know that the function exists.

def is_prime(number):
    for j in range(2,int(number/2)+1,1):
        if number % j == 0:
            print(number, "is not prime.")
            break
    else:
        if number == 1:
            print(number, "is not prime.")
        else:
            print(number, "is prime.")

for i in range(1,31,1):
    is_prime(i)