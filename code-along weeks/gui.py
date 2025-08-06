import tkinter as tk
from tkinter import Frame, Label , Button
from number_entry import IntEntry
import random

def main():
    root = tk.Tk()
    root.option_add('*Font', 'Arial 14')
    frm_main = tk.Frame(root)
    frm_main.master.title("Dice")
    frm_main.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
    setup_main(frm_main)
    frm_main.mainloop()

def setup_main(frm):
    lbl_sides= tk.Label(frm, text="Enter the number of sides on the dice(2-20):")
    lbl_sides.grid(row=0, column=0,padx=3, pady=3)
    ent_sides = IntEntry(frm, width=2, lower_bound=2, upper_bound=20)
    ent_sides.grid(row=0, column=1,padx=3, pady=3)
    lbl_count= tk.Label(frm, text="Enter the number of dice to roll(1-10):")
    lbl_count.grid(row=1, column=0,padx=3, pady=3)
    ent_count = IntEntry(frm, width=2, lower_bound=1, upper_bound=10)
    ent_count.grid(row=1, column=1,padx=3, pady=3)
    btn_roll = Button(frm, text="Roll it!")
    btn_roll.grid(row=2, column=0, columnspan=2, pady=5)
    lbl_roll = tk.Label(frm, text="")
    lbl_roll.grid(row=3, column=0, columnspan=2, pady=5)

    def roll_dice(sides, count):
        sun=0
        roll_text= ""
        for roll in range(count):
            die_roll=random.randint(1, sides)
            sun += die_roll
            roll_text += f"{die_roll} "
        roll_text += f"total {sun}"
        return roll_text

    def roll_action():
        try:
            sides = int(ent_sides.get())
            count = int(ent_count.get())
        except ValueError:
            lbl_roll.config(text="You must enter a valid number of sides and count")
            return
        try:
            count = int(ent_count.get())
            sides = int(ent_sides.get())
        except ValueError:
            lbl_roll.config(text="You must enter a valid number of sides")
            return
        
        
        lbl_text=roll_dice(sides, count)
        lbl_roll.config(text=lbl_text)

    btn_roll.config(command=roll_action)




if __name__ == "__main__":
    main()