class Patient:

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSSN(self, SSN):
        self.__SSN = SSN

    def getSSN(self):
        return self.__SSN


p1 = Patient()
p1.setId(1234)
p1.setName("Jill")
p1.setSSN("028492")

print(p1.getId())
print(p1.getName())
print(p1.getSSN())


