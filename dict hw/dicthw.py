test_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20,
    'f': 10
}

value_to_check = 10
frequency = list(test_dict.values()).count(value_to_check)

print(frequency)
