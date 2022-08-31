from tkinter import *;
from pynput.keyboard import Key, Listener;
import pyautogui as pg;
import time;

class App:
    def __init__(self, master=None):
        self.keys = [];
        self.btn = Button(master);

        self.btn["text"] = "Começar";
        self.btn.bind("<Button-1>", self.start);

        self.btn.pack();

    def start(self, event):
        with Listener(on_press = self.show) as listener:
            listener.join();

    def show(self, key):
        self.makeAction(key);

    def makeAction(self, key):
        if (len(self.keys) == 2):
            del self.keys[0];
        if (len(self.keys) < 3):
            self.keys.append(key);
        
        try:
            if (self.keys[0] == Key.ctrl_l and self.keys[1].char == "j"):
                self.click();
        except:
            pass

        if (len(self.keys) > 1):
            if (self.keys[0] == Key.esc and self.keys[1] == Key.esc):
                self.keys.clear();
                exit();

    def click(self):
        pg.mouseDown(button="left"); time.sleep(0.9); pg.mouseUp();

root = Tk();
App(root);
root.mainloop();
