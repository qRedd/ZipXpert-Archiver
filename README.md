# ZipXpert - Aplicație Desktop de Arhivare și Criptare

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-green?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-AES%20Encryption-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

**ZipXpert** este o aplicație desktop modernă și intuitivă, dezvoltată în Python, care permite crearea rapidă de arhive ZIP. Aplicația se distinge prin interfața grafică modernă (Dark Mode) și capacitatea de a securiza arhivele prin criptare cu parolă.

---

## 🚀 Funcționalități Principale

Aplicația a fost proiectată pentru eficiență și securitate, oferind următoarele capabilități:

* **📂 Selecție Flexibilă:** Posibilitatea de a adăuga fișiere individuale sau foldere întregi în lista de arhivare.
* **🔐 Securitate Avansată:** Criptarea arhivelor ZIP folosind parole (implementat via `pyminizip`).
* **🗜️ Compresie Ajustabilă:** Suportă două niveluri de compresie: 'Fără compresie' (rapid) și 'Compresie maximă'.
* **🎨 Interfață Modernă:** Design "Dark Mode" cu accente albastre, construit pe librăria `customtkinter`.
* **✨ Gestiune Listă:** Posibilitatea de a vizualiza și șterge fișierele selectate înainte de procesare.

---

## 🛠️ Tehnologii Utilizate

Proiectul este construit integral în **Python**, utilizând biblioteci standard și externe pentru funcționalități specifice:

| Tehnologie | Descriere |
| :--- | :--- |
| **Python** | Limbajul principal de programare. |
| **CustomTkinter** | Extensie modernă pentru `tkinter`, utilizată pentru UI/UX. |
| **Pyminizip** | Bibliotecă pentru crearea arhivelor criptate cu parolă. |
| **Tkinter** | Biblioteca standard pentru interfața grafică de bază. |
| **Zipfile** | Modul nativ Python pentru manipularea arhivelor standard. |

---

## 💻 Instalare și Rulare

### 1. Cerințe de sistem
Asigurați-vă că aveți instalat **Python 3.x**.

### 2. Instalarea dependențelor
Deschideți terminalul în folderul proiectului și rulați comanda:

```bash
pip install customtkinter pyminizip Pillow
python ZipXpert.py
```

Notă: Pentru a crea un fișier executabil (.exe), se poate utiliza PyInstaller:

```bash
pyinstaller --onefile --add-data "logo.png;." --icon favicon.ico ZipXpert.py
```

📖 Ghid de Utilizare

1. Apăsați Selectează fișiere sau Selectează folder pentru a popula lista de lucru.

2. Alegeți Nivelul de compresie dorit din meniul dropdown.

3. (Opțional) Bifați Adaugă parolă și introduceți cheia de securitate dorită.

4. Apăsați Creează ZIP și alegeți locația de salvare.


## 📸 Structura Proiectului

```text
ZipXpert/
├── ZipXpert.py        # Codul sursă principal
├── logo.png           # Element grafic UI
├── favicon.ico        # Iconița aplicației
├── README.md          # Documentația proiectului
└── .gitignore         # Configurare Git