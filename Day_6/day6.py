import os


# paths
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'data.txt')


# part 1 
def part1(days):
    with open(filename, 'r') as file:
        fishes = [int(i) for i in file.read().split(',')]
    days = range(days)

    for day in days:
        fish_babys = 0
        for i in range(len(fishes)):
            if fishes[i] == 0:
                fishes[i] = 6
                fish_babys += 1
            else:
                fishes[i] -= 1
        for fish_baby in range(fish_babys):
            fishes.append(8)
        # print(f"After Day {day+1}: {fishes}")
    print(f"After Day {day+1}: {len(fishes)}")


# part 2
def update_dict(data_dict):
    new_dict = {}

    new_dict[6] = data_dict[0]
    new_dict['6_new'] = data_dict[7]
    new_dict[5] = data_dict[6] + data_dict['6_new']

    for i in [1, 2, 3, 4, 5, 8]:
        new_dict[i-1] = data_dict[i]

    new_dict[8] = new_dict[6]
    
    return new_dict

def part2(days):
    with open(filename) as file:
        fishes = [int(i) for i in file.read().split(',')]
    data_dict = {}
    for i in range(9):
        data_dict[i] = 0
    data_dict["6_new"] = 0
        
    for fish in fishes:
        data_dict[fish] += 1
    for day in range(days):
        data_dict = update_dict(data_dict)
    print(f"After Day {day+1}: {sum(data_dict.values())}")


part1(80)
part2(256)

