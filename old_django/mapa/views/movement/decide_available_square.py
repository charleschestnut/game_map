

def decide_available_square(square_list):
    last_idx = len(square_list)
    axis_location_list = [square.axis_position for square in square_list]
    square_selected = -1

    while (type(square_selected) == int and square_selected not in range(0, last_idx)):
        print("Select, between 0 and "+str(last_idx)+" , the square to move your character.")
        counter = 0
        for axis in axis_location_list:
            print(str(counter)+": "+str(axis))
            counter += 1
        try:
            square_selected = int(input())
        except ValueError:
            print("That's not a number. Choose a N-U-M-B-E-R between 0 and "+str(last_idx))

    return square_list[square_selected]
