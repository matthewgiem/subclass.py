import copy
class ReversedStr(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self

class FilledList(list):
    def __init__(self, count, value, *args, **kwargs):
        super(FilledList, self).__init__(self, count, value, *args, **kwargs)
        for _ in range(count):
            self.append(copy.copy(value))
