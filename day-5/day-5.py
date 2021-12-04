import numpy as np

# return seat id for given code
def get_seat_id(code):
    # initialize starting boundary values
    c_low, r_low = 0, 0
    c_up, r_up = 7, 127 
    # find row
    for letter in code[:7]:
        if letter == 'F':
            r_up = int((r_up-1+r_low)/2)
        else:
            r_low = int((r_up+r_low+1)/2)
    # find col
    for letter in code[7:]:
        if letter == 'L':
            c_up = int(np.floor((c_up-1+c_low)/2))
        else:
            c_low = int(np.floor((c_up+c_low+1)/2))
    # upper and lower bounderies should now be equal and
    # hold the row / col value -> return seat id
    return r_low*8+c_low
input_ = open('input.txt').read().split('\n')[:-1]
seat_id_list = []

for code in input_:
    seat_id_list.append(get_seat_id(code))

# part 1
#print(np.max(seat_id_list))

# part 2
seat_id_list = np.sort(seat_id_list)
# index of seat with an id of (my_seat_id - 1)
index = np.nonzero(seat_id_list[1:]-seat_id_list[:-1]-1)[0][0]
my_seat_id = seat_id_list[index]+1
print(my_seat_id)
# just a check if the found seat id is missing in the list
print(np.any(np.isin(my_seat_id, seat_id_list)))

