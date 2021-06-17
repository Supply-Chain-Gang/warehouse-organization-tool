# import threading
# import os
# import time
# import sys
# import random
from termcolor import colored
from pyfiglet import Figlet
from warehouse_organization_tool.utilities.user_input import UserInput

class WelcomeScreen:
    # def __init__(self):
        # self.pipe = []
        # self.slash = []
        # self.u_score = []
        # self.manager = str(open("warehouse_organization_tool/utilities/welcome_screen/pattern.txt").read().rstrip())

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

# if __name__ == "__main__":
#     welcome_screen = WelcomeScreen()
#     welcome_screen.colored_characters()

"""
[summary] Below is code to make the coloring of the characters animated.
Could not get this to work. Check into Engineer Man's Christmas Tree Video. 
"""

        # if color == "red":
        #     print("Made it to red")
        #     return prRed()
        # if color == "green":
        #     return '\033[92m{char}\033[0m'.format('{'|'}')
        # if color == "blue":
        #     return '\033[94m{char}\033[0m'.format('{'_'}')

    # def twinkle(self, char, indexes, color):
    #     mutex = threading.Lock()
    #     off = True
    #     while True:
    #         for idx in indexes:
    #             self.manager[idx] = self.colored_characters(color, char) if off else self.manager[idx]
    #         mutex.acquire()
    #         os.system('cls' if os.name == 'nt' else 'clear')
    #         print(''.join(self.manager))
    #         mutex.release()
    #         off = not off
    #         time.sleep(random.uniform(.5, 1.5))
    #         user_response = UserInput.get_and_validate_input
    #         if user_response:
    #             return False
    #         else:
    #             continue

            
            #need to exit out of loop with keyboard inputs
            #but not exit program
            #go back into loop if re-enter main menu

    # def all_characters(self):
    #     pipes = random.sample(self.pipe, len(self.pipe)// 2)
    #     slash = random.sample(self.slash, len(self.slash)// 2)
    #     u_score = random.sample(self.u_score, len(self.u_score)// 2)

    #     for i, c in enumerate(self.manager):
    #         if c == "|":
    #             self.pipe.append(i)
    #         if c == "/":
    #             self.slash.append(i)
    #         if c == "_":
    #             self.u_score.append(i)

    #     tp = threading.Thread(target=self.twinkle("|", pipes, "red" ))
    #     ts = threading.Thread(target=self.twinkle("/", slash, "green" ))
    #     tu = threading.Thread(target=self.twinkle("_", u_score, "blue" ))

    #     for t in [tp, ts, tu]:
    #         t.start()
    #     for t in [tp, ts, tu]:
    #         t.join()