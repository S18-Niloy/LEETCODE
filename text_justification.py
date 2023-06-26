class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        curr_line = []
        curr_width = 0

        for word in words:
            if curr_width + len(curr_line) + len(word) <= maxWidth:
                curr_line.append(word)
                curr_width += len(word)
            else:
                result.append(self.format_line(curr_line, maxWidth, False))
                curr_line = [word]
                curr_width = len(word)

        result.append(self.format_line(curr_line, maxWidth, True))

        return result

    def format_line(self, line, maxWidth, is_last_line):
        if is_last_line or len(line) == 1:
            return ' '.join(line).ljust(maxWidth)

        num_words = len(line)
        total_spaces = maxWidth - sum(len(word) for word in line)
        spaces_between_words = total_spaces // (num_words - 1)
        extra_spaces = total_spaces % (num_words - 1)

        formatted_line = ''
        for i in range(num_words - 1):
            formatted_line += line[i] + ' ' * spaces_between_words
            if extra_spaces > 0:
                formatted_line += ' '
                extra_spaces -= 1

        formatted_line += line[-1]

        return formatted_line
