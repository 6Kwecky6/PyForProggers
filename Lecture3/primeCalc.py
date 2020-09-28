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
    primes = [2, 3, 5]
    for x in range(6,limit):
        if prime_check(x):
            primes.append(x)
    return primes

def k6(n):
    if n<=3: return n>1
    if (n>>1)<<1==n or n%3==0: return False

    i=5
    while i*i <=n:
        if n%i==0 or n%(i+2)==0:return False
        i+=6
    return True



def main():
    epoch = 0
    start = datetime.datetime.now()
    while True:
        old_primes= find_all_prime(1000)
        epoch+=1
        end = datetime.datetime.now()
        if (start - end).seconds >= 1:
             break

    print("The old function uses %s milliseconds per iteration"%((end-start).total_seconds()*1000))
    epoch = 0
    start = datetime.datetime.now()
    while True:
        primes=[]
        for i in range(1000):
            if k6(i): primes.append(i)
        epoch += 1
        end = datetime.datetime.now()
        if (start - end).seconds >= 1:
            break
    print("The k6 function uses %s milliseconds per iteration" % ((end - start).total_seconds() * 1000))
    diff = [item for item in old_primes if item not in primes]
    print(diff)
    # Conclusion: no only was the old algorithm much slower, but it was also wrong

if __name__ == '__main__':
    main()