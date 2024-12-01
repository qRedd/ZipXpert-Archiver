import os
import tkinter.filedialog
import tkinter.messagebox
from zipfile import ZipFile, ZIP_STORED, ZIP_DEFLATED
import customtkinter as ctk
import pyminizip  # Pentru suportul parolelor

# Setarea modului întunecat și temei implicite
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Funcție pentru selectarea fișierelor (se pot selecta fișiere multiple)
def select_files():
    files = tkinter.filedialog.askopenfilenames(title="Selectează fișierele pentru arhivă")
    if files:
        add_files_to_list(files)
    else:
        tkinter.messagebox.showwarning("Selecție fișiere", "Nu ai selectat niciun fișier!")

# Funcție pentru selectarea unui folder
def select_folder():
    folder = tkinter.filedialog.askdirectory(title="Selectează un folder pentru arhivă")
    if folder:
        files = []
        for root_dir, _, filenames in os.walk(folder):
            for filename in filenames:
                files.append(os.path.join(root_dir, filename))
        add_files_to_list(files)
    else:
        tkinter.messagebox.showwarning("Selecție folder", "Nu ai selectat niciun folder!")

# Funcție pentru adăugarea fișierelor selectate în lista afișată
def add_files_to_list(files):
    for file in files:
        if file not in file_list:  # Evităm adăugarea duplicatelor
            file_list.append(file)
            file_label = ctk.CTkLabel(file_frame, text=file, anchor="w")
            file_label.pack(fill="x", padx=5, pady=2)

# Funcție pentru ștergerea fișierelor selectate
def clear_file_list():
    global file_list
    file_list = []
    for widget in file_frame.winfo_children():
        widget.destroy()

# Funcție pentru crearea fișierului ZIP
def create_zip():
    if not file_list:
        tkinter.messagebox.showwarning("Selecție fișiere", "Nu ai selectat fișiere pentru arhivă!")
        return

    # Selectează locația de salvare pentru arhiva ZIP
    zip_path = tkinter.filedialog.asksaveasfilename(defaultextension=".zip",
                                                    filetypes=[("ZIP files", "*.zip")],
                                                    title="Salvează arhiva ZIP")
    if not zip_path:
        tkinter.messagebox.showwarning("Salvare fișier", "Nu ai specificat un nume pentru fișierul ZIP!")
        return

    # Determinăm nivelul de compresie ales
    compression = compression_level.get()
    if compression == "Fără compresie (rapid)":
        compression_method = ZIP_STORED
    else:
        compression_method = ZIP_DEFLATED

    # Crearea arhivei ZIP
    if password_var.get():
        # Dacă există o parolă, folosim pyminizip
        try:
            password = password_entry.get()
            if not password:
                tkinter.messagebox.showwarning("Parolă lipsă", "Introduceți o parolă pentru arhivă!")
                return

            pyminizip.compress_multiple(file_list, [], zip_path, password, compression_method)
            tkinter.messagebox.showinfo("Succes", f"Arhivarea cu parolă s-a efectuat cu succes la {zip_path}")
        except Exception as e:
            tkinter.messagebox.showerror("Eroare", f"A apărut o eroare: {e}")
    else:
        try:
            with ZipFile(zip_path, 'w', compression=compression_method) as zip_file:
                for file in file_list:
                    zip_file.write(file, arcname=os.path.basename(file))
            tkinter.messagebox.showinfo("Succes", f"Arhivarea s-a efectuat cu succes la {zip_path}")
        except Exception as e:
            tkinter.messagebox.showerror("Eroare", f"A apărut o eroare: {e}")

# Configurarea interfeței grafice
root = ctk.CTk()
root.title("Creare fișier ZIP")
root.geometry("600x650")

file_list = []

# Titlu principal
title_label = ctk.CTkLabel(root, text="Creare fișier ZIP", font=ctk.CTkFont(size=24, weight="bold"))
title_label.pack(pady=20)

# Frame scrollabil pentru lista fișierelor
file_frame = ctk.CTkScrollableFrame(root, width=500, height=200)
file_frame.pack(pady=10)

# Butoane pentru selectarea fișierelor și folderelor
select_files_button = ctk.CTkButton(root, text="Selectează fișiere", command=select_files, width=200)
select_files_button.pack(pady=5)

select_folder_button = ctk.CTkButton(root, text="Selectează folder", command=select_folder, width=200)
select_folder_button.pack(pady=5)

# Buton pentru ștergerea fișierelor selectate
clear_button = ctk.CTkButton(root, text="Șterge fișierele selectate", command=clear_file_list, width=200)
clear_button.pack(pady=5)

# Opțiunea de selectare a nivelului de compresie
compression_label = ctk.CTkLabel(root, text="Nivel de compresie:", font=ctk.CTkFont(size=14))
compression_label.pack(pady=10)

compression_level = ctk.StringVar(value="Fără compresie (rapid)")
compression_dropdown = ctk.CTkComboBox(root, values=["Fără compresie (rapid)", "Compresie maximă"],
                                       variable=compression_level, state="readonly", width=300)
compression_dropdown.pack(pady=5)

# Opțiunea de parolă
password_var = ctk.BooleanVar(value=False)
password_checkbox = ctk.CTkCheckBox(root, text="Adaugă parolă", variable=password_var)
password_checkbox.pack(pady=10)

password_entry = ctk.CTkEntry(root, placeholder_text="Introduceți parola", show="*")
password_entry.pack(pady=5)

# Buton pentru crearea arhivei ZIP
zip_button = ctk.CTkButton(root, text="Creează ZIP", command=create_zip, width=200, fg_color="green")
zip_button.pack(pady=20)

# Eliminarea label-ului de subsol
#footer_label = ctk.CTkLabel(root, text="Un proiect modern de comprimare", font=ctk.CTkFont(size=12))
#footer_label.pack(side="bottom", pady=10)

# Rularea aplicației
root.mainloop()

