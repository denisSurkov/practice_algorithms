num = int(input())
def move_tower(height, from_pole, help_pole, target_pole):
    if height != 0:
        move_tower(height - 1, from_pole=from_pole, help_pole=target_pole, target_pole=help_pole)
        move_one_disk(from_pole, target_pole)
        move_tower(height - 1, from_pole=help_pole, help_pole=from_pole, target_pole=target_pole)

def move_one_disk(fp,tp):
    print(fp,"-",tp)

move_tower(num,"1","2","3")