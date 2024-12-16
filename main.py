import existInverse
import keygen
import sign
import verif
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import genPrime

def win_check_primary(type):
    def check_primary():
        num = int(text_entry.get().strip())

        if (type == "FERMA"):
            if genPrime.fermat_primality_test(num) == True:
                result_label.config(text='Простое')
            else:
                result_label.config(text='Не простое')
        elif (type == "PROBA"):
            if genPrime.trial_division_primality(num) == True:
                result_label.config(text='Простое')
            else:
                result_label.config(text='Не простое')

    # Создаем новое окно
    new_window = tk.Toplevel(root)
    new_window.title(f"Проверка")
    new_window.geometry("500x200")

    text_title = ""

    if (type == "FERMA"):
        text_title = 'Тест Ферма'
    elif (type == "PROBA"):
        text_title = "Метод пробных делений"

    title_label = tk.Label(new_window,
                           text=f"Проверка {text_title}",
                           font=("Arial", 14, "bold"))
    title_label.pack(pady=10)

    # Создаем текстовое поле
    text_entry = tk.Entry(new_window, width=30)
    text_entry.pack(pady=20)

    # Создаем кнопку для действия с текстовым полем
    submit_button = tk.Button(new_window, text="Проверить",
                               command=lambda: check_primary())

    result_label = tk.Label(new_window,
                            text="",
                            font=("Arial", 12),
                            wraplength=350)
    result_label.pack(pady=10)
    submit_button.pack()

def winGenPrime():
    def gennum():
        pr = genPrime.genRandomNum()
        pr1 = genPrime.genPrime()
        entry1.insert(0, pr)
        entry2.insert(0, pr1)

    def isPrimary():
        pr = int(entry1.get().strip())
        if (genPrime.trial_division_primality(pr)):
            label1_1['text'] = 'Простое'
        else:
            label1_1['text'] = 'Не простое'

        if (genPrime.fermat_primality_test(pr)):
            label2_1['text'] = 'Простое'
        else:
            label2_1['text'] = 'Не простое'

        pr1 = int(entry2.get().strip())

        if (genPrime.trial_division_primality(pr1)):
            label11_1['text'] = 'Простое'
        else:
            label11_1['text'] = 'Не простое'

        if (genPrime.fermat_primality_test(pr1)):
            label22_1['text'] = 'Простое'
        else:
            label22_1['text'] = 'Не простое'

    pr = 0
    pr1 = 0

    Gen = tk.Toplevel(root)
    Gen.title("Генерация")
    Gen.geometry("400x600")

    button1 = tk.Button(Gen, text="Сгенерировать числа",
                             command=gennum)
    button1.pack(pady=10)

    # Первое текстовое поле
    entry1 = tk.Entry(Gen, width=40)
    entry1.pack(pady=10)

    label1 = tk.Label(Gen, text="Проверка по теореме Ферма")
    label1.pack(pady=10)

    label1_1 = tk.Label(Gen, text="Результат")
    label1_1.pack(pady=10)

    label2 = tk.Label(Gen, text="Проверка по методу пробных делений")
    label2.pack(pady=10)

    label2_1 = tk.Label(Gen, text="Результат")
    label2_1.pack(pady=10)

    entry2 = tk.Entry(Gen, width=40)
    entry2.pack(pady=10)

    label11 = tk.Label(Gen, text="Проверка по теореме Ферма")
    label11.pack(pady=10)

    label11_1 = tk.Label(Gen, text="Результат")
    label11_1.pack(pady=10)

    label22 = tk.Label(Gen, text="Проверка по методу пробных делений")
    label22.pack(pady=10)

    label22_1 = tk.Label(Gen, text="Результат")
    label22_1.pack(pady=10)

    button2 = tk.Button(Gen, text="Проверить",
                        command=isPrimary)
    button2.pack(pady=10)

def winAbout():
    Gen = tk.Toplevel(root)
    Gen.title("Создатель")
    Gen.geometry("320x90")

    label0_1 = ttk.Label(Gen, text="БИСО-01-21 УСТИНОВ И.А.", font="Arial 14")
    label0_1.place(x=10, y=10)

class SenderWindow:
    def __init__(self, master):
        self.master = master
        master.title("Пользователь 1")
        master.geometry("450x600")
        self.zakr_key = 0
        self.hash_message = ''
        self.podpis_r = 0
        self.podpis_s = 0
        self.hashPoluch = 0
        self.messagePoluch = ''

        main_menu = tk.Menu(master)
        master.config(menu=main_menu)

        is_prime_menu = tk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="Проверка на простоту", menu=is_prime_menu)
        is_prime_menu.add_command(label="Метод пробных делений", command=lambda: win_check_primary("PROBA"))
        is_prime_menu.add_command(label="Теорема Ферма", command=lambda: win_check_primary("FERMA"))

        main_menu.add_cascade(label="Сгенерировать числа", command=winGenPrime)

        main_menu.add_cascade(label="Создатель", command=winAbout)

        main_menu.add_cascade(label="Выход", command=root.quit)

        # Создаем фрейм для коэффициентов
        coef_frame = ttk.LabelFrame(master, text="Коэффициенты")
        coef_frame.pack(padx=10, pady=5, fill="x")

        # Создаем метки и поля для коэффициентов
        coefficients = ['p', 'a - коэф. элипт. кривой', 'b - коэф. элипт. кривой', 'q - порядок подгруппы точек', 'Q - открытый ключ', 'P - точка эллиптической кривой порядка q', 'Подпись']
        self.coef_entries = {}

        for coef in coefficients:
            frame = ttk.Frame(coef_frame)
            frame.pack(fill="x", padx=5, pady=2)

            ttk.Label(frame, text=f"{coef}:").pack(side="left")
            entry = ttk.Entry(frame)
            entry.pack(side="left", fill="x", expand=True)
            self.coef_entries[coef] = entry

        # Создаем кнопки
        buttons_frame = ttk.Frame(master)
        buttons_frame.pack(padx=10, pady=5, fill="x")

        ttk.Button(buttons_frame, text="Сформировать ключи",
                   command=self.generate_keys).pack(fill="x", pady=2)

        # Создаем текстовое поле
        ttk.Label(master, text="Сообщение:").pack(padx=10)
        self.message_text = tk.Text(master, height=5)
        self.message_text.pack(padx=10, pady=5, fill="x")

        ttk.Button(master, text="Подписать",
                   command=self.sign).pack(fill="x", padx=10, pady=5)

        ttk.Button(master, text="Отправить",
                   command=self.send).pack(fill="x", padx=10, pady=5)

        ttk.Button(master, text="Проверить",
                   command=self.verify).pack(padx=10, pady=5, fill="x")

        ttk.Label(master, text="Хеш-сумма сообщения:").pack(padx=10)
        self.hash_text = tk.Text(master, height=5)
        self.hash_text.pack(padx=10, pady=5, fill="x")

    def update_coefficient(self, coef_name, value):
        """Обновляет значение в поле ввода коэффициента"""
        if coef_name in self.coef_entries:
            # Очищаем текущее значение
            self.coef_entries[coef_name].delete(0, tk.END)
            # Вставляем новое значение
            self.coef_entries[coef_name].insert(0, str(value))

    def update_received_data(self, data, message, r, s, hash):
        # Обновляем значения коэффициентов
        for key, value in data.items():
            if key in self.coef_entries:
                self.coef_entries[key].delete(0, tk.END)
                self.coef_entries[key].insert(0, value)

        # Обновляем сообщение
        self.message_text.delete("1.0", tk.END)
        self.message_text.insert("1.0", message)

        self.podpis_r = r
        self.podpis_s = s

        self.messagePoluch = message

        self.hashPoluch = hash

    def generate_keys(self):
        p, a, b, q, xp, yp, d, xq, yq = keygen.keygen()
        self.update_coefficient('p', p)
        self.update_coefficient('a - коэф. элипт. кривой', a)
        self.update_coefficient('b - коэф. элипт. кривой', b)
        self.update_coefficient('q - порядок подгруппы точек', q)
        self.update_coefficient('Q - открытый ключ', (xq, yq))
        self.update_coefficient('P - точка эллиптической кривой порядка q', (xp, yp))
        self.zakr_key = d

        mb.showinfo("Успех!",
                     "Ключи сформированы")

    def sign(self):
        message = self.message_text.get("1.0", tk.END).strip()
        self.hash_text.delete("1.0", tk.END)
        if message == '':
            mb.showerror("Ошибка",
                         "Вы ввели пустое сообщение")
        else:
            d = self.zakr_key
            q = int(self.coef_entries['q - порядок подгруппы точек'].get())
            xp = int(self.coef_entries['P - точка эллиптической кривой порядка q'].get().rstrip(')').lstrip('(').split(',')[0])
            yp = int(self.coef_entries['P - точка эллиптической кривой порядка q'].get().rstrip(')').lstrip('(').split(',')[1])
            a = int(self.coef_entries['a - коэф. элипт. кривой'].get())
            p = int(self.coef_entries['p'].get())

            for i in range(100):
                check = existInverse.existInverse(message, q, p, xp, yp, a)

                if check == False:
                    message += " "
                else:
                    self.message_text.delete(1.0, tk.END)
                    self.message_text.insert(1.0, message)
                    break

            r, s, self.hash_message = sign.sign(d, message, q, xp, yp, a, p)

            self.podpis_r = r

            self.podpis_s = s

            concatRS = int(str(r) + str(s))

            self.hash_text.insert("1.0", self.hash_message)

            self.update_coefficient('Подпись', concatRS)

            mb.showinfo("Успех!",
                        "Сообщение подписано!")

    def verify(self):
        message = self.message_text.get("1.0", tk.END).rstrip('\n')
        while message.endswith('\n'):
            message = message.rstrip('\n')
        r = self.podpis_r
        s = self.podpis_s
        q = int(self.coef_entries['q - порядок подгруппы точек'].get())
        xp = int(self.coef_entries['P - точка эллиптической кривой порядка q'].get().rstrip(')').lstrip('(').split(',')[0])
        yp = int(self.coef_entries['P - точка эллиптической кривой порядка q'].get().rstrip(')').lstrip('(').split(',')[1])
        a = int(self.coef_entries['a - коэф. элипт. кривой'].get())
        p = int(self.coef_entries['p'].get())
        xq = int(self.coef_entries['Q - открытый ключ'].get().rstrip(')').lstrip('(').split(',')[0])
        yq = int(self.coef_entries['Q - открытый ключ'].get().rstrip(')').lstrip('(').split(',')[1])

        podpis = int(self.coef_entries['Подпись'].get().rstrip())
        concatRS = int(str(r) + str(s))

        if (message.strip() != self.messagePoluch.strip()):
            mb.showerror("Ошибка!", "Ошибка в сообщении!")
        else:
            isCheck, hash_text = verif.verif(message, r, s, q, p, xp, yp, a, xq, yq)

            if (self.hashPoluch.strip() != hash_text.strip()):
                mb.showerror("Ошибка!", "Проблема в хеш-сумме!")
            elif (podpis != concatRS):
                mb.showerror("Ошибка!", "Проблема в подписи!")

            else:
                if isCheck:
                    mb.showinfo("Успех",
                                 "Подпись верна!")
                    self.hash_text.delete("1.0", tk.END)
                    self.hash_text.insert("1.0", hash_text)
                else:
                    mb.showinfo("Не сошлось",
                                "Подпись не верна!")

    def send(self):
        message = self.message_text.get("1.0", tk.END).strip()
        if message == '':
            mb.showerror("Ошибка",
                         "Вы ввели пустое сообщение")
        else:
            data = {
                'p': self.coef_entries['p'].get(),
                'a - коэф. элипт. кривой': self.coef_entries['a - коэф. элипт. кривой'].get(),
                'b - коэф. элипт. кривой': self.coef_entries['b - коэф. элипт. кривой'].get(),
                'q - порядок подгруппы точек': self.coef_entries['q - порядок подгруппы точек'].get(),
                'Q - открытый ключ': self.coef_entries['Q - открытый ключ'].get(),
                'P - точка эллиптической кривой порядка q': self.coef_entries['P - точка эллиптической кривой порядка q'].get(),
                'Подпись': self.coef_entries['Подпись'].get()
            }
            message = self.message_text.get("1.0", tk.END)

            r = self.podpis_r
            s = self.podpis_s
            hash = self.hash_text.get("1.0", tk.END)

            # Передаем данные получателю
            receiver.update_received_data(data, message, r, s, hash)

            self.message_text.delete("1.0", tk.END)

            mb.showinfo("Успех!",
                        "Передача прошла успешно!")


class ReceiverWindow:
    def __init__(self, master):
        self.master = master
        master.title("Пользователь 2")
        master.geometry("450x600")
        self.hash_sum = ''
        self.podp_r = 0
        self.podp_s = 0
        self.zakr_key = 0
        self.hashPoluch = 0
        self.messagePoluch = ''

        main_menu = tk.Menu(master)
        master.config(menu=main_menu)

        file_menu = tk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="Проверка на простоту", menu=file_menu)
        file_menu.add_command(label="Метод пробных делений", command=lambda: win_check_primary("PROBA"))
        file_menu.add_command(label="Теорема Ферма", command=lambda: win_check_primary("FERMA"))

        main_menu.add_cascade(label="Сгенерировать числа", command=winGenPrime)

        main_menu.add_cascade(label="Создатель", command=winAbout)

        main_menu.add_cascade(label="Выход", command=root.quit)

        # Создаем фрейм для коэффициентов
        coef_frame = ttk.LabelFrame(master, text="Коэффициенты")
        coef_frame.pack(padx=10, pady=5, fill="x")

        # Создаем метки и поля для коэффициентов
        coefficients = ['p', 'a - коэф. элипт. кривой', 'b - коэф. элипт. кривой', 'q - порядок подгруппы точек', 'Q - открытый ключ', 'P - точка эллиптической кривой порядка q', 'Подпись']
        self.coef_entries = {}

        for coef in coefficients:
            frame = ttk.Frame(coef_frame)
            frame.pack(fill="x", padx=5, pady=2)

            ttk.Label(frame, text=f"{coef}:").pack(side="left")
            entry = ttk.Entry(frame)
            entry.pack(side="left", fill="x", expand=True)
            self.coef_entries[coef] = entry

        # Создаем кнопку проверки
        buttons_frame = ttk.Frame(master)
        buttons_frame.pack(padx=10, pady=5, fill="x")

        ttk.Button(buttons_frame, text="Сформировать ключи",
                   command=self.generate_keys).pack(fill="x", pady=2)

        # Создаем текстовое поле
        ttk.Label(master, text="Сообщение:").pack(padx=10)
        self.message_text = tk.Text(master, height=5)
        self.message_text.pack(padx=10, pady=5, fill="x")

        ttk.Button(master, text="Подписать",
                   command=self.sign).pack(fill="x", padx=10, pady=5)

        ttk.Button(master, text="Отправить",
                   command=self.send).pack(fill="x", padx=10, pady=5)

        ttk.Button(master, text="Проверить",
                   command=self.verify).pack(padx=10, pady=5, fill="x")

        ttk.Label(master, text="Хеш-сумма сообщения:").pack(padx=10)
        self.hash_text = tk.Text(master, height=5)
        self.hash_text.pack(padx=10, pady=5, fill="x")

    def update_coefficient(self, coef_name, value):
        """Обновляет значение в поле ввода коэффициента"""
        if coef_name in self.coef_entries:
            # Очищаем текущее значение
            self.coef_entries[coef_name].delete(0, tk.END)
            # Вставляем новое значение
            self.coef_entries[coef_name].insert(0, str(value))

    def sign(self):
        message = self.message_text.get("1.0", tk.END).strip()
        self.hash_text.delete("1.0", tk.END)
        if message == '':
            mb.showerror("Ошибка",
                         "Вы ввели пустое сообщение")
        else:
            d = self.zakr_key
            q = int(self.coef_entries['q - порядок подгруппы точек'].get())
            xp = int(self.coef_entries['P - точка эллиптической кривой порядка q'].get().rstrip(')').lstrip('(').split(',')[0])
            yp = int(self.coef_entries['P - точка эллиптической кривой порядка q'].get().rstrip(')').lstrip('(').split(',')[1])
            a = int(self.coef_entries['a - коэф. элипт. кривой'].get())
            p = int(self.coef_entries['p'].get())

            for i in range(100):
                check = existInverse.existInverse(message, q, p, xp, yp, a)

                if check == False:
                    message += " "
                else:
                    self.message_text.delete(1.0, tk.END)
                    self.message_text.insert(1.0, message)
                    break

            r, s, self.hash_sum = sign.sign(d, message, q, xp, yp, a, p)

            self.podp_r = r

            self.podp_s = s

            concatRS = int(str(r) + str(s))

            self.hash_text.insert("1.0", self.hash_sum)

            self.update_coefficient('Подпись', concatRS)

            mb.showinfo("Успех!",
                        "Сообщение подписано!")

    def generate_keys(self):
        p, a, b, q, xp, yp, d, xq, yq = keygen.keygen()
        self.update_coefficient('p', p)
        self.update_coefficient('a - коэф. элипт. кривой', a)
        self.update_coefficient('b - коэф. элипт. кривой', b)
        self.update_coefficient('q - порядок подгруппы точек', q)
        self.update_coefficient('Q - открытый ключ', (xq, yq))
        self.update_coefficient('P - точка эллиптической кривой порядка q', (xp, yp))
        self.zakr_key = d

        mb.showinfo("Успех!",
                    "Ключи сформированы")

    def update_received_data(self, data, message, r, s, hash):
        # Обновляем значения коэффициентов
        for key, value in data.items():
            if key in self.coef_entries:
                self.coef_entries[key].delete(0, tk.END)
                self.coef_entries[key].insert(0, value)

        # Обновляем сообщение
        self.message_text.delete("1.0", tk.END)
        self.message_text.insert("1.0", message)

        self.messagePoluch = message

        self.podp_r = r
        self.podp_s = s

        self.hashPoluch = hash

    def verify(self):
        message = self.message_text.get("1.0", tk.END).rstrip('\n')
        while message.endswith('\n'):
            message = message.rstrip('\n')
        r = self.podp_r
        s = self.podp_s
        q = int(self.coef_entries['q - порядок подгруппы точек'].get())
        xp = int(self.coef_entries['P - точка эллиптической кривой порядка q'].get().rstrip(')').lstrip('(').split(',')[0])
        yp = int(self.coef_entries['P - точка эллиптической кривой порядка q'].get().rstrip(')').lstrip('(').split(',')[1])
        a = int(self.coef_entries['a - коэф. элипт. кривой'].get())
        p = int(self.coef_entries['p'].get())
        xq = int(self.coef_entries['Q - открытый ключ'].get().rstrip(')').lstrip('(').split(',')[0])
        yq = int(self.coef_entries['Q - открытый ключ'].get().rstrip(')').lstrip('(').split(',')[1])

        podpis = int(self.coef_entries['Подпись'].get().rstrip())
        concatRS = int(str(r) + str(s))


        if (message.strip() != self.messagePoluch.strip()):
            mb.showerror("Ошибка!",
                         "Сообщения не совпадают!")
        else:

            isCheck, hash_text = verif.verif(message, r, s, q, p, xp, yp, a, xq, yq)

            if (self.hashPoluch.strip() != hash_text.strip()):
                mb.showerror("Ошибка!",
                            "Проблема в хеш-сумме!")
                self.hash_text.insert("1.0", hash_text)

            elif (podpis != concatRS):
                mb.showerror("Ошибка!",
                             "Проблема в подписи!!")
            else:
                if isCheck:
                    mb.showinfo("Успех",
                                 "Подпись верна!")
                    self.hash_text.delete("1.0", tk.END)
                    self.hash_text.insert("1.0", hash_text)
                else:
                    mb.showinfo("Не сошлось",
                                "Подпись не верна!")

    def send(self):
        message = self.message_text.get("1.0", tk.END).strip()
        if message == '':
            mb.showerror("Ошибка",
                         "Вы ввели пустое сообщение")
        else:
            message = self.message_text.get("1.0", tk.END)
            data = {
                'p': self.coef_entries['p'].get(),
                'a - коэф. элипт. кривой': self.coef_entries['a - коэф. элипт. кривой'].get(),
                'b - коэф. элипт. кривой': self.coef_entries['b - коэф. элипт. кривой'].get(),
                'q - порядок подгруппы точек': self.coef_entries['q - порядок подгруппы точек'].get(),
                'Q - открытый ключ': self.coef_entries['Q - открытый ключ'].get(),
                'P - точка эллиптической кривой порядка q': self.coef_entries['P - точка эллиптической кривой порядка q'].get(),
                'Подпись': self.coef_entries['Подпись'].get()
            }

            r = self.podp_r
            s = self.podp_s

            hash = self.hash_text.get("1.0", tk.END)

            # Передаем данные получателю
            sender.update_received_data(data, message, r, s, hash)

            self.message_text.delete("1.0", tk.END)

            mb.showinfo("Успех!",
                        "Передача прошла успешно!")

# Создание основного окна
root = tk.Tk()
root.withdraw()  # Скрываем основное окно

receiver = ReceiverWindow(tk.Toplevel(root))
sender = SenderWindow(tk.Toplevel(root))

# Запуск главного цикла
root.mainloop()
