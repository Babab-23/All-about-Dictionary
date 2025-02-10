from collections import Counter

def check_frequency(test_dict):
    # Extracting values from dictionary
    values = test_dict.values()
    
    # Counting frequency of each value
    freq_counter = Counter(values)
    
    return freq_counter

# Example dictionary
test_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20,
    'f': 10
}

# Checking frequency
frequency = check_frequency(test_dict)
print("Frequency of values:", frequency)
