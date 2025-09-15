# 🔐 Password Manager GUI App

A simple yet powerful password manager built with Python and Tkinter.  
This project is part of the 100 Days of Code: The Complete Python Bootcamp by Angela Yu.  

The app allows you to generate secure passwords, save them locally, and quickly retrieve credentials for different websites.

---

## 📌 Features
- **Graphical User Interface (GUI)** built with Tkinter.
- **Secure Password Generator** with letters, numbers, and symbols.
- **Clipboard Copying** – automatically copies newly generated passwords for convenience.
- **Data Storage** – saves website credentials (Website, Email/Username, Password) into a local text file.
- **User-Friendly Design** – simple input fields and buttons for quick interaction.

---

## 🖼️ Screenshots

<img width="569" height="467" alt="Capture-pass0" src="https://github.com/user-attachments/assets/21db3434-72f2-46a8-83d1-73cc863217d0" />

<img width="574" height="469" alt="Capture-pass01" src="https://github.com/user-attachments/assets/81c45fa6-6f39-4d9f-bb84-046be37a8456" />

<img width="571" height="471" alt="Capture-pass02" src="https://github.com/user-attachments/assets/359805f8-8a7e-4052-8b08-9785e4f6be58" />

<img width="575" height="470" alt="Capture-pass03" src="https://github.com/user-attachments/assets/f7e3a46f-2a2f-4454-af47-1f7cfa60fb9c" />

---

## 🖥️ Tech Stack
- **Python 3**
- **Tkinter** (for GUI)
- **pyperclip** (to copy password to clipboard)
- **random** & **string** modules (for password generation)

---

## 📂 Project Structure
📁 password-manager-gui-app
│── main.py            # Main application script
│── data.txt           # Stores saved credentials (auto-created)
│── screenshots/       # Folder for images (create manually)
│── README.md          # Project documentation


---

## 🚀 How to Run
1. Make sure you have **Python 3.x** installed.
2. Install the required dependency:
   ```bash
   pip install pyperclip
3. Run the app:
   ```bash
   python main.py

## 🛠️ Usage

1. Enter the **Website**, **Email/Username**, and **Password**.
2. Click **Generate Password** to create a strong random password.

   * It will automatically copy to your clipboard.
3. Click **Add** to save the credentials into `data.txt`.

---

## 📖 Example `data.txt` entry

```
Website: github.com | Email: user@example.com | Password: 9@LmZ7!kA2
```

---

## ✨ Future Improvements

* Add search functionality to retrieve stored credentials quickly.
* Store passwords in JSON or a database instead of plain text.
* Encrypt stored passwords for extra security.
* Add a password strength indicator.
