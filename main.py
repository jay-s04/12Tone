import time

# We need to get a few things from the user to start with: reference note, prime series and transformation
def get_reference_pitch():
    while True:
        base_list = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
        enharmonics = {'Db': 'C#', 'D#': 'Eb', 'Gb': 'F#', 'G#': 'Ab', 'A#': 'Bb'}

        reference_pitch = input("Please enter your reference pitch: ")

        if reference_pitch in base_list:
            print(f"Your reference pitch is {reference_pitch}")
            return reference_pitch
        elif reference_pitch in enharmonics:
            print(f"Note unavailable. Did you mean [{enharmonics[reference_pitch]}]?")
        else:
            print("Invalid Reference Pitch. Available accidentals include: C#, Eb, F#, Ab, Bb\n")
        


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
    while True:
        user_input = input("Please enter your 12tone series. Separate the numbers with spaces: ")
        series = [i for i in list(user_input.split(' '))]
        # And now we check for errors.
        # Our two main checks are whether each element of the list is a number, and whether it's less than 12
        # This check also converts the list[str] to a list[int]
        for index, element in enumerate(series):
            if element.isdigit():
                if int(element) < 12:
                    series[index] = int(element)
                else:
                    print('Each element must be below 12\n')
                    continue
            else:
                print("Each element must be an integer from 0 - 11\n")
                continue
        # Our last check is to see whether the series has 12 unique tones
        if len(series) == 12 and (len(series) == len(set(series))):
            print(f"Your series is {series}")
            return series
        else:
            print('There should be 12 unique tones in your series\n')
            continue

# Now to write the three possible transformations
def transpose(prime_series: list[int], n: int):
    # The modulus 12 is to keep everything between 0 and 11
    transposed_list = []
    for i in prime_series:
        transposed_list.append((i + n) % 12)
    return transposed_list
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
    while(True): # This is necessary to get transformations over and over until they work
        transformations = input("What transformations would you like to do to your series: ")
        new_series = prime_series.copy()
        error = False

        # I've put something in here to deal with if they enter the number before
        # the letter. Something like '4R' instead of 'R4'
        # This is because it refers back to the instantiated dictionary instead 
        # of creating a new one in this case.
        if transformations[0].isdigit() and len(transformations) > 1:
            print("If applying more than 1 transformation, put the number after.")
            continue
        # Now to check and apply the transformations.
        for i in transformations:
            if i.isdigit():
                new_series = transpose(new_series, int(i))
            elif i.lower() == 'r':
                new_series = retrograde(new_series)
            elif i.lower() == 'i':
                new_series = invert(new_series)
            elif i.lower() == 'p':
                pass
            else:
                print('Error')
                error = True
                continue # If there's an error at all, it will break out of the initial for loop

        if error == False: # Checks if there was an error that broke out of the loop
            return new_series

# And now just a little something to spit out the notes corresponding to the numbers
def spit_out_notes(new_series, note_dictionary):
    notes = ''
    for i in new_series:
        notes += note_dictionary[i] + ' '
    return notes


# This run_again function will determine whether to keep the same series and pitch.
# This is called at the bottom of the run function if the user says Yes to run again
def run_again(reference_pitch, prime_series):
    while True:
        keep_same = input('Would you like to keep the same series and pitch? Y/n: ')
        if keep_same.lower() == 'y':
            print(f'Ok, your reference pitch is {reference_pitch}\nAnd series is {prime_series}')
            run(reference_pitch=reference_pitch, prime_series=prime_series, keep_same=True)
        elif keep_same.lower() == 'n':
            print('Resetting values...')
            run(reference_pitch=None, prime_series=None, keep_same=False)
        else:
            print('Invalid input.')
            

# Now to put it all together.
# The order is: get the reference pitch, then create a dictionary on it, then get the prime series,
# then get the transformations and apply them. Finally, spit out the notes for the series.

def run(reference_pitch, prime_series, keep_same: bool):
    if keep_same == False:
        reference_pitch = get_reference_pitch()
        prime_series = get_prime_series()

    note_dictionary = create_note_dictionary(reference_pitch)
        
    new_series = transform(prime_series)
    notes = spit_out_notes(new_series, note_dictionary)
    print(f"New series: {new_series}")
    print(notes)

    while(True):
            user_input = input("Would you like to go again? Y/n: ")
            if user_input.lower() not in 'yn': # Any answer other than yes or no
                print('Invalid input. Try again')
            elif user_input.lower() == 'n':
                print('Exiting program...')
                quit()
            elif user_input.lower() == 'y':
                run_again(reference_pitch, prime_series)
            else:
                print('What') # This should technically be inaccessible, but just in case...
                continue           

run(reference_pitch=None, prime_series=None, keep_same=False)
