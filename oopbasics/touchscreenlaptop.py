from abc import abstractmethod, ABC


class TouchScreenLaptop(ABC):
    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass


class HP(TouchScreenLaptop):
    def scroll(self):
        print('HP Scroll')


class Dell(TouchScreenLaptop):
    def scroll(self):
        print('Dell Scroll')


class HPNotebook(HP):
    def click(self):
        print("Click HP")


class DellNotebook(Dell):
    def click(self):
        print("Click Dell")


hp = HPNotebook()
dp = DellNotebook()
print(hp.scroll())
print(hp.click())
print(dp.scroll())
print(dp.click())
