import tkinter as tk
from tkinter import messagebox


# Add digits to the entry_main
def add_digit(digit):
    value = entry_main.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    entry_main.delete(0, 'end')
    entry_main.insert('end', value + str(digit))


def add_operation(operation):
    value = entry_main.get()
    if value[-1] in '-+*/':
        value = value[:-1]
    elif '+' in value or '*' in value or '/' in value or '-' in value:
        calculate()
        value = entry_main.get()
    entry_main.delete(0, 'end')
    entry_main.insert('end', value + operation)


def calculate():
    value = entry_main.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    entry_main.delete(0, 'end')
    try:
        entry_main.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', 'Нужно вводить только цифры! Вы ввели другие символы!')
        entry_main.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль делить нельзя!')
        entry_main.insert(0, 0)


def entry_delete():
    entry_main.delete(0, 'end')
    entry_main.insert(0, '0')


def make_digit_button(digit):
    return tk.Button(text=digit, command=lambda: add_digit(digit),
                     font=('Arial', 13), bd=5)


def make_operation_button(operation):
    return tk.Button(text=operation, command=lambda: add_operation(operation),
                     font=('Arial', 13), bd=5, fg='red')


def make_calc_button(equals):
    return tk.Button(text=equals, command=calculate,
                     font=('Arial', 13), bd=5, fg='red')


def make_delete_button(delete):
    return tk.Button(text=delete, command=entry_delete,
                     font=('Arial', 13), bd=5, fg='red')


def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()


# Window creation
root = tk.Tk()
root.title('Calculator')
root.geometry('240x270+100+200')
root['bg'] = '#33ffe6'

# Bind keyboard
root.bind('<Key>', press_key)

# Entry for answer
entry_main = tk.Entry(root, justify=tk.RIGHT, font=('Arial', 15), width=15)
entry_main.insert(0, '0')
entry_main.grid(row=0, column=0, columnspan=4, sticky='WE', padx=5, pady=1)

# Number buttons
make_digit_button(1).grid(row=1, column=0, sticky='WENS', padx=5, pady=5)
make_digit_button(2).grid(row=1, column=1, sticky='WENS', padx=5, pady=5)
make_digit_button(3).grid(row=1, column=2, sticky='WENS', padx=5, pady=5)
make_digit_button(4).grid(row=2, column=0, sticky='WENS', padx=5, pady=5)
make_digit_button(5).grid(row=2, column=1, sticky='WENS', padx=5, pady=5)
make_digit_button(6).grid(row=2, column=2, sticky='WENS', padx=5, pady=5)
make_digit_button(7).grid(row=3, column=0, sticky='WENS', padx=5, pady=5)
make_digit_button(8).grid(row=3, column=1, sticky='WENS', padx=5, pady=5)
make_digit_button(9).grid(row=3, column=2, sticky='WENS', padx=5, pady=5)
make_digit_button(0).grid(row=4, column=0, sticky='WENS', padx=5, pady=5)

# Operations buttons
make_operation_button('+').grid(row=1, column=3, sticky='WENS', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, sticky='WENS', padx=5, pady=5)
make_operation_button('/').grid(row=3, column=3, sticky='WENS', padx=5, pady=5)
make_operation_button('*').grid(row=4, column=3, sticky='WENS', padx=5, pady=5)
make_calc_button('=').grid(row=4, column=2, sticky='WENS', padx=5, pady=5)
make_delete_button('del').grid(row=4, column=1, sticky='WENS', padx=5, pady=5)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)

root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)

root.mainloop()
