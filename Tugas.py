import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Prediksi Prodi Pilihan")
root.geometry("480x570")
root.resizable(False, False)

frame = ttk.Frame(root, padding=25)
frame.pack(fill="both", expand=True)
frame.columnconfigure(1, weight=1)

judul = ttk.Label(
    frame,
    text="Aplikasi prediksi Prodi Pilihan",
    font=("Arial", 16, "bold"),
    anchor="center"
)
judul.grid(row=0, column=0, columnspan=2, pady=(0, 20))

mata_pelajaran = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Fisika",
    "Kimia",
    "Biologi",
    "Informatika",
    "Ekonomi",
    "Geografi",
    "Sejarah"
]

input_nilai = []

for nomor, pelajaran in enumerate(mata_pelajaran, start=1):
    label = ttk.Label(frame, text=f"{nomor}. {pelajaran}")
    label.grid(row=nomor, column=0, sticky="w", padx=(0, 20), pady=7)

    entry = ttk.Entry(frame, width=20)
    entry.grid(row=nomor, column=1, sticky="ew", pady=7)
    input_nilai.append(entry)

def hasil_prediksi():
    label_hasil.config(text="TeknologiInformasi")

tombol = ttk.Button(
    frame,
    text="Hasil Prediksi",
    command=hasil_prediksi
)
tombol.grid(row=11, column=0, columnspan=2, pady=(20, 15))

label_hasil = ttk.Label(
    frame,
    text="Hasil prediksi akan muncul di sini",
    font=("Arial", 12, "bold"),
    foreground="blue",
    anchor="center"
)
label_hasil.grid(row=12, column=0, columnspan=2, sticky="ew")

root.mainloop()