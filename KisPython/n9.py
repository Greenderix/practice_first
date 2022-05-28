class MilesFSM():

    def __init__(self):
        self.state = 'A'

    def grow(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'E'
            return 2
        elif self.state == 'G':
            self.state = 'A'
            return 11
        elif self.state == 'D':
            self.state = 'E'
            return 5
        else:
            raise KeyError

    def get(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'A'
            return 6
        elif self.state == 'G':
            self.state = 'H'
            return 10
        else:
            raise KeyError

    def load(self):
        if self.state == 'B':
            self.state = 'G'
            return 3
        elif self.state == 'E':
            self.state = 'F'
            return 8
        elif self.state == 'F':
            self.state = 'G'
            return 9
        elif self.state == 'D':
            self.state = 'H'
            return 7
        else:
            raise KeyError


def main():
    obj = MilesFSM()
    return obj
