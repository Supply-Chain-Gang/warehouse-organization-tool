import threading
import os
import time
import sys
import random

class WelcomeScreen:
    def __init__(self):
        self.pipe = []
        self.slash = []
        self.u_score = []
        self.manager = list(open("warehouse_organization_tool/utilities/welcome_screen/pattern.txt").read().rstrip())

    def colored_characters(self, color, char):
        if color == "red":
            return f'\033[91m{char}\033[0m'
        if color == "green":
            return f'\033[92m{char}\033[0m'
        if color == "blue":
            return f'\033[94m{char}\033[0m'

    def twinkle(self, char, indexes, color):
        mutex = threading.Lock()
        off = True
        while True:
            for idx in indexes:
                self.manager[idx] = self.colored_characters(color, char) if off else self.manager[idx]
            mutex.acquire()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(''.join(self.manager))
            mutex.release()
            off = not off
            time.sleep(random.uniform(.5, 1.5))
            #need to exit out of loop with keyboard inputs
            #but not exit program
            #go back into loop if re-enter main menu

    def all_characters(self):
        pipes = random.sample(self.pipe, len(self.pipe)// 2)
        slash = random.sample(self.slash, len(self.slash)// 2)
        u_score = random.sample(self.u_score, len(self.u_score)// 2)

        for i, c in enumerate(self.manager):
            if c == "|":
                self.pipe.append(i)
            if c == "/":
                self.slash.append(i)
            if c == "_":
                self.u_score.append(i)

        tp = threading.Thread(target=self.twinkle, args=("|", pipes, "red" ))
        ts = threading.Thread(target=self.twinkle, args=("/", slash, "green" ))
        tu = threading.Thread(target=self.twinkle, args=("_", u_score, "blue" ))

        for t in [tp, ts, tu]:
            t.start()
        for t in [tp, ts, tu]:
            t.join()

if __name__ == "__main__":
    welcome_screen = WelcomeScreen()
    welcome_screen.all_characters()