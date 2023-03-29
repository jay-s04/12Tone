
def get_prime_series():
    user_input = input("Please enter your 12tone row. Seperate the numbers with spaces: ")
    row = [i for i in list(user_input.split(' '))]
    # And now we check for errors.
    # Our two main checks are whether each element of the list is a number and whether its less than 12
    # This check also converts the list[str] to a list[int]
    for index, element in enumerate(row):
        if element.isdigit():
            if int(element) < 12:
                row[index] = int(element)
            else:
                print('Each element must be below 12\n')
                get_prime_series()
        else:
            print("Each element must be an integer from 0 - 11\n")
            get_prime_series()
    # Our last check is to see whether the row has 12 unique tones
    if len(row) == 12 and (len(row) == len(set(row))):
        print(f"Your row is {row}")
        return row
    else:
        print('There should be 12 unique tones in your row\n')
        get_prime_series()
        
print(get_prime_series())
