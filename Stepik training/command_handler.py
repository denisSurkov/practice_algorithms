def log_processing(process):
    print(f'Processing "{process}" command...')

command = input()

while command != 'End':
    log_processing(command)
    command = input()
else:
    print('Good bye')