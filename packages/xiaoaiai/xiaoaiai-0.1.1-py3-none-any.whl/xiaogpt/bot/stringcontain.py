class StringConcatenator:
    def __init__(self):
        self.lines = []

    def add_string(self, string):
        if len(self.lines) == 0:
            self.lines.append(string)
        else:
            last_line = self.lines[-1]
            if len(last_line) + len(string) >= 8:
                remaining_space = 8 - len(last_line)
                self.lines[-1] += string[:remaining_space]
                self.lines.append(string[remaining_space:])
            else:
                self.lines[-1] += string

    def get_string(self):
        return '\r\n|'.join(self.lines)
