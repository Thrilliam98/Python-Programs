def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return "No uppercase character found"

input_str_1 = "lucidProgramming"

print(find_uppercase_iterative(input_str_1))
