def count_upper_lower(text):
    upper_count = 0
    lower_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count


input_text = input("enter string: ")
upper, lower = count_upper_lower(input_text)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
