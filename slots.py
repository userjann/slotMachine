import tkinter as tk
from tkinter import messagebox
import random

# Symbols for the slot machine
SYMBOLS = ["🍒", "🔔", "🍋", "⭐", "🍉"]

class SlotMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine")
        self.balance = 100

        # Slot display
        self.slot_labels = [tk.Label(root, text=random.choice(SYMBOLS), font=("Arial", 30)) for _ in range(3)]
        for i, label in enumerate(self.slot_labels):
            label.grid(row=0, column=i, padx=10, pady=10)
        
        # Balance display
        self.balance_label = tk.Label(root, text=f"Credit: {self.balance}€", font=("Arial", 14))
        self.balance_label.grid(row=1, columnspan=3)
        
        # Bet entry field
        self.bet_entry = tk.Entry(root)
        self.bet_entry.grid(row=2, columnspan=3)
        self.bet_entry.insert(0, "10")
        
        # Spin button
        self.spin_button = tk.Button(root, text="Spin", command=self.spin)
        self.spin_button.grid(row=3, columnspan=3, pady=10)

    def update_slots(self, symbols):
        for label, sym in zip(self.slot_labels, symbols):
            label.config(text=sym)
        self.root.update()

    def spin(self):
        try:
            bet = int(self.bet_entry.get())
            if bet <= 0 or bet > self.balance:
                messagebox.showerror("Error", "Invalid bet!")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            return

        self.balance -= bet
        self.balance_label.config(text=f"Credit: {self.balance}CHF")

        # Spinning animation
        for _ in range(10):
            self.update_slots([random.choice(SYMBOLS) for _ in range(3)])
            self.root.after(100)

        # Final result
        final_symbols = [random.choice(SYMBOLS) for _ in range(3)]
        self.update_slots(final_symbols)

        # Winning calculation
        if final_symbols[0] == final_symbols[1] == final_symbols[2]:
            winnings = bet * 5
        elif final_symbols[0] == final_symbols[1] or final_symbols[1] == final_symbols[2] or final_symbols[0] == final_symbols[2]:
            winnings = bet * 2
        else:
            winnings = 0

        self.balance += winnings
        self.balance_label.config(text=f"Credit: {self.balance}CHF")
        
        if winnings > 0:
            messagebox.showinfo("Congratulations!", f"You won {winnings} CHF!")
        elif self.balance == 0:
            messagebox.showwarning("Game Over", "No more money left!")
            self.spin_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachine(root)
    root.mainloop()
