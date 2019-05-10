import pytest
#update with assignment name
import calculator

def main():
    a = ''
    while a not in ('run','test'):
        print("Choose an option:\n\tRun\tTest")
        a = input("Your choice: ")
        a=a.lower()
    if a=="run":
        calculator.main()
    elif a=="test":
        pytest.main(['-v'])

if __name__ == '__main__':
    main()
