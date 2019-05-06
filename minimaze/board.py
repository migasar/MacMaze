"""Gere le plateau de jeu et les interactions des objets"""


from position import Position
from case import Case

import settings as constants


class Board:

    def __init__(self, grid):
        self.grid = grid


    @classmethod
    def load_blueprint(cls, filename):
        grid = []

        with open(filename, 'r') as infile:

            content = [
                line.strip() for line in infile.readlines() if line.strip()
                ]

            for y, line in enumerate(content):
                for x, col in enumerate(line):
                    if col == "S":
                        grid.append(
                            Case(x+1, y+1, walk=True, landing="start", visual=col)
                            )
                    elif col == "G":
                        grid.append(
                            Case(x+1, y+1, walk=True, landing="goal", visual=col)
                            )
                    elif col == ".":
                        grid.append(
                            Case(x+1, y+1, walk=True, visual=col)
                            )
                    else:
                        grid.append(
                            Case(x+1, y+1, walk=False, visual=col)
                            )

        return cls(grid)


    @property
    def width(self):
        return self.grid[-1].x

    @property
    def height(self):
        return self.grid[-1].y

    def inside(self,step):
        return (1, 1) <= (step.x, step.y) <= (self.width, self.height)
    

    def get_case(self, att, val):
        for i, block in enumerate(self.grid):
            if getattr(block, att) == val:
                return block

    def get_case_index(self, att, val):
        for i, block in enumerate(self.grid):
            if getattr(block, att) == val:
                return i

    def get_coordinates(self, attx, atty, valx, valy):
        for i, block in enumerate(self.grid):
            if getattr(block, attx) == valx and getattr(block, atty) == valy:
                return block


    def ending(self):
        end = self.get_case_index("landing", "goal")
        hero_case = self.get_case_index("toping", constants.HERO_CHAR)
        return end == hero_case


"""
# TEST
def main():
    board = Board.load_blueprint(constants.blueprint)

    print(board.get_case_index("landing", "goal"))
    print(board.grid[-1])

if __name__ == "__main__":
    main()
"""
