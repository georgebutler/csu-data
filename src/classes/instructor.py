class Instructor:
    def __init__(self, name_first, name_last):
        self.name_first = name_first.strip()
        self.name_last = name_last.strip()

    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.name_first!r} {self.name_last!r})')