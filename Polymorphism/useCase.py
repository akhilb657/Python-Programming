from abc import abstractmethod,ABC

class TouchScreenLaptop(ABC):
    @abstractmethod
    def scroll(self):
        pass
    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):
    def scroll(self):
        print("Scrolling in HP Lap")

class DELL(TouchScreenLaptop):
    def scroll(self):
        print("Scrolling in DELL Lap")

class HPNotebook(HP):
    def click(self):
        print("Clicking in HP")

class DELLNotebook(DELL):
    def click(self):
        print("Clicking in DELL")

h = HPNotebook()
h.scroll()
h.click()

d = DELLNotebook()
d.scroll()
d.click()