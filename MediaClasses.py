class Media:
    def __init__(self, title):
        self.title = title
        self.author = ""  # For books
        self.director = ""  # For Movies
        self.year = ""
        self.category = ""  # Media type
        self.genre = ""
        self.subgenre = ""
        self.players = 0  # For games
        self.age_restriction = None
        self.actors = []

    def set_attr(self, key, value):
        self.__dict__[key] = value

    def get_attr(self, key):
        return self.__dict__[key]

    # def __del__(self):
    #     delstatement = str(self.title + " has been deleted.")
    #     print(delstatement)
    #     return delstatement


# Test:
def test():
    rh = Media("Der Räuber Hotzenplotz")

    print("Titel: ", rh)

    rh.set_attr('author', 'Otfried Preußler')

    print(rh.title, "ist von", rh.author)
    for item in rh.__dict__.items():
        print(item)
    print("Ende")

if __name__ == "__main__":
    test()