import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class NoteTakingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note-taking App")

        self.text_editor = tk.Text(root)
        self.text_editor.pack()

        self.save_button = ttk.Button(root, text="Save Note", command=self.save_note)
        self.save_button.pack()

        self.note_listbox = tk.Listbox(root)
        self.note_listbox.pack()

        self.load_button = ttk.Button(root, text="Load Note", command=self.load_note)
        self.load_button.pack()

    def save_note(self):
        note_content = self.text_editor.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(note_content)
            self.update_note_list(file_path)

    def load_note(self):
        selected_note = self.note_listbox.get(tk.ACTIVE)
        with open(selected_note, "r") as file:
            note_content = file.read()
            self.text_editor.delete("1.0", tk.END)
            self.text_editor.insert(tk.END, note_content)

    def update_note_list(self, new_note_path):
        self.note_listbox.insert(tk.END, new_note_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteTakingApp(root)
    root.mainloop()
