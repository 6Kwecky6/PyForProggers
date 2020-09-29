import math

#Method to check if a number is prime
def k6(n):
    if n<=3: return n>1
    if (n>>1)<<1==n or n%3==0: return False

    i=5
    while i*i <=n:
        if n%i==0 or n%(i+2)==0:return False
        i+=6
    return True

# Producer to get a prime as we need it to save memory space, and to avoid being dependant on a list length
def prime_producer():
    n=2
    while True:
        if k6(n): yield n
        n+=1

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

#This method unpacks n into it's factors (p,q)
def find_primes(n_mod):
    prime_prod = prime_producer()
    prime = next(prime_prod)
    while n_mod%prime!=0:
        prime=next(prime_prod)
    p = prime
    q = n_mod//p
    return p,q

# Calculating the greatest common divisor recursively
def gcd(a, b):
    if b==0: return a
    return gcd(b,a%b)

# The naming is a bit weird here, but point is that this is that lambda function I'm seeing
def euclidian_carmichael(p,q):
    return (abs((p-1)*(q-1)))//gcd(p-1,q-1)

def multiplicative_inverse(a, b):
    """Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb
    """
    # r = gcd(a,b) i = multiplicitive inverse of a mod b
    #      or      j = multiplicitive inverse of b mod a
    # Neg return values for i or j are made positive mod b or a respectively
    # Iterateive Version is faster and uses much less stack space
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a  # Remember original a/b to remove
    ob = b  # negative values from return results
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # If neg wrap modulo orignal b
    if ly < 0:
        ly += oa  # If neg wrap modulo orignal a
    # return a , lx, ly  # Return only positive values
    return lx


def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr(pow(char, key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)

def main():
    encrypted_msg = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]
    public_key = (29815,100127)
    #Unpacking n to be used for
    p,q = find_primes(public_key[1])
    lam = euclidian_carmichael(p,q)
    e_inverse = multiplicative_inverse(public_key[0],lam)
    print("e-inverse: %s\ne: %s\n(e-inverse*e)mod(lambda): %s"%(e_inverse,public_key[0],(e_inverse*public_key[0])%lam))
    print(chr(exponential(encrypted_msg[0],e_inverse)%public_key[1]))
    print(decrypt((e_inverse,public_key[1]),encrypted_msg))

    #by using the public key, I will attempt to find all possible private keys(Yield could be useful here)
    #Testing every possible private key to check if I get the same char as the start char
    #Decrypt the rest
    #Pseudocode:
    #possible_pk = findPrivateKey(public_key)
    #pk =possible_pk.yield()
    #while !checkFirstChar(first_char,pk):
    #   pk=possible_pk.yield()
    #decrypt(encrypted_msg,pk,public_key)



if __name__ == '__main__':
    main()


