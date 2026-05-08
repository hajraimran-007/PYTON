#Write a function is_prime(n) that returns True if n is a prime number, else False. Assume n >= 2
def is_prime(n):
 for i in range(2,n):
        if i%n==0:
            return False
        return True
 print(is_prime(5))   # True
print(is_prime(2))   # False

