import numpy as np

def get_possible_bags(bag, rule_dict):
    possible_bags = rule_dict[bag]

    for p_bag in possible_bags:
        if not p_bag == 'no other bag':
            possible_bags += get_possible_bags((p_bag[2:]+'s'), rule_dict)

    return possible_bags

input_ = open('input.txt').read().split('\n')[:-1]
rule_dict = {}

for rule in input_:
    # split rules key - value pairs
    key, values = rule.split(' contain ')
    # split values into list and make them uniform (remove . and plural s)
    value_list = values.split(', ')
    for index, value in enumerate(value_list):
        value_list[index] = value.strip('.').strip('s')
    rule_dict[key] = value_list

# find possible bags to put 'shiny gold bags' in
bag_list = list(dict.fromkeys(get_possible_bags('shiny gold bags', rule_dict)))
print(len(bag_list))

    