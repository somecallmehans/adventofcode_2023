import re

file = open("day_2_input.txt", "r")
content = file.read().split("\n")
# only 12 red cubes, 13 green cubes, and 14 blue cubes in the bag
red = 12
green = 13
blue = 14
thresholds = {'red': red, 'blue': blue, 'green': green}

def remove_game(game_string):
    pattern = r'^Game \d+: '
    return re.sub(pattern, '', game_string)

processed_string = [remove_game(game) for game in content]

def do_the_thing(one_game):
    # Each instance of this is 1 game
    processed_thing = one_game.split("; ")
    for pt in processed_thing:
        new_list = []
        nt = pt.split(", ")
        for n in nt:
            split = n.split(' ')
            key = split[1]
            val = split[0]
            new_list.append({key: val})
        for g in new_list:
            for key, val in thresholds.items():
                if(key in g and int(g[key]) > val):
                    return False
                else:
                    continue
    return True


valid_games = 0
for idx, one_game in enumerate(processed_string):
    check = do_the_thing(one_game)
    print(idx + 1)
    if(check):
        valid_games += (idx + 1)
print(valid_games)