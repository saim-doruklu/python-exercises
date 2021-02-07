import re


class StringLength:
    def decode(self, escaped_string: str):
        escaped_string = re.sub("^\"", "", escaped_string)
        escaped_string = re.sub("[\"]\n?$", "", escaped_string)
        escaped_string = re.sub("[\\\]x[0-9a-f]{2}", "a", escaped_string)
        escaped_string = re.sub("[\\\][\"]", "a", escaped_string)
        escaped_string = re.sub("[\\\][\\\]", "a", escaped_string)
        return escaped_string

    def encoded_length(self, escaped_string: str):
        escaped_string = re.sub("[\\\]", "aa", escaped_string)
        escaped_string = re.sub("[\"]", "aa", escaped_string)
        # len_by_replacement = len("a" + escaped_string + "a")
        # print(len_by_replacement)
        encode_len = len(re.findall("[\\\]", escaped_string)) + len(re.findall("[\"]", escaped_string)) + len(
            escaped_string) + 2
        # print(len_by_regex)
        return encode_len


if __name__ == '__main__':
    string_length = StringLength()
    decode_diff = 0
    encode_diff = 0
    with open('inputs/string-length.txt', 'r') as file:
        all_lines = file.readlines()
        for line in all_lines:
            line = line.strip()
            decoded = string_length.decode(line)
            # print(line, "\n", decoded, "\n")
            decode_diff += len(decoded) - len(line)

            encoded = string_length.encoded_length(line)
            # print(line, "\n", encoded, "\n")
            encode_diff += encoded - len(line)

    print(decode_diff)
    print(encode_diff)
