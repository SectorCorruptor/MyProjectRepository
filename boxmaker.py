class Box:
    def __init__(self, height, width):
        self.h = height
        self.w = width
    def __repr__(self):
        s = "+" + "-"*(self.w - 2) + "+\n"
        for x in range(self.h):
            s += "|" + " "*(self.w - 2) + "|\n"
        s = s + "+" + "-"*(self.w - 2) + "+\n"
        return s

if __name__ == "__main__":
    z = Box(10, 10)
    print(z)
        
