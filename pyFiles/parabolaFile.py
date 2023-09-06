# parabolaFile.py
from . import plt, np, random
from . import xmin, xmax, steps, linewidth

plt.ion()

from ._plotSettFile import plotSett


class parabola(plotSett):

    def __init__(self, xmin = xmin, xmax = xmax, steps = steps):

        super().__init__(xmin, xmax, steps)
        self.xShift = np.random.randint(xmin, xmax)
        self.yShift = np.random.randint(xmin, xmax)
        self.concavity = np.random.randint(-10, 10)/5#to be checked out!
        self.lines = []
        self.data = None
        self.name =  None
        self.color = random.choice(self.colors)

    def draw(self ):
        #self.remove()
        self.__del__()

        self.data = [ self.x ]

        self.data = self.data + [self.concavity*(self.x - self.xShift)**2 + self.yShift]
        line, = self.ax.plot(self.data[0], self.data[1], linewidth=self.linewidth, color = self.color, label = self.name) # can be optimized for ALL pictures vi rmParams
        
        self.lines = []
        self.lines.append(line)

    def __str__(self):

        super().__str__()

        attributes = (
            f"\033[93mClass type:\033[0m parabola\n"
            f"\nAttributes:\n"
            f"\033[93m.xShift = \033[0m {self.xShift}\n"
            f"\033[93m.yShift = \033[0m {self.yShift}\n"
            f"\033[93m.concavity = \033[0m {self.concavity}\n"
            f"\033[93m.data[0] =\033[0m {self.data[0]}\n"
            f"\033[93m.data[1] =\033[0m {self.data[1]}\n"
            f"\033[93m.name:\033[0m {self.name}\n"
            f"\033[93m.color:\033[0m {self.color}\n"
        )
        
        methods = (
            f"\nMethods:\n"
            f"\033[93m.draw()\033[0m\n"
            f"\033[93m.erase()\033[0m\n"
        )

        return attributes + methods + self.plotSettings
