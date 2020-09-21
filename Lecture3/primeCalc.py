import datetime
#Takes in a number, and checks if it'sa prime
#Output: True if prime, False if not prime
def prime_check(num):
    if (num >> 1)<<1 == num or num%3 == 0 or num%5 == 0: #Checking for normal non-prime divisible for a quick answer
        return False
    else: #Here starts the main loop
        for x in range(4,num//3):
            exp = 2
            ans = 0
            while ans <= num:
                ans = exponential(x,exp)
                if ans == num:
                    return False
                exp+=1
        return True

#Function for quick exponential calculation
def exponential(num, exp):
    if (exp >> 1)<<1 == exp:
        #Do even stuff
        if exp ==0:
            return 1
        else:
            tmp_num = exponential(num,exp//2)
            return tmp_num*tmp_num
    else:
        #Do odd stuff
        tmp_num = exponential(num,(exp-1)//2)
        return tmp_num*tmp_num*num

#prints all primes up to a limit
def find_all_prime(limit):

    #Exceptions for 2,3 and 5 come here
    print('Prime found: 2\nPrime found: 3\nPrime found: 5') #If this is unacceptable, I will remove the 'quick check' in prime_check()
    for x in range(6,limit):
        if prime_check(x):
            print('Prime found: %s'%x)

def main():
    epoch = 0
    start = datetime.datetime.now()
    while True:
        find_all_prime(1000)
        epoch+=1
        end = datetime.datetime.now()
        if (start - end).seconds >= 1:
            break

    print("The function uses %s milliseconds per iteration"%((end-start).total_seconds()*1000))


if __name__ == '__main__':
    main()