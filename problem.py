test_data = [3, "hello", True, 20, "world", False]

def analyze_data(test_data):
    for item in test_data:
        if type(item) is int and item < 5:
            print(f"success, {item}")
        elif type(item) is int and item >=5:
            print(f"notice confirmation message showing its value {item}")
        elif type(item) is str:
            print(f"success confirmation message displaying the string value {item}")
        else:
            print(f"notice encountered other data type {item}")
analyze_data(test_data)
