class Solution:
    def compress(self, chars):
        if len(chars) == 0:
            return 0

        write_index = 0
        count = 1

        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                chars[write_index] = chars[i - 1]
                write_index += 1

                if count > 1:
                    count_str = str(count)
                    for j in range(len(count_str)):
                        chars[write_index] = count_str[j]
                        write_index += 1
                
                count = 1

        chars[write_index] = chars[-1]
        write_index += 1

        if count > 1:
            count_str = str(count)
            for j in range(len(count_str)):
                chars[write_index] = count_str[j]
                write_index += 1

        return write_index
