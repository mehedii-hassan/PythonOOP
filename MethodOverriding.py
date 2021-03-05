class Moble:
    def __init__(self):
        print("This is phone class")


class Nokia(Moble):
    # init()method overriding---------
    def __init__(self):
        super().__init__()
        print("This is Nokia class")
    # pass


s = Nokia()
