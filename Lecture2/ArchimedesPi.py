import math

def main():
    ArchimedesPiEstimator('100')
    print('Real pi: ')
    print(math.pi)

def ArchimedesPiEstimator(accuracy):
    side = 1.0
    resolution = 6.0
    previous_estimate = 4.0
    current_estimate = resolution/2

    while abs(previous_estimate-current_estimate)>float('1.00e-'+accuracy):
        a = math.sqrt(1.0-math.pow(side/2,2))
        b = 1.0-a
        side = math.sqrt(math.pow(b,2)+math.pow(side/2,2))
        resolution= resolution*2
        previous_estimate=current_estimate
        current_estimate=(resolution*side)/2
        print(current_estimate)


if __name__ == '__main__':
    main()