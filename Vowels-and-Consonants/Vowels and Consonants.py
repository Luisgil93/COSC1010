#
# Name
# Date
# Vowels and Consonants Programming Project
# COSC 2409 DNT
#
# Main function
def main():
    # Get string from user.
    user_str = input('Enter a string of characters:')

    # Report the vowels and consonants.
    print('That string has', num_vowels(user_str), 'Vowels and', \
          num_consonants(user_str), 'consonants.')

# The num_vowels funtion returns the number of
# Vowels in the string passed as an argument.
def num_vowels(s):
    # Make a list containing the vowels.
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Initialize an accumulator.
    v_count = 0

    # Count the vowels in s.
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1

    # Return the vowel count.
    return v_count

# The num_consonants function returns the number of
# consonants in the string passed as an argument.
def num_consonants(s):
    # Make a list containing the vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Initialize an accumulator
    c_count = 0

    # Count the consonants in s.
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            c_count += 1

    # Return of the consonant count.
    return c_count

# Call the main funtion
main()
      
