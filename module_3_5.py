def get_multiplied_digits(number):
    first = 0
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        result = first * get_multiplied_digits(int(str_number[1:]))
    else:
        result = first
    return result


result = get_multiplied_digits(40203)
print(result)