class Checksum(object):
    def __init__(self):
        self.num_twos = 0
        self.num_threes = 0

    def get_checksum(self, filename: str) -> int:
        with open(filename, 'r') as fp:
            for line in fp:
                char_dict = {}
                for char in line:
                    if char_dict.get(char) is None:
                        char_dict[char] = 1
                    else:
                        char_dict[char] += 1
                if 2 in char_dict.values():
                    self.num_twos += 1
                if 3 in char_dict.values():
                    self.num_threes += 1
        return self.num_twos * self.num_threes


if __name__ == "__main__":
    check = Checksum()
    print(check.get_checksum("input"))
