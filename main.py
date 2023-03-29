import time

# We need to get a few things from the user to start with: reference note, prime series and transformation
def get_reference_pitch():
    base_list = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']

    reference_pitch = input("Please enter your reference pitch: ")

    if reference_pitch in base_list:
        print(f"Your reference pitch is {reference_pitch}")
        return reference_pitch
    else:
        print("Invalid Reference Pitch. Available accidentals include: C#, Eb, F#, Ab, Bb\n")
        get_reference_pitch()


# Based on the reference pitch, we are able to create a corresponding dictionary.
# This dictionary will switch the numbers in the series to notes
def create_note_dictionary(reference_pitch: str):
    base_list = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
    new_list = base_list.copy()
    for i in range(new_list.index(reference_pitch)):
        # This loop will remove the first note and add it to the end
        # Doing this over and over until the reference note becomes the first pitch
        # This makes it so the chromatic scale starts at the reference pitch.
        first_note = new_list[0]
        new_list.pop(0)
        new_list.append(first_note)

    # Now that the scale starts at the reference, it is converted into a key/value pair dictionary.
    # The key being the number and the value being the note.
    return {i: x for i, x in enumerate(new_list)}


# Now to get the prime series from the user
def get_prime_series():
    user_input = input("Please enter your 12tone series. Seperate the numbers with spaces: ")
    series = [i for i in list(user_input.split(' '))]
    # And now we check for errors.
    # Our two main checks are whether each element of the list is a number and whether its less than 12
    # This check also converts the list[str] to a list[int]
    for index, element in enumerate(series):
        if element.isdigit():
            if int(element) < 12:
                series[index] = int(element)
            else:
                print('Each element must be below 12\n')
                get_prime_series()
        else:
            print("Each element must be an integer from 0 - 11\n")
            get_prime_series()
    # Our last check is to see whether the series has 12 unique tones
    if len(series) == 12 and (len(series) == len(set(series))):
        print(f"Your series is {series}")
        return series
    else:
        print('There should be 12 unique tones in your series\n')
        get_prime_series()

# Now to write the three possible transformations
def transpose(prime_series: list[int], n):
    # The modulus 12 is to keep everything between 0 and 11
    return list((i + n) % 12 for i in prime_series) 
def invert(prime_series: list[int]):
    inverted_list = []
    for i in prime_series:
        inverted_list.append(12 - i)
    # Since 12 is 0, we replace the 12 in the series with 0
    index_of_12 = inverted_list.index(12)
    inverted_list[index_of_12] = 0
    return inverted_list
def retrograde(prime_series: list[int]):
    return prime_series[::-1] # Simply returns the reverse of the list

# Finally, we can get what transformation the user wants to do to their series
def transform(prime_series: list[int]):
    transformations = input("What transformations would you like to do to your series: ")
    transformations = transformations.lower()
    new_list = prime_series.copy()
    # Now to check and apply the transformations.
    """
    for i in transformations:
        print(new_list)
        if i.lower() == 'r':
            new_list = retrograde(new_list)
            print(new_list)
        elif i.lower() == 'i':
            new_list = invert(new_list)
        elif str.isdigit(i):
            new_list = transpose(new_list, int(i))
        elif i.lower() == 'p':
            new_list = new_list
            pass
        else:
            print('Error')
            transform(prime_series) # This shouldn't happen unless I need it to

    return new_list

print(transform([0, 1, 2, 3]))
"""
# TODO: Make the loop work. I have no idea why it goes to the else and throws the error
# even after I reset the variable values.
# Honestly I might just rewrite the loop to make it work properly