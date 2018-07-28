full_string = input()
substring = input()

cursor = 0

ans = []

while cursor < len(full_string):
    current_slice = full_string[cursor:]

    try:
        index = current_slice.index(substring)
    except ValueError:
        if not ans:
            print(-1)
        break
    else:
        ans.append(cursor + index)

        cursor += index + 1

[print(i, end=' ') for i in ans]