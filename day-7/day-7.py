import numpy as np

def get_possible_bags(bag, rule_dict):
    # possible bags due to single applied rule
    if bag in rule_dict:
        p_bags = rule_dict[bag]
    else:
        return []
    # possible bags due to all recursively applied rules
    possible_bags = []

    for p_bag in p_bags:
        if not p_bag == 'no other bag':
            possible_bags += get_possible_bags((p_bag), rule_dict)
            possible_bags.append(p_bag)
        
    return possible_bags

input_ = open('input.txt').read().split('\n')[:-1]
rule_dict = {}

for rule in input_:
    # split rules key - value pairs
    value, keys = rule.split(' contain ')
    # split keys into list and make them uniform (remove . and plural s)
    key_list = keys.split(', ')
    value = value.strip(' ')
    for index in np.arange(len(key_list)):
        while key_list[index][0].isnumeric():
            key_list[index] = key_list[index][1:]
        key_list[index] = key_list[index].strip('.').strip('s').strip(' ') + 's'
        if key_list[index] in rule_dict:
            rule_dict[key_list[index]].append(value)
        else:
            rule_dict[key_list[index]] = [value]

# remove possible duplicates
for key in rule_dict:
    rule_dict[key] = list(dict.fromkeys(rule_dict[key]))

# find possible bags to put 'shiny gold bags' in
bag_list = list(dict.fromkeys(get_possible_bags('shiny gold bags', rule_dict)))
print(bag_list)
print(len(bag_list))
