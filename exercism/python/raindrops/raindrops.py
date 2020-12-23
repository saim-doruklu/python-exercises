def convert(number):
    sound_of_three = "Pling" if number % 3 == 0 else ""
    sound_of_five = "Plang" if number % 5 == 0 else ""
    sound_of_seven = "Plong" if number % 7 == 0 else ""
    return f"{sound_of_three}{sound_of_five}{sound_of_seven}" or str(number)
