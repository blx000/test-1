class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers

    def __iter__(self):
        return iter(self.numbers)
