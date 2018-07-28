def is_str_int(str_):
    try:
        _ = int(str_)
    except ValueError:
        return False
    else:
        return True


def get_int(start_message, error_message, end_message):
    print(start_message)
    first_call = input()

    if is_str_int(first_call):
        print(end_message)
        return int(first_call)

    print(error_message)
    call = input()
    while not is_str_int(call):
        print(error_message)
        call = input()
    print(end_message)
    return int(call)

print(get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.'))