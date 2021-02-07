import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for line in lines:
        line = "asda __ass __a__ qwe__qwe cd_ _qq asdasd xcz___"
        list_item_matcher = re.match(r'\* (.*)', line)
        if list_item_matcher:
            list_item = True
            line = list_item_matcher.group(1).strip()

        heading_matcher = re.match("([#]{1,6})(.*)", line)
        if heading_matcher is not None:
            heading = heading_matcher.group(1)
            html_heading_type = f'h{len(heading)}'
            line = heading_matcher.group(2).strip()

        bold_italic_boundaries = re.compile(
            "((?:^[_]+(?=[^_]))|(?:(?<= )[_]+(?=[^_]))|(?:(?<=[^_])[_]+(?= ))|(?:(?<=[^_])[_]+$))").split(line)
        # ['asda ', '__', 'ass ', '__', 'a', '__', ' qwe__qwe cd', '_', ' ', '_', 'qq asdasd xcz', '___', '']
        for index, element in range(1, len(bold_italic_boundaries)-1):
            if re.match("_+", element):
                if index == 1 and  len(bold_italic_boundaries[0]) == 0:
                    is_left = True
                elif bold_italic_boundaries[index-1][-1] == " ":
                    is_left = True
                elif index == len(bold_italic_boundaries)-2 and len(bold_italic_boundaries[len(bold_italic_boundaries)-1]) == 0:
                    is_right = True
                elif bold_italic_boundaries[index+1][0] == " ":
                    is_right = True
                else:
                    raise Exception(f"There was an error in index {index} contaning element {element}")
            # if is_left:
            #     pass
            # else:
            #     pass


        for boundary in bold_italic_boundaries:
            left_underscores = boundary.group(2)
            right_underscore = boundary.group(4)
            if left_underscores is not None:
                depth += len(left_underscores)
            elif right_underscore is not None and depth > 0:
                depth = depth

        m = re.match(r'\* (.*)', line)
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                           m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                           '</em>' + m1.group(3)
                    is_italic = True
                line = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                           m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                           '</em>' + m1.group(3)
                line = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', line)
        if not m:
            line = '<p>' + line + '</p>'
        m = re.match('(.*)__(.*)__(.*)', line)
        if m:
            line = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', line)
        if m:
            line = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        if in_list_append:
            line = '</ul>' + line
            in_list_append = False
        res += line
    if in_list:
        res += '</ul>'
    return res
