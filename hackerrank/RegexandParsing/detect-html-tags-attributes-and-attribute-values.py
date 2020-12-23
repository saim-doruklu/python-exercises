import re

if __name__ == '__main__':
    num_lines = int(input())
    is_in_comment = False
    is_in_tag = False
    for curr_line in range(0, num_lines):
        line = input()

        p = re.compile('(?P<commentst>(?<=<!--))|'
                       '(?P<commentend>-->)|'
                       '(?P<tagst>(?<=<)\w+((?=\s)|(?=>)|(?=/)|(?=$)))|'
                       '(?P<tagend>((?<="|\s|/))>)|'
                       '(?P<tagendtwo>:^>)|'
                       '(?P<attr>\s[^\s]+="[^"]+(?=\"))')
        for m in p.finditer(line):
            if m.lastgroup == "commentst":
                is_in_comment = True
            elif m.lastgroup == "commentend":
                is_in_comment = False
            elif m.lastgroup == "tagst" and not is_in_comment:
                is_in_tag = True
                print(m.group())
            elif is_in_tag and m.lastgroup == "attr":
                print("-> " + (m.group().split('=')[0]).strip()+ " > " + m.group().split("=\"")[1].strip())
            elif is_in_tag and (m.lastgroup == "tagend" or m.lastgroup == "tagendtwo"):
                is_in_tag = False
