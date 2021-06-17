from termcolor import colored
from pyfiglet import Figlet

class WelcomeScreen:
    
    @staticmethod
    def print_prompt():
        print(colored("*********************************************", 'blue'))        
        f = Figlet(font="smslant")
        print(colored(f.renderText('Warehouse Manager'),'green'))
        print(colored('MENU:', 'green', 'on_yellow'))
        print(colored("""
        S = Item(s) sold
        R = Item(s) recieved
        I = Show Inventory
        A = Run Inventory Analysis
        O = Optimize placement
        H = Help
        E = Exit
        """, 'yellow'))
        print(colored("*********************************************", 'blue'))

















