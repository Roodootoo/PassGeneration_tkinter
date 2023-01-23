import tkinter
from string import ascii_lowercase, ascii_uppercase, punctuation, digits

import customtkinter as CTk

import password


class PassGen(CTk.CTk):
    def __init__(self):
        super().__init__()

        # Размеры окна
        self.geometry('460x240')
        self.title('PassGen')
        self.resizable(False, False)

        # Инициализация фрейма для поля пароля
        self.password_frame = CTk.CTkFrame(master=self, fg_color='transparent')
        self.password_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky='nsew')

        # Поле вывода пароля
        self.entry_password = CTk.CTkEntry(master=self.password_frame, width=300)
        self.entry_password.grid(row=0, column=0, padx=(0, 20))
        self.entry_password.insert(0, '   click Generate -->')

        # Кнопка Сгенерировать пароль
        self.btn_password = CTk.CTkButton(master=self.password_frame, text='Generate', width=100,
                                          command=self.set_password)
        self.btn_password.grid(row=0, column=1)

        # Инициализация фрейма для настроек пароля
        self.settings_frame = CTk.CTkFrame(master=self)
        self.settings_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky='nsew')

        # Слайдер длины пароля
        self.password_length_slider = CTk.CTkSlider(master=self.settings_frame, from_=0, to=100, number_of_steps=100,
                                                    command=self.slider_event)
        self.password_length_slider.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky='ew')

        self.password_length_entry = CTk.CTkEntry(master=self.settings_frame, width=50)
        self.password_length_entry.grid(row=1, column=3, padx=(20, 20), sticky='we')

        self.password_length_slider.set(16)
        self.password_length_entry.insert(0, 16)

        # Сложность пароля
        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = CTk.CTkCheckBox(master=self.settings_frame, text='0-9', variable=self.cb_digits_var,
                                         onvalue=digits, offvalue='')
        self.cb_digits.grid(row=2, column=0, padx=10)
        self.cb_digits_var.set(digits)

        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = CTk.CTkCheckBox(master=self.settings_frame, text='a-z', variable=self.cb_lower_var,
                                         onvalue=ascii_lowercase, offvalue='')
        self.cb_lower.grid(row=2, column=1)
        self.cb_lower_var.set(ascii_lowercase)

        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = CTk.CTkCheckBox(master=self.settings_frame, text='A-Z', variable=self.cb_upper_var,
                                         onvalue=ascii_uppercase, offvalue='')
        self.cb_upper.grid(row=2, column=2)
        self.cb_upper_var.set(ascii_uppercase)

        self.cb_symbol_var = tkinter.StringVar()
        self.cb_symbol = CTk.CTkCheckBox(master=self.settings_frame, text='@#$%', variable=self.cb_symbol_var,
                                         onvalue=punctuation, offvalue='')
        self.cb_symbol.grid(row=2, column=3)

        # Изменение цвета приложения
        self.appearance_mode_option_menu = CTk.CTkOptionMenu(master=self.settings_frame,
                                                             values=('Light', 'Dark', 'System'),
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=3, column=0, columnspan=4, pady=(20, 20))
        self.appearance_mode_option_menu.set('System')

    def change_appearance_mode_event(self, new_appearance_mode):
        ''' Изменить цвет приложения '''
        CTk.set_appearance_mode(new_appearance_mode)

    def slider_event(self, value):
        ''' Установка значения слайдера '''
        self.password_length_entry.delete(0, 'end')
        self.password_length_entry.insert(0, int(value))

    def get_characters(self):
        ''' Получить символы для пароля '''
        if self.cb_digits_var.get() + self.cb_symbol_var.get() + self.cb_lower_var.get() \
                      + self.cb_upper_var.get() == '':
            self.cb_digits_var.set(digits)
            self.cb_lower_var.set(ascii_lowercase)
            self.cb_upper_var.set(ascii_uppercase)

        chars = ''.join(self.cb_digits_var.get() + self.cb_symbol_var.get() + self.cb_lower_var.get() \
                      + self.cb_upper_var.get())

        return chars

    def set_password(self, ):
        ''' Сформировать пароль '''
        self.entry_password.delete(0, 'end')
        self.entry_password.insert(0, password.create_new(length=int(self.password_length_slider.get()),
                                                          characters=self.get_characters()))


if __name__ == '__main__':
    app = PassGen()
    app.mainloop()
