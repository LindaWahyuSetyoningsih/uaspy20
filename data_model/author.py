class Author:
    def __init__(self, name=""):
        self.name = "Linda Wahyu Setyoningsih"
        self.gender = "Perempuan"
        self.address = "Cibitung"
        self.phone = "0895326388827"

    def toString(self):
        return "Name: {0}, Address: {1}".format(self.name, self.address)
