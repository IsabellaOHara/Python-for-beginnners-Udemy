class Programmer:

    def setName(self, name):
        self.name = name


    def getName(self):
        return self.name

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setTechnologies(self, tech):
        self.technologies = tech

    def getTechnologies(self):
        return self.technologies


p1 = Programmer()
p1.setName("Bella")
p1.setSalary(32000)
p1.setTechnologies(['Java', 'Python', 'JavaScript'])

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())
