gifts = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves, ",
    "three French Hens, ",
    "four Calling Birds, ",
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, ",
]

day_number = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]


def recite(start_verse, end_verse):
    recites = []
    for index in range(start_verse - 1, end_verse):
        recites.append(get_recite_of_day(index))
    return recites


def get_recite_of_day(day):
    gifts_of_day = gifts[day:0:-1] + (["and "] if day > 0 else []) + [gifts[0]]
    intro = f"On the {day_number[day]} day of Christmas my true love gave to me: "
    return f"{intro}{''.join(gifts_of_day)}"
