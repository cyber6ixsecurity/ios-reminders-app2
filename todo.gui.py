import tkinter as tk

# --- Colors (NovaCurve style) ---
BG_COLOR = "#0f0f14"
CARD_COLOR = "#1c1c24"
ACCENT = "#7c5cff"
TEXT = "#ffffff"
SUBTEXT = "#a1a1aa"

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, "  " + task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except:
        pass

# --- Window ---
window = tk.Tk()
window.title("NovaTasks")
window.geometry("360x500")
window.configure(bg=BG_COLOR)

# --- Header ---
header = tk.Label(
    window,
    text="NovaTasks",
    font=("Helvetica", 20, "bold"),
    fg=TEXT,
    bg=BG_COLOR
)
header.pack(pady=(20, 10))

subheader = tk.Label(
    window,
    text="Stay organized. Stay focused.",
    font=("Helvetica", 10),
    fg=SUBTEXT,
    bg=BG_COLOR
)
subheader.pack(pady=(0, 20))

# --- Card Frame ---
card = tk.Frame(window, bg=CARD_COLOR)
card.pack(padx=20, pady=10, fill="both", expand=True)

# --- Input ---
entry = tk.Entry(
    card,
    font=("Helvetica", 12),
    bg="#2a2a35",
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat"
)
entry.pack(padx=15, pady=(15, 10), fill="x", ipady=8)

# --- Buttons ---
button_frame = tk.Frame(card, bg=CARD_COLOR)
button_frame.pack(padx=15, pady=5, fill="x")

add_btn = tk.Button(
    button_frame,
    text="Add",
    bg=ACCENT,
    fg="white",
    relief="flat",
    command=add_task
)
add_btn.pack(side="left", expand=True, fill="x", padx=(0,5), ipady=6)

delete_btn = tk.Button(
    button_frame,
    text="Delete",
    bg="#ff4d4d",
    fg="white",
    relief="flat",
    command=delete_task
)
delete_btn.pack(side="left", expand=True, fill="x", padx=(5,0), ipady=6)

# --- Task List ---
listbox = tk.Listbox(
    card,
    bg=CARD_COLOR,
    fg=TEXT,
    font=("Helvetica", 12),
    selectbackground=ACCENT,
    relief="flat"
)
listbox.pack(padx=15, pady=15, fill="both", expand=True)

# --- Run ---
window.mainloop()