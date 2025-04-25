# File: 120140086_Challenge.py
# Author: Reza Chairul Manam
# NIM: 120140086
# Class: Praktikum PBO-RC
#===================================================================================================
# Challenge:
import tkinter as tk
from tkinter import messagebox, Menu, Scrollbar
from datetime import datetime
import json
import os

# Struktur data: list of dict
catatan = []

# File untuk menyimpan data
FILE_JSON = "catatan.json"

def simpan_catatan():
    with open(FILE_JSON, "w") as f:
        json.dump(catatan, f)

def muat_catatan():
    if os.path.exists(FILE_JSON):
        with open(FILE_JSON, "r") as f:
            data = json.load(f)
            for item in data:
                catatan.append(item)
                listbox.insert(tk.END, f"{item['judul']} ({item['waktu']})")

def tambah_catatan():
    judul = entry_judul.get().strip()
    isi = text_isi.get("1.0", tk.END).strip()
    waktu = datetime.now().strftime("%d-%m-%Y %H:%M")
    if not judul or not isi:
        messagebox.showerror("Error", "Judul dan isi tidak boleh kosong!")
        return
    catatan.append({"judul": judul, "isi": isi, "waktu": waktu})
    listbox.insert(tk.END, f"{judul} ({waktu})")
    entry_judul.delete(0, tk.END)
    text_isi.delete("1.0", tk.END)

def tampilkan_catatan(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        isi = catatan[index]["isi"]
        text_isi.config(state=tk.NORMAL)
        text_isi.delete("1.0", tk.END)
        text_isi.insert(tk.END, isi)
        text_isi.config(state=tk.DISABLED)

def hapus_catatan():
    selection = listbox.curselection()
    if not selection:
        return
    index = selection[0]
    konfirmasi = messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus catatan ini?")
    if konfirmasi:
        listbox.delete(index)
        catatan.pop(index)
        text_isi.config(state=tk.NORMAL)
        text_isi.delete("1.0", tk.END)

def edit_catatan():
    selection = listbox.curselection()
    if not selection:
        return
    index = selection[0]
    new_judul = entry_judul.get().strip()
    new_isi = text_isi.get("1.0", tk.END).strip()
    if not new_judul or not new_isi:
        messagebox.showerror("Error", "Judul dan isi tidak boleh kosong!")
        return
    catatan[index]["judul"] = new_judul
    catatan[index]["isi"] = new_isi
    listbox.delete(index)
    waktu = catatan[index]["waktu"]
    listbox.insert(index, f"{new_judul} ({waktu})")

def keluar():
    simpan_catatan()
    root.destroy()

def tentang():
    messagebox.showinfo("Tentang", "Catatan Harian v1.0\nDibuat dengan Tkinter")

# Inisialisasi GUI
root = tk.Tk()
root.title("Catatan Harian")

# Menu bar
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Keluar", command=keluar)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Tentang", command=tentang)
menu_bar.add_cascade(label="Bantuan", menu=help_menu)
root.config(menu=menu_bar)

# Input Judul
tk.Label(root, text="Judul:").grid(row=0, column=0, sticky="w", padx=5)
entry_judul = tk.Entry(root, width=40)
entry_judul.grid(row=0, column=1, columnspan=3, sticky="we", padx=5, pady=5)

# Tombol
btn_tambah = tk.Button(root, text="Tambah Catatan", command=tambah_catatan)
btn_tambah.grid(row=1, column=1, sticky="we", padx=5)
btn_edit = tk.Button(root, text="Edit Catatan", command=edit_catatan)
btn_edit.grid(row=1, column=2, sticky="we", padx=5)
btn_hapus = tk.Button(root, text="Hapus Catatan", command=hapus_catatan)
btn_hapus.grid(row=1, column=3, sticky="we", padx=5)

# Listbox + Scrollbar
listbox = tk.Listbox(root, width=40, height=15)
listbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
scrollbar = Scrollbar(root, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.grid(row=2, column=2, sticky="nsw")
listbox.config(yscrollcommand=scrollbar.set)

# Text area
text_isi = tk.Text(root, width=40, height=15, state=tk.DISABLED)
text_isi.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

# Event
listbox.bind("<<ListboxSelect>>", tampilkan_catatan)
root.protocol("WM_DELETE_WINDOW", keluar)

# Layout growable
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_rowconfigure(2, weight=1)

# Muat catatan jika ada
muat_catatan()

# Jalankan aplikasi
root.mainloop()
