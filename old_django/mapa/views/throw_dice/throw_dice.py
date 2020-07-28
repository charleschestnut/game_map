from random import randrange


def throw_dice():
    dice_number = randrange(1, 6)
    print("You have thrown you dice and you get a..."+str(dice_number))
    return dice_number
