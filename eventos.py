class Eventos:
    def __init__(self):
        pass

    def entry_keyboard(self, event, key_entry1, key_entry2):
        key = event.char
        if key >= "0" and key <= "9" or key == ".":
            key_entry2.set(key_entry2.get() + key)
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
            return

    def clear_keyboard(self, event, key_entry2):
        inicio = 0
        final = len(key_entry2.get())

        key_entry2.set(key_entry2.get()[inicio : final - 1])

    def clear_all_keyboard(self, event, key_entry1, key_entry2):
        key_entry1.set("")
        key_entry2.set("")
