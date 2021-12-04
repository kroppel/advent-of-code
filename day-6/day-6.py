import numpy as np

def get_count_anyone(people):
    return len(list(dict.fromkeys("".join(people))))

def get_count_everyone(people):
    answer_count = np.zeros(26)
    for answers in people:
        for c in answers:
            # get ascii value of char, shift is so that 'a' maps
            # to 0 and increment count array on the resulting index 
            answer_count[ord(c)-97] += 1

    return np.count_nonzero(answer_count == len(people))

input_ = open('input.txt').read().split('\n\n')
sum_anyone, sum_everyone = 0, 0

for group in input_:
    people = group.strip('\n').split('\n')
    # join strings, remove duplicate chars and add length to sum
    sum_anyone += get_count_anyone(people)
    sum_everyone += get_count_everyone(people)

# part 1
print(sum_anyone)

# part 2
print(sum_everyone)