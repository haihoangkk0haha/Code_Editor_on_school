# Code editor app
import tkinter as tk
class Edit:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("NotePad")
        self.win.geometry("500x500")
        self.main()
    
    def build_fe(self):
        self.code_in = tk.Entry(
            self.win,
            font=("Cascadia Mono", 16),
        )
        self.code_in.pack(fill="x")
    def main(self):
        self.build_fe()
    def run(self):
        self.win.mainloop()

if __name__ == "__main__":
    editor = Edit()
    editor.run()