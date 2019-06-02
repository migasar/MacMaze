"""Manage the display of every elements of the game"""


from CLI.board import Board

import config.constants as constants


class CLIview:

    def __init__(self, board):
        self.board = board


    def display_board(self):

        print("")
        display_grid = []

        for y, line in enumerate(self.board.grid):

            display_line = ""
            for block in self.board.grid[y]:
                if block.toping:
                    display_line += block.toping
                else:
                    display_line += block.visual
            display_grid.append(display_line)
        
        for line in display_grid:
            print(line)


    def display_title(self):
        print("")
        print("\t**********************************************")
        print(
            "\t  " + constants.GAME_TITLE 
            + " - " + constants.GAME_BID
            )
        print("\t**********************************************")

    def display_goodbye(self):
        print("")
        print("\t**********************************************")
        print("\t Vous quittez le jeu.")
        print("\t Le labyrinthe n'était sans doute pas fait pour vous, ")
        print("\t mais nous vous remercions d'avoir essayé.")
        print("")


    def display_victory(self):
        print("")
        print("\t**********************************************")
        print("\t Bravo, vous avez trouvé le chemin du labyrinthe,")
        print("\t mais ces jeux violents auront une fin violente.")
        print("")

    def display_defeat(self):
        print("")
        print("\t**********************************************")
        print("\t Désolé, le gardien vous a vaincu,")
        print("\t et ces jeux violents ont eu une fin violente.")
        print("")       


    def display_failure_input(self):
        print("")
        print("\t Désolé, votre commande n'est pas valide.")

    def display_no_motion(self):
        print("")
        print("\t Mac Gyver ne peut pas aller par là.")


    def display_explanation(self):
        print("")
        print("\t Dirigez MacGyver jusqu'à la sortie du labyrinthe")
        print("\t  - pour aller en haut, appuyez sur S")
        print("\t  - pour aller en bas, appuyez sur X")
        print("\t  - pour aller à gauche, appuyez sur W")
        print("\t  - pour aller à droite, appuyez sur C")
        print("\t  - pour quitter le jeu, appuyez sur Q")

    def display_invitation(self):
        print("")
        self.new_order = input("Qu'allez vous faire ?  ")
        return self.new_order

