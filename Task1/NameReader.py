def main():
    inp = input('Please enter your full name: ')
    names = inp.split()
    print('Credentials: ', end = '')
    for name in names:
        print(name[0], end = '')
    print()
    names.reverse()
    print('Welcome mr. ' + ', '.join(names))

if __name__ == '__main__':
    main()