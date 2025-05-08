import tkinter as tk
from tkinter import messagebox

class MarvelTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Marvel Rivals Tracker Final")
        self.stats = {}

        self.characters = ["Spider-Man", "Magneto", "Hulk", "Iron Man", "Storm", "Loki", "Black Panther","Hela"]

        # Character selection
        self.selected_char = tk.StringVar()
        self.selected_char.set(self.characters[0])
        tk.Label(root, text="Choose Character:").pack(pady=(10, 50))
        tk.OptionMenu(root, self.selected_char, *self.characters).pack()

        # Notes
        tk.Label(root, text="Match Notes (optional):").pack(pady=(10, 50))
        self.notes_entry = tk.Entry(root, width=40)
        self.notes_entry.pack(pady=(0, 10))

        # Win/Loss buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Win", width=10, command=self.log_win).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Loss", width=10, command=self.log_loss).pack(side=tk.LEFT, padx=5)

        # Show Stats button
        tk.Button(root, text="Show Stats", command=self.show_stats).pack(pady=10)

    def log_match(self, result):
        char = self.selected_char.get()
        note = self.notes_entry.get().strip()

        if char not in self.stats:
            self.stats[char] = {"wins": 0, "losses": 0, "notes": []}

        if result == "win":
            self.stats[char]["wins"] += 1
        else:
            self.stats[char]["losses"] += 1

        if note:
            self.stats[char]["notes"].append(note)
            self.notes_entry.delete(0, tk.END)

        messagebox.showinfo("Logged", f"{result.capitalize()} recorded for {char}!")

    def log_win(self):
        self.log_match("win")

    def log_loss(self):
        self.log_match("loss")

    def show_stats(self):
        if not self.stats:
            messagebox.showinfo("Stats Summary", "No match data recorded yet.")
            return

        msg = ""
        for char, data in self.stats.items():
            total = data["wins"] + data["losses"]
            win_rate = (data["wins"] / total) * 100 if total else 0
            msg += f"{char}: {data['wins']}W / {data['losses']}L - Win Rate: {win_rate:.1f}%\n"
            if data["notes"]:
                msg += "  Notes:\n"
                for note in data["notes"]:
                    msg += f"   - {note}\n"
            msg += "\n"

        messagebox.showinfo("Stats Summary", msg)

if __name__ == "__main__":
    root = tk.Tk()
    app = MarvelTrackerGUI(root)
    root.mainloop()