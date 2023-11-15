import math


class Calculator_functions:
    def __init__(self):
        pass

    def entry2_values(self, key_entry2, key):
        if key >= "0" and key <= "9" or key == ".":
            key_entry2.set(key_entry2.get() + key)

    def entry1_values(self, key_entry1, key_entry2, key):
        if key == "*" or key == "/" or key == "+" or key == "-":
            if key == "*":
                key_entry1.set(key_entry2.get() + "*")
            elif key == "/":
                key_entry1.set(key_entry2.get() + "/")
            elif key == "+":
                key_entry1.set(key_entry2.get() + "+")
            elif key == "-":
                key_entry1.set(key_entry2.get() + "-")
            key_entry2.set("")

        if key == "=":
            key_entry1.set(key_entry1.get() + key_entry2.get())
            resultado = eval(key_entry1.get())
            key_entry2.set(resultado)

    def square_root(self, key_entry1, key_entry2):
        key_entry1.set("")
        resultado = math.sqrt(float(key_entry2.get()))
        key_entry2.set(resultado)

    def percentage(self, key_entry2, key):
        if key == "%":
            perce = float(key_entry2.get()) / 100
            key_entry2.set(str(perce))

    def clear_entry2(self, key_entry2):
        inicio = 0
        final = len(key_entry2.get())

        key_entry2.set(key_entry2.get()[inicio : final - 1])

    def clear_all(self, key_entry1, key_entry2):
        key_entry1.set("")
        key_entry2.set("")
