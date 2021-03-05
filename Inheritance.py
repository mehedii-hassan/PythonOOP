class Phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can messange")


class Iphone(Phone):  # using inheritance-----------------------
    """
        def call(self):
        print("You can call")

        def message(self):
        print("You can message")
    """

    def photo(self):
        print("You can take photo ")


i = Iphone()
i.message()
i.call()
i.photo()
print(issubclass(Iphone, Phone))
