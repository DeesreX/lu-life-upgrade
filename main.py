"""
    Author: Arthur
"""
from os import system
class Menu:    

    def __init__(self):
        system("clear")
        self.run_program()
        
    def run_program(self):
        self.running = True
        self.main_menu()

    def main_menu(self):
        first_run = True
        while(self.running):
            print("MAIN MENU\n\n\t1: [COMING SOON])\n\t2: [COMING SOON])\n\t3: [COMING SOON])\n\t4: [COMING SOON])\n\t5: Exit\n")
            if(not first_run): user_input = ""
            user_input = input("Please select\n > ")
            # if(user_input == "1"): start_user_enviroment()
            if(user_input == "5"): self.running = False
            first_run = False
            system("clear")

Menu() 