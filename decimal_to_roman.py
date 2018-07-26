def get_correct_thousands(number):
    return number // 1000


def get_correct_hundreds(number):
    return number // 100 % 10


def get_correct_tens(number):
    return number // 10 % 10


def get_correct_num(number):
    return number % 10


def get_int_in_roman(num, main_roman="I",before_next_int="X", middle="V"):
    if num >= 5:
        if num == 5:
            return middle
        else:
            if num == 9:
                return main_roman + before_next_int
            else:
                return middle + main_roman * (num - 5)
    else:
        if num > 3:
            return main_roman * (num - 3) + middle
        else:
            return main_roman * num


if __name__ == '__main__':
    user_number = int(input().strip())

    thousands = get_correct_thousands(user_number)
    hundreds = get_correct_hundreds(user_number)
    tens = get_correct_tens(user_number)
    nums = get_correct_num(user_number)

    thousands_in_roman = "M" * thousands
    hundreds_in_roman = get_int_in_roman(hundreds, 'C', 'M', 'D')
    tens_in_roman = get_int_in_roman(tens, 'X', 'C', 'L')
    nums_in_roman = get_int_in_roman(nums, 'I', 'X', 'V')

    print(thousands_in_roman + hundreds_in_roman + tens_in_roman + nums_in_roman)