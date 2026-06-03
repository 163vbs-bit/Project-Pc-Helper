import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import platform
import subprocess
import sys

class SystemControlPanel:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()
        self.setup_bindings()
        
    def setup_window(self):
        """Настройка окна"""
        self.root.title("🚀 System Control Panel")
        self.root.geometry("800x500")
        
        # Стили
        self.bg_color = '#2b2b2b'
        self.btn_color = '#3c3c3c'
        self.text_color = '#ffffff'
        self.highlight_color = '#4a90e2'
        
        self.root.configure(bg=self.bg_color)
        
    def create_widgets(self):
        """Создание всех элементов интерфейса"""
        # Заголовок
        title_frame = tk.Frame(self.root, bg=self.bg_color)
        title_frame.pack(pady=20)
        
        tk.Label(title_frame, text="⚡ SYSTEM CONTROL PANEL", 
                font=("Arial", 20, "bold"),
                bg=self.bg_color, fg=self.highlight_color).pack()
        
        tk.Label(title_frame, text="Быстрый доступ к системным функциям",
                font=("Arial", 10),
                bg=self.bg_color, fg=self.text_color).pack(pady=5)
        
        # Основные кнопки
        self.create_buttons()
        
        # Информация о системе
        self.create_system_info()
        
    def create_buttons(self):
        """Создание кнопок управления"""
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        # Первый ряд
        row1 = tk.Frame(button_frame, bg=self.bg_color)
        row1.pack(pady=10)
        
        buttons_row1 = [
            ("🌐 Открыть браузер", self.open_browser, '#4CAF50'),
            ("📺 Открыть YouTube", self.open_youtube, '#FF0000'),
            ("📁 Открыть проводник", self.open_explorer, '#2196F3'),
        ]
        
        for text, command, color in buttons_row1:
            btn = tk.Button(row1, text=text, command=command,
                          bg=color, fg='white', font=("Arial", 11, "bold"),
                          padx=20, pady=10, relief='raised', bd=2,
                          cursor='hand2')
            btn.pack(side='left', padx=10)
            
        # Второй ряд
        row2 = tk.Frame(button_frame, bg=self.bg_color)
        row2.pack(pady=10)
        
        buttons_row2 = [
            ("⏻ Выключить компьютер", self.shutdown_computer, '#F44336'),
            ("🔄 Перезагрузить компьютер", self.restart_computer, '#FF9800'),
            ("🚪 Выход из программы", self.exit_app, '#9E9E9E'),
        ]
        
        for text, command, color in buttons_row2:
            btn = tk.Button(row2, text=text, command=command,
                          bg=color, fg='white', font=("Arial", 11, "bold"),
                          padx=20, pady=10, relief='raised', bd=2,
                          cursor='hand2')
            btn.pack(side='left', padx=10)
            
        # Дополнительные функции
        row3 = tk.Frame(button_frame, bg=self.bg_color)
        row3.pack(pady=20)
        
        buttons_row3 = [
            ("📝 Блокнот", self.open_notepad, '#9C27B0'),
            ("🧮 Калькулятор", self.open_calculator, '#009688'),
            ("🐱 GitHub", self.open_github, '#333333'),
        ]
        
        for text, command, color in buttons_row3:
            btn = tk.Button(row3, text=text, command=command,
                          bg=color, fg='white', font=("Arial", 10),
                          padx=15, pady=8, relief='raised', bd=1,
                          cursor='hand2')
            btn.pack(side='left', padx=5)
    
    def create_system_info(self):
        """Информация о системе"""
        info_frame = tk.Frame(self.root, bg=self.bg_color)
        info_frame.pack(pady=20)
        
        sys_info = f"Система: {platform.system()} {platform.release()}\n"
        sys_info += f"Python: {platform.python_version()}\n"
        sys_info += f"Процессор: {platform.processor()[:30]}..."
        
        tk.Label(info_frame, text=sys_info, 
                font=("Courier", 9),
                bg=self.bg_color, fg='#aaaaaa',
                justify='left').pack()
        
        # Статус бар
        status_frame = tk.Frame(self.root, bg='#1a1a1a', height=30)
        status_frame.pack(side='bottom', fill='x')
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(status_frame, text="Готов к работе", 
                                     font=("Arial", 9),
                                     bg='#1a1a1a', fg='#4CAF50')
        self.status_label.pack(side='left', padx=10)
        
        tk.Label(status_frame, text=f"Админ: {'Да' if self.is_admin() else 'Нет'}",
                font=("Arial", 9),
                bg='#1a1a1a', fg='#FF9800').pack(side='right', padx=10)
    
    def setup_bindings(self):
        """Настройка горячих клавиш"""
        self.root.bind('<Control-b>', lambda e: self.open_browser())
        self.root.bind('<Control-y>', lambda e: self.open_youtube())
        self.root.bind('<Control-q>', lambda e: self.exit_app())
        self.root.bind('<Escape>', lambda e: self.exit_app())
    
    def is_admin(self):
        """Проверка прав администратора"""
        try:
            if platform.system() == "Windows":
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
            else:
                return os.geteuid() == 0
        except:
            return False
    
    # === ОСНОВНЫЕ ФУНКЦИИ ===
    
    def open_browser(self):
        """Открыть браузер"""
        try:
            webbrowser.open("https://www.google.com")
            self.show_status("Браузер открыт")
        except Exception as e:
            self.show_error(f"Ошибка: {e}")
    
    def open_youtube(self):
        """Открыть YouTube"""
        try:
            webbrowser.open("https://www.youtube.com")
            self.show_status("YouTube открыт")
        except Exception as e:
            self.show_error(f"Ошибка: {e}")
    
    def open_explorer(self):
        """Открыть проводник"""
        try:
            if platform.system() == "Windows":
                os.startfile(".")
            elif platform.system() == "Darwin":
                subprocess.Popen(["open", "."])
            else:
                subprocess.Popen(["xdg-open", "."])
            self.show_status("Проводник открыт")
        except Exception as e:
            self.show_error(f"Ошибка: {e}")
    
    def shutdown_computer(self):
        """Выключить компьютер"""
        if not self.is_admin():
            self.show_warning("Требуются права администратора!")
            return
            
        if messagebox.askyesno("Подтверждение", 
                              "Вы уверены, что хотите выключить компьютер?\n"
                              "Все несохраненные данные будут потеряны!"):
            try:
                if platform.system() == "Windows":
                    os.system("shutdown /s /t 5")
                    self.show_status("Компьютер выключится через 5 секунд")
                    messagebox.showinfo("Выключение", 
                                      "Компьютер будет выключен через 5 секунд")
                elif platform.system() == "Darwin":
                    subprocess.Popen(["sudo", "shutdown", "-h", "now"])
                else:
                    subprocess.Popen(["sudo", "shutdown", "-h", "now"])
            except Exception as e:
                self.show_error(f"Ошибка: {e}")
    
    def restart_computer(self):
        """Перезагрузить компьютер"""
        if not self.is_admin():
            self.show_warning("Требуются права администратора!")
            return
            
        if messagebox.askyesno("Подтверждение", 
                              "Вы уверены, что хотите перезагрузить компьютер?\n"
                              "Все несохраненные данные будут потеряны!"):
            try:
                if platform.system() == "Windows":
                    os.system("shutdown /r /t 5")
                    self.show_status("Перезагрузка через 5 секунд")
                    messagebox.showinfo("Перезагрузка", 
                                      "Компьютер перезагрузится через 5 секунд")
                elif platform.system() == "Darwin":
                    subprocess.Popen(["sudo", "shutdown", "-r", "now"])
                else:
                    subprocess.Popen(["sudo", "shutdown", "-r", "now"])
            except Exception as e:
                self.show_error(f"Ошибка: {e}")
    
    def exit_app(self):
        """Выйти из программы"""
        if messagebox.askyesno("Выход", "Закрыть программу?"):
            self.root.destroy()
    
    # === ДОПОЛНИТЕЛЬНЫЕ ФУНКЦИИ ===
    
    def open_notepad(self):
        """Открыть блокнот"""
        try:
            if platform.system() == "Windows":
                os.system("notepad")
            elif platform.system() == "Darwin":
                subprocess.Popen(["open", "-a", "TextEdit"])
            else:
                subprocess.Popen(["gedit"])
            self.show_status("Блокнот открыт")
        except Exception as e:
            self.show_error(f"Ошибка: {e}")
    
    def open_calculator(self):
        """Открыть калькулятор"""
        try:
            if platform.system() == "Windows":
                os.system("calc")
            elif platform.system() == "Darwin":
                subprocess.Popen(["open", "-a", "Calculator"])
            else:
                subprocess.Popen(["gnome-calculator"])
            self.show_status("Калькулятор открыт")
        except Exception as e:
            self.show_error(f"Ошибка: {e}")
    
    def open_github(self):
        """Открыть GitHub"""
        try:
            webbrowser.open("https://github.com")
            self.show_status("GitHub открыт")
        except Exception as e:
            self.show_error(f"Ошибка: {e}")
    
    # === УТИЛИТЫ ===
    
    def show_status(self, message):
        """Показать статус"""
        print(f"[STATUS] {message}")
        if hasattr(self, "status_label"):
            self.status_label.config(text=message, fg='#4CAF50')
    
    def show_error(self, message):
        """Показать ошибку"""
        print(f"[ERROR] {message}")
        if hasattr(self, "status_label"):
            self.status_label.config(text=message, fg='#F44336')
        messagebox.showerror("Ошибка", message)
    
    def show_warning(self, message):
        """Показать предупреждение"""
        print(f"[WARNING] {message}")
        if hasattr(self, "status_label"):
            self.status_label.config(text=message, fg='#FF9800')
        messagebox.showwarning("Предупреждение", message)

def check_admin():
    """Проверка и запрос прав администратора"""
    if platform.system() == "Windows":
        try:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if not is_admin:
                print("Запрашиваю права администратора...")
                ctypes.windll.shell32.ShellExecuteW(
                    None, "runas", sys.executable, " ".join(sys.argv), None, 1
                )
                return False
        except:
            pass
    return True

def main():
    """Главная функция"""
    # Проверяем права администратора
    if not check_admin():
        return
    
    # Создаем окно
    root = tk.Tk()
    
    # Создаем приложение
    app = SystemControlPanel(root)
    
    # Центрируем окно
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    # Запускаем
    root.mainloop()

if __name__ == "__main__":
    main()
