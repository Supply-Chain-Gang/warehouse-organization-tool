# import threading
# import os
# import time
# import sys
# import random
from warehouse_organization_tool.utilities.user_input import UserInput

class WelcomeScreen:
    def __init__(self):
        self.pipe = []
        self.slash = []
        self.u_score = []
        self.manager = str(open("warehouse_organization_tool/utilities/welcome_screen/pattern.txt").read().rstrip())

    def colored_characters(self, text):
        # text = self.manager
        def prRed(skk): 
            return("\033[91m {}\033[00m" .format(skk))

        def prGreen(skk): 
            return("\033[92m {}\033[00m" .format(skk))

        def prCyan(skk): 
            return("\033[96m {}\033[00m" .format(skk))

        # for char in text:
        #     if char == "/":
        #         print(prRed(char))
        #     if char == "|":
        #         print(prRed(char))
        #     if char == "_":
        #         print(prRed(char))
        #     if char == "*":
        #         print(prCyan(char))
        #     else:
        #         print(prGreen(char))
        # print(prRed(text))

        print(prCyan("*******************************************"))
        print(prGreen(" _      __             __                   "))
        print(prGreen("| | /| / /__ ________ / /  ___  __ ________ "))
        print(prGreen("| |/ |/ / _ `/ __/ -_) _ \/ _ \/ // (_-< -_)"))
        print(prGreen("|__/|__/\_,_/_/  \__/_//_/\___/\_,_/___|__/ "))
        print(prGreen("   __  ___                           "))
        print(prGreen("  /  |/  /__ ____  ___ ____ ____ ____"))
        print(prGreen(" / /|_/ / _ `/ _ \/ _ `/ _ `/ -_) __/"))
        print(prGreen("/_/  /_/\_,_/_//_/\_,_/\_, /\__/_/   "))
        print(prGreen("                      /___/          "))
        print(prRed("Menu:"))
        print(prRed("S = Item(s) sold "))
        print(prRed("R = Item(s) recieved"))
        print(prRed("I = Show Inventory"))
        print(prRed("I = Show Inventory"))
        print(prRed("I = Show Inventory"))
        print(prRed("A = Run Inventory Analysis"))
        print(prRed("O = Optimize placement"))
        print(prRed("H = Help"))
        print(prRed("E = Exit"))
        print(prCyan("*******************************************"))

if __name__ == "__main__":
    welcome_screen = WelcomeScreen()
    welcome_screen.colored_characters(welcome_screen.manager)









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