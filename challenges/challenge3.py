def highest_consonant_string(str):
    # Define the vowels to identify consonants
    vowels = "aeiou"
    
    # Assign numerical values to consonants
    consonant_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
                        'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
                        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
                        'w': 23, 'x': 24, 'y': 25, 'z': 26}
    
    def calculate_value(substring):
        return sum(consonant_values[char] for char in substring)
    
    # Generate a list of consonant substrings by splitting the input string using vowels as delimiters
    consonant_substrings = [substring for substring in str.split(vowels) if substring != ""]
    
    # Find the highest value among the consonant substrings
    highest_value = max(calculate_value(substring) for substring in consonant_substrings)
    
    return highest_value

# Test cases
str = input("Enter a random name: ")  # Take input from the user
print(f"{str}, {highest_consonant_string(str)}")  