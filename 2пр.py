import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import platform
import subprocess

def open_browser():
    """Открыть браузер"""
    webbrowser.open("https://google.com")

def open_youtube():
    """Открыть YouTube"""
    webbrowser.open("https://youtube.com")

def open_explorer():
    """Открыть проводник"""
    system = platform.system()
    
    if system == "Windows":
        os.startfile(".")
    elif system == "Darwin":  # macOS
        subprocess.run(["open", "."])
    else:  # Linux и другие
        subprocess.run(["xdg-open", "."])

def restart_computer():
    """Перезагрузить компьютер"""
    if messagebox.askyesno("Подтверждение", "Вы уверены, что хотите перезагрузить компьютер?"):
        system = platform.system()
        
        try:
            if system == "Windows":
                os.system("shutdown /r /t 5")
            elif system == "Darwin":
                subprocess.run(["sudo", "shutdown", "-r", "now"])
            else:  # Linux
                subprocess.run(["sudo", "shutdown", "-r", "now"])
            messagebox.showinfo("Информация", "Компьютер будет перезагружен через 5 секунд")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось перезагрузить компьютер: {e}")

def shutdown_computer():
    """Выключить компьютер"""
    if messagebox.askyesno("Подтверждение", "Вы уверены, что хотите выключить компьютер?"):
        system = platform.system()
        
        try:
            if system == "Windows":
                os.system("shutdown /s /t 5")
            elif system == "Darwin":
                subprocess.run(["sudo", "shutdown", "-h", "now"])
            else:  # Linux
                subprocess.run(["sudo", "shutdown", "-h", "now"])
            messagebox.showinfo("Информация", "Компьютер будет выключен через 5 секунд")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось выключить компьютер: {e}")

def exit_app():
    """Выход из приложения"""
    root.destroy()

# Создание главного окна
root = tk.Tk()
root.title("Панель управления")
root.geometry("400x400")
root.resizable(False, False)

# Стили
button_style = {
    "font": ("Arial", 12),
    "width": 25,
    "height": 2,
    "bd": 2,
    "relief": "raised"
}

# Заголовок
title_label = tk.Label(
    root,
    text="Управление компьютером",
    font=("Arial", 16, "bold"),
    pady=10
)
title_label.pack()

# Кнопки
btn_browser = tk.Button(
    root,
    text="🌐 Открыть браузер",
    command=open_browser,
    bg="#4CAF50",
    fg="white",
    **button_style
)
btn_browser.pack(pady=5)

btn_youtube = tk.Button(
    root,
    text="▶️ Открыть YouTube",
    command=open_youtube,
    bg="#FF0000",
    fg="white",
    **button_style
)
btn_youtube.pack(pady=5)

btn_explorer = tk.Button(
    root,
    text="📁 Открыть проводник",
    command=open_explorer,
    bg="#2196F3",
    fg="white",
    **button_style
)
btn_explorer.pack(pady=5)

btn_restart = tk.Button(
    root,
    text="🔄 Перезагрузить компьютер",
    command=restart_computer,
    bg="#FF9800",
    fg="white",
    **button_style
)
btn_restart.pack(pady=5)

btn_shutdown = tk.Button(
    root,
    text="⏻ Выключить компьютер",
    command=shutdown_computer,
    bg="#F44336",
    fg="white",
    **button_style
)
btn_shutdown.pack(pady=5)

btn_exit = tk.Button(
    root,
    text="❌ Выход",
    command=exit_app,
    bg="#9E9E9E",
    fg="white",
    **button_style
)
btn_exit.pack(pady=20)

# Подсказка в статусной строке
status_label = tk.Label(
    root,
    text="Выберите действие",
    font=("Arial", 10),
    bg="#f0f0f0",
    height=2,
    relief="sunken",
    bd=1
)
status_label.pack(side="bottom", fill="x")

# Запуск приложения
root.mainloop()
