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

