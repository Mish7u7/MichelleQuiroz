import tkinter as tk
from tkinter import messagebox

class ClickCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador de Clics")
        self.click_count = 0
        self.time_left = 30
        self.timer_running = False

        self.click_label = tk.Label(root, text="Clics: 0", font=("Helvetica", 16))
        self.click_label.pack(pady=10)

        self.time_label = tk.Label(root, text="Tiempo restante: 30", font=("Helvetica", 16))
        self.time_label.pack(pady=10)

        self.click_button = tk.Button(root, text="Haz clic en mí", font=("Helvetica", 16), command=self.increment_clicks)
        self.click_button.pack(pady=20)


        self.start_timer()

    def increment_clicks(self):
        if self.timer_running:
            self.click_count += 1
            self.click_label.config(text=f"Clics: {self.click_count}")

    def start_timer(self):
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Tiempo restante: {self.time_left}")
            self.root.after(1000, self.update_timer)
        else:
            self.time_label.config(text="Tiempo agotado")
            self.click_button.config(state=tk.DISABLED)
            self.timer_running = False
            self.show_final_count()

    def show_final_count(self):
        messagebox.showinfo("Resultado Final", f"Número total de clics: {self.click_count}")

root = tk.Tk()
app = ClickCounterApp(root)
root.mainloop()
