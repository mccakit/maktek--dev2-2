def least_bigger_prime_number():
    number=int(input("Write a number"))
    check=True
    temp_number=1
    while check:
        checked_number=number+temp_number
        def prime_checker(number):
            list = []
            for k in range(1, number + 1):
                list.append(k)
            list.remove(1)
            list.remove(number)
            end = 0
            while end == 0:
                for m in list:
                    if number % m == 0:
                        end = 1
                if end == 1:
                    return False
                else:
                    return True
        if prime_checker(checked_number) is True:
            print(f"The least bigger prime number is{checked_number}")
            check=False
        else:
            temp_number+=1
least_bigger_prime_number()