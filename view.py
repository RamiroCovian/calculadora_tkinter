from tkinter import *
from tkinter import ttk
from eventos import Eventos
from model import Calculator_functions


class Calculator:
    def __init__(self, window):
        self.main = window

        self.main.title("Calculadora")
        self.main.iconbitmap("calc.ico")
        self.main.geometry("374x468+480+180")
        self.main.columnconfigure(0, weight=1)
        self.main.rowconfigure(0, weight=1)

        # Estilo mainframe
        styles = ttk.Style()
        styles.theme_use("alt")
        styles.configure("mainframe.TFrame", background="black")

        mainframe = ttk.Frame(self.main, style="mainframe.TFrame")
        mainframe.grid(row=0, column=0, padx=1, pady=1, sticky=(W, N, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.columnconfigure(1, weight=1)
        mainframe.columnconfigure(2, weight=1)
        mainframe.columnconfigure(3, weight=1)

        mainframe.rowconfigure(0, weight=1)
        mainframe.rowconfigure(1, weight=1)
        mainframe.rowconfigure(2, weight=1)
        mainframe.rowconfigure(3, weight=1)
        mainframe.rowconfigure(4, weight=1)
        mainframe.rowconfigure(5, weight=1)
        mainframe.rowconfigure(6, weight=1)

        # Estilos entry
        style_entry1 = ttk.Style()
        style_entry1.configure(
            "Entry1.TLabel",
            font="arial 15",
            anchor="e",
            background="black",
            foreground="white",
        )
        style_entry2 = ttk.Style()
        style_entry2.configure(
            "Entry2.TLabel",
            font="arial 40",
            anchor="e",
            background="black",
            foreground="white",
        )

        entry1 = StringVar()
        label_entry1 = ttk.Label(mainframe, textvariable=entry1, style="Entry1.TLabel")
        label_entry1.grid(row=0, column=0, sticky=(W, N, E, S), columnspan=4)

        entry2 = StringVar()
        label_entry2 = ttk.Label(mainframe, textvariable=entry2, style="Entry2.TLabel")
        label_entry2.grid(row=1, column=0, sticky=(W, N, E, S), columnspan=4)

        # Estilos botones
        style_button_num = ttk.Style()
        style_button_num.configure(
            "Buttons_Num.TButton",
            font="arial 22",
            width=5,
            foreground="white",
            background="#333633",
            relief="flat",
        )

        style_button_del = ttk.Style()
        style_button_del.configure(
            "Buttons_del.TButton",
            font="arial 22",
            width=5,
            foreground="black",
            background="#b3ced7",
            relief="flat",
        )

        style_buttons = ttk.Style()
        style_buttons.configure(
            "Buttons_.TButton",
            font="arial 22",
            width=5,
            foreground="white",
            background="#e0823d",
            relief="flat",
        )

        # Botones
        button0 = ttk.Button(
            mainframe,
            text="0",
            style="Buttons_Num.TButton",
            command=lambda: Calculator_functions.entry2_values(self, entry2, "0"),
        )
        button1 = ttk.Button(
            mainframe,
            text="1",
            style="Buttons_Num.TButton",
            command=lambda: Calculator_functions.entry2_values(self, entry2, "1"),
        )
        button2 = ttk.Button(
            mainframe,
            text="2",
            style="Buttons_Num.TButton",
            command=lambda: Calculator_functions.entry2_values(self, entry2, "2"),
        )
        button3 = ttk.Button(
            mainframe,
            text="3",
            style="Buttons_Num.TButton",
            command=lambda: Calculator_functions.entry2_values(self, entry2, "3"),
        )
        button4 = ttk.Button(
            mainframe,
            text="4",
            style="Buttons_Num.TButton",
            command=lambda: Calculator_functions.entry2_values(self, entry2, "4"),
        )
        button5 = ttk.Button(
            mainframe,
            text="5",
            style="Buttons_Num.TButton",
            command=lambda: Calculator_functions.entry2_values(self, entry2, "5"),
        )
        button6 = ttk.Button(
            mainframe,
            text="6",
            style="Buttons_Num.TButton",
            command=lambda: Calculator_functions.entry2_values(self, entry2, "6"),
        )
        button7 = ttk.Button(
            mainframe,
            text="7",
            style="Buttons_Num.TButton",
            command=lambda: Calculator_functions.entry2_values(self, entry2, "7"),
        )
        button8 = ttk.Button(
            mainframe,
            text="8",
            style="Buttons_Num.TButton",
            command=lambda: Calculator_functions.entry2_values(self, entry2, "8"),
        )
        button9 = ttk.Button(
            mainframe,
            text="9",
            style="Buttons_Num.TButton",
            command=lambda: Calculator_functions.entry2_values(self, entry2, "9"),
        )

        button_delete = ttk.Button(
            mainframe,
            text=chr(9003),
            style="Buttons_del.TButton",
            command=lambda: Calculator_functions.clear_entry2(self, entry2),
        )
        button_delete_all = ttk.Button(
            mainframe,
            text="C",
            style="Buttons_del.TButton",
            command=lambda: Calculator_functions.clear_all(self, entry1, entry2),
        )
        button_point = ttk.Button(
            mainframe,
            text=".",
            style="Buttons_Num.TButton",
            command=lambda: Calculator_functions.entry2_values(self, entry2, "."),
        )

        button_division = ttk.Button(
            mainframe,
            text=chr(247),
            style="Buttons_.TButton",
            command=lambda: Calculator_functions.entry1_values(
                self, entry1, entry2, "/"
            ),
        )
        button_multiply = ttk.Button(
            mainframe,
            text="x",
            style="Buttons_.TButton",
            command=lambda: Calculator_functions.entry1_values(
                self, entry1, entry2, "*"
            ),
        )
        button_subs = ttk.Button(
            mainframe,
            text="-",
            style="Buttons_.TButton",
            command=lambda: Calculator_functions.entry1_values(
                self, entry1, entry2, "-"
            ),
        )
        button_sum = ttk.Button(
            mainframe,
            text="+",
            style="Buttons_.TButton",
            command=lambda: Calculator_functions.entry1_values(
                self, entry1, entry2, "+"
            ),
        )

        button_equal = ttk.Button(
            mainframe,
            text="=",
            style="Buttons_.TButton",
            command=lambda: Calculator_functions.entry1_values(
                self, entry1, entry2, "="
            ),
        )
        button_square_root = ttk.Button(
            mainframe,
            text="√",
            style="Buttons_.TButton",
            command=lambda: Calculator_functions.square_root(self, entry1, entry2),
        )
        button_percentage = ttk.Button(
            mainframe,
            text="%",
            style="Buttons_.TButton",
            command=lambda: Calculator_functions.percentage(self, entry2, "%"),
        )

        # Situar botones
        button_delete_all.grid(row=2, column=0, sticky=(W, N, E, S))
        button_delete.grid(row=2, column=1, sticky=(W, N, E, S))
        button_percentage.grid(row=2, column=2, sticky=(W, N, E, S))
        button_square_root.grid(row=2, column=3, sticky=(W, N, E, S))

        button7.grid(row=3, column=0, sticky=(W, N, E, S))
        button8.grid(row=3, column=1, sticky=(W, N, E, S))
        button9.grid(row=3, column=2, sticky=(W, N, E, S))
        button_division.grid(row=3, column=3, sticky=(W, N, E, S))

        button4.grid(row=4, column=0, sticky=(W, N, E, S))
        button5.grid(row=4, column=1, sticky=(W, N, E, S))
        button6.grid(row=4, column=2, sticky=(W, N, E, S))
        button_multiply.grid(row=4, column=3, sticky=(W, N, E, S))

        button1.grid(row=5, column=0, sticky=(W, N, E, S))
        button2.grid(row=5, column=1, sticky=(W, N, E, S))
        button3.grid(row=5, column=2, sticky=(W, N, E, S))
        button_subs.grid(row=5, column=3, sticky=(W, N, E, S))

        button0.grid(row=6, column=0, sticky=(W, N, E, S))
        button_point.grid(row=6, column=1, sticky=(W, N, E, S))
        button_equal.grid(row=6, column=2, sticky=(W, N, E, S))
        button_sum.grid(row=6, column=3, sticky=(W, N, E, S))

        for child in mainframe.winfo_children():
            child.grid_configure(
                ipady=10,
                padx=1,
                pady=1,
            )
        self.main.bind(
            "<Key>", lambda evento: Eventos.entry_keyboard(self, evento, entry1, entry2)
        )
        self.main.bind(
            "<KeyPress-c>", lambda evento: Eventos.clear_keyboard(self, evento, entry2)
        )
        self.main.bind(
            "<KeyPress-a>",
            lambda evento: Eventos.clear_all_keyboard(self, evento, entry1, entry2),
        )
