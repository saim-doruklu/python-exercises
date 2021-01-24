class DayFour:
    def MD5(self, message):
        s = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
             5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
             4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
             6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
        K = [0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
             0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
             0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
             0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
             0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
             0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
             0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
             0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
             0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
             0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
             0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
             0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
             0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
             0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
             0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
             0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391]

        def bin_to_int(binary):
            return int(''.join(binary), 2)

        def left_rotate(integer, rotation):
            return (integer << rotation) | (integer >> (32 - rotation))

        a0 = 0x67452301
        b0 = 0xefcdab89
        c0 = 0x98badcfe
        d0 = 0x10325476
        message_bits = self.tobits(message)
        original_length_in_bits = len(message_bits)
        message_bits.append("1")
        message_bits = message_bits + ["0"] * ((448 - (len(message_bits) % 512)) % 512)
        length_in_bits = list("{0:b}".format(original_length_in_bits))
        length_in_bits = ["0"]*(64-len(length_in_bits)) + length_in_bits
        message_bits = message_bits + length_in_bits

        num_chunks = len(message_bits) // 512
        if len(message_bits) % 512 > 0:
            num_chunks += 1

        addition_modulo = 2**32
        for chunk_i in range(num_chunks):
            chunk_start_index = chunk_i * 512

            M = {}
            for i in range(14):
                word_start_index = chunk_start_index + i * 32
                byte_one = message_bits[word_start_index + 24:word_start_index + 32]
                byte_two = message_bits[word_start_index + 16:word_start_index + 24]
                byte_three = message_bits[word_start_index + 8:word_start_index + 16]
                byte_four = message_bits[word_start_index:word_start_index + 8]
                M[i] = bin_to_int(byte_one + byte_two + byte_three + byte_four)
            fifteenth_word_start = chunk_start_index + 15 * 32
            fourteenth_word_start = chunk_start_index + 14 * 32
            M[14] = bin_to_int(message_bits[fifteenth_word_start:])
            M[15] = bin_to_int(message_bits[fourteenth_word_start:fourteenth_word_start+32])

            A = a0
            B = b0
            C = c0
            D = d0

            for i in range(64):
                if -1 < i < 16:
                    F = ((B & C) | (~B & D))
                    g = i
                elif 15 < i < 32:
                    F = ((D & B) | (~D & C))
                    g = (5*i + 1) % 16
                elif 31< i < 48:
                    F = B ^ C ^ D
                    g = (3*i + 5) % 16
                else:
                    F = C ^ (B | ~D)
                    g = (7*i) % 16

                F = (F + A + K[i] + M[g]) % addition_modulo
                A = D
                D = C
                C = B
                B = (B + left_rotate(F, s[i])) % addition_modulo

            a0 += A
            a0 %= addition_modulo
            b0 += B
            b0 %= addition_modulo
            c0 += C
            c0 %= addition_modulo
            d0 += D
            d0 %= addition_modulo

        def revert_bytes(hex_str):
            return hex_str[6]+hex_str[7]+hex_str[4]+hex_str[5]+hex_str[2]+hex_str[3]+hex_str[0]+hex_str[1]

        def eight_digit_hex(num):
            return format(num, '{fill}{align}{width}{type}'.format(fill='0', align='>', width=8, type='x'))

        return revert_bytes(eight_digit_hex(a0)) + revert_bytes(eight_digit_hex(b0))\
                 + revert_bytes(eight_digit_hex(c0)) + revert_bytes(eight_digit_hex(d0))

    def tobits(self, s):
        result = []
        for c in s:
            bits = bin(ord(c))[2:]
            bits = '00000000'[len(bits):] + bits
            result.extend(bits)
        return result

    def frombits(self, bits):
        chars = []
        for b in range(len(bits) / 8):
            byte = bits[b * 8:(b + 1) * 8]
            chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
        return ''.join(chars)


if __name__ == '__main__':
    # print((448 - ((447) % 512)) % 512)
    day_four = DayFour()
    for i in range(999999,2000000):
        if i%10000 == 0:
            print("Checkpoint ", i)
        result = day_four.MD5("bgvyzdsv"+str(i))
        if result.startswith("000000"):
            print(i)
    # result = day_four.MD5("asdasd")
    # print(result, " a8f5f167f44f4964e6c998dee827110c")
