import keygen
import sign
import verif

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb


class SenderWindow:
    def __init__(self, receiver=None):

        self.window = tk.Tk()
        self.window.title("Отправитель")
        self.window.geometry("400x600")
        self.receiver = receiver

        # Создаем фрейм для коэффициентов
        coef_frame = ttk.LabelFrame(self.window, text="Коэффициенты")
        coef_frame.pack(padx=10, pady=5, fill="x")

        # Создаем метки и поля для коэффициентов
        coefficients = ['p', 'a - коэф. элипт. кривой', 'b - коэф. элипт. кривой', 'q - порядок подгруппы точек', 'd - закрытый ключ', 'Q - открытый ключ', 'P - точка эллиптической кривой порядка q', '(r, s) - подпись']
        self.coef_entries = {}

        for coef in coefficients:
            frame = ttk.Frame(coef_frame)
            frame.pack(fill="x", padx=5, pady=2)

            ttk.Label(frame, text=f"{coef}:").pack(side="left")
            entry = ttk.Entry(frame)
            entry.pack(side="left", fill="x", expand=True)
            self.coef_entries[coef] = entry

        # Создаем кнопки
        buttons_frame = ttk.Frame(self.window)
        buttons_frame.pack(padx=10, pady=5, fill="x")

        ttk.Button(buttons_frame, text="Сформировать ключи",
                   command=self.generate_keys).pack(fill="x", pady=2)
        ttk.Button(buttons_frame, text="Подписать",
                   command=self.sign).pack(fill="x", pady=2)
        ttk.Button(buttons_frame, text="Отправить",
                   command=self.send).pack(fill="x", pady=2)

        # Создаем текстовое поле
        ttk.Label(self.window, text="Сообщение:").pack(padx=10)
        self.message_text = tk.Text(self.window, height=5)
        self.message_text.pack(padx=10, pady=5, fill="x")

    def update_coefficient(self, coef_name, value):
        """Обновляет значение в поле ввода коэффициента"""
        if coef_name in self.coef_entries:
            # Очищаем текущее значение
            self.coef_entries[coef_name].delete(0, tk.END)
            # Вставляем новое значение
            self.coef_entries[coef_name].insert(0, str(value))

    def generate_keys(self):
        p, a, b, q, xp, yp, d, xq, yq = keygen.keygen()
        self.update_coefficient('p', p)
        self.update_coefficient('a - коэф. элипт. кривой', a)
        self.update_coefficient('b - коэф. элипт. кривой', b)
        self.update_coefficient('q - порядок подгруппы точек', q)
        self.update_coefficient('d - закрытый ключ', d)
        self.update_coefficient('Q - открытый ключ', (xq, yq))
        self.update_coefficient('P - точка эллиптической кривой порядка q', (xp, yp))

    def sign(self):
        message = self.message_text.get("1.0", tk.END).strip()
        if message == '':
            mb.showerror("Ошибка",
                         "Вы ввели пустое сообщение")
        else:
            d = int(self.coef_entries['d - закрытый ключ'].get())
            q = int(self.coef_entries['q - порядок подгруппы точек'].get())
            xp = int(self.coef_entries['P - точка эллиптической кривой порядка q'].get().rstrip(')').lstrip('(').split(',')[0])
            yp = int(self.coef_entries['P - точка эллиптической кривой порядка q'].get().rstrip(')').lstrip('(').split(',')[1])
            a = int(self.coef_entries['a - коэф. элипт. кривой'].get())
            p = int(self.coef_entries['p'].get())

            r, s = sign.sign(d, message, q, xp, yp, a, p)

            self.update_coefficient('(r, s) - подпись', (r, s))
    def send(self):
        data = {
            'p': self.coef_entries['p'].get(),
            'a - коэф. элипт. кривой': self.coef_entries['a - коэф. элипт. кривой'].get(),
            'b - коэф. элипт. кривой': self.coef_entries['b - коэф. элипт. кривой'].get(),
            'q - порядок подгруппы точек': self.coef_entries['q - порядок подгруппы точек'].get(),
            'Q - открытый ключ': self.coef_entries['Q - открытый ключ'].get(),
            'P - точка эллиптической кривой порядка q': self.coef_entries['P - точка эллиптической кривой порядка q'].get(),
            '(r, s) - подпись': self.coef_entries['(r, s) - подпись'].get()
        }
        message = self.message_text.get("1.0", tk.END).strip()

        # Передаем данные получателю
        self.receiver.update_received_data(data, message)


class ReceiverWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Получатель")
        self.window.geometry("400x600")

        # Создаем фрейм для коэффициентов
        coef_frame = ttk.LabelFrame(self.window, text="Коэффициенты")
        coef_frame.pack(padx=10, pady=5, fill="x")

        # Создаем метки и поля для коэффициентов
        coefficients = ['p', 'a - коэф. элипт. кривой', 'b - коэф. элипт. кривой', 'q - порядок подгруппы точек', 'Q - открытый ключ', 'P - точка эллиптической кривой порядка q', '(r, s) - подпись']
        self.coef_entries = {}

        for coef in coefficients:
            frame = ttk.Frame(coef_frame)
            frame.pack(fill="x", padx=5, pady=2)

            ttk.Label(frame, text=f"{coef}:").pack(side="left")
            entry = ttk.Entry(frame)
            entry.pack(side="left", fill="x", expand=True)
            self.coef_entries[coef] = entry

        # Создаем кнопку проверки
        ttk.Button(self.window, text="Проверить",
                   command=self.verify).pack(padx=10, pady=5, fill="x")

        # Создаем текстовое поле
        ttk.Label(self.window, text="Сообщение:").pack(padx=10)
        self.message_text = tk.Text(self.window, height=5)
        self.message_text.pack(padx=10, pady=5, fill="x")

    def update_received_data(self, data, message):
        # Обновляем значения коэффициентов
        for key, value in data.items():
            if key in self.coef_entries:
                self.coef_entries[key].delete(0, tk.END)
                self.coef_entries[key].insert(0, value)

        # Обновляем сообщение
        self.message_text.delete("1.0", tk.END)
        self.message_text.insert("1.0", message)

    def verify(self):
        message = self.message_text.get("1.0", tk.END).strip()
        r = int(self.coef_entries['(r, s) - подпись'].get().rstrip(')').lstrip('(').split(',')[0])
        s = int(self.coef_entries['(r, s) - подпись'].get().rstrip(')').lstrip('(').split(',')[1])
        q = int(self.coef_entries['q - порядок подгруппы точек'].get())
        xp = int(self.coef_entries['P - точка эллиптической кривой порядка q'].get().rstrip(')').lstrip('(').split(',')[0])
        yp = int(self.coef_entries['P - точка эллиптической кривой порядка q'].get().rstrip(')').lstrip('(').split(',')[1])
        a = int(self.coef_entries['a - коэф. элипт. кривой'].get())
        p = int(self.coef_entries['p'].get())
        xq = int(self.coef_entries['Q - открытый ключ'].get().rstrip(')').lstrip('(').split(',')[0])
        yq = int(self.coef_entries['Q - открытый ключ'].get().rstrip(')').lstrip('(').split(',')[1])

        if verif.verif(message, r, s, q, p, xp, yp, a, xq, yq):
            mb.showinfo("Успех",
                         "Подпись верна!")
        else:
            mb.showinfo("Не сошлось",
                        "Подпись не верна!")

def main():
    receiver = ReceiverWindow()
    sender = SenderWindow(receiver)

    sender.window.mainloop()
    receiver.window.mainloop()

if __name__ == "__main__":
    main()