def tally(rows):
    table = dict()
    for row in rows:
        tokens = row.split(";")
        first_team_name = tokens[0]
        second_team_name = tokens[1]
        table.setdefault(first_team_name, {"name": first_team_name, "mp": 0, "w": 0, "d": 0, "l": 0, "p": 0})
        table.setdefault(second_team_name, {"name": second_team_name, "mp": 0, "w": 0, "d": 0, "l": 0, "p": 0})
        first_team_info = table[first_team_name]
        second_team_info = table[second_team_name]

        result = tokens[2]
        if result == "win":
            first_team_info["w"] += 1
            second_team_info["l"] += 1
            first_team_info["p"] += 3
        elif result == "loss":
            second_team_info["w"] += 1
            first_team_info["l"] += 1
            second_team_info["p"] += 3
        else:
            first_team_info["d"] += 1
            first_team_info["p"] += 1
            second_team_info["d"] += 1
            second_team_info["p"] += 1

        first_team_info["mp"] += 1
        second_team_info["mp"] += 1

    def to_string_repr(name, mp, w, d, l, p):
        return "|".join([f'{name: <31}',
                         f'{mp: >3} ',
                         f'{w: >3} ',
                         f'{d: >3} ',
                         f'{l: >3} ',
                         f'{p: >3}'])

    def sort_by(item):
        return -1 * item["p"], item["name"]

    return [to_string_repr("Team", "MP", "W", "D", "L", "P")] + [to_string_repr(**team) for team in
                                                                 sorted(table.values(), key=sort_by)]
