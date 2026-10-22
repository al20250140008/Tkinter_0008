import tkinter as tk
from tkinter import ttk

# Daftar 10 mata kuliah semester
MAPEL = [
    "Administrasi Basis Data",
    "Implementasi Basis Data",
    "Bahasa Inggris",
    "Teknologi Server",
    "Dasar Jaringan",
    "Manajemen Proyek",
    "Pemrograman Multiplatform",
    "Probabilitas dan Statistika",
    "Switching dan Wireless",
    "Perancangan Berbasis Objek",
]


def hasil_prediksi():
    # Apapun input yang diberikan, hasilnya selalu Teknologi Informasi
    label_hasil.config(text="Teknologi Informasi")


# ===== Jendela utama =====
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("480x540")
root.resizable(False, False)

# ===== Label judul =====
label_judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold"),
)
label_judul.pack(pady=15)

# ===== Frame input nilai =====
frame_input = tk.Frame(root)
frame_input.pack(pady=5)

entries = []
for i, nama in enumerate(MAPEL):
    tk.Label(frame_input, text=f"{nama} :", font=("Arial", 11), anchor="w", width=26).grid(
        row=i, column=0, padx=10, pady=4, sticky="w"
    )
    