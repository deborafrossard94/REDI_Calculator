# this is a test
from tkinter import*
from math import*

LARGE_FONT_STYLE = ("Arial", 30, "bold")
SMALL_FONT_STYLE = ("Arial", 14)
DIGITS_FONT_STYLE = ("Arial", 20, "bold")
DEFAULT_FONT_STYLE = ("Arial", 16)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

#use of class:
class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("850x667")
        self.window.resizable(width = True, height = True)
        self.window.title("Debora's Scientific Calculator")

        self.total_expression = ""
        self.total_value = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

#use of dictionary:
        self.digits = {
            7: (2,1), 8: (2, 2), 9: (2, 3),
            4: (3, 1), 5: (3, 2), 6: (3, 3),
            1: (4, 1), 2: (4, 2), 3: (4, 3),
            0: (5, 2), '.': (5, 3)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 6):
            self.buttons_frame.rowconfigure(x, weight=1)
        for x in range(1, 8):
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()
        self.create_scientific_buttons()

        self.display_scientific_calc_text()

    def create_display_frame(self):
        frame = Frame(self.window, height=130, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        total_label = Label(self.display_frame, text=self.total_expression, anchor=E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = Label(self.display_frame, text=self.total_value, anchor=E, bg=LIGHT_GRAY,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_buttons_frame(self):
        frame = Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=NSEW)

    def display_scientific_calc_text(self):
        button = Button(self.buttons_frame, text="Other scientific operations", relief=RIDGE, bg=LIGHT_GRAY, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=2)
        button.grid(row=0, column=5, columnspan=3, sticky=NSEW)

    def create_operator_buttons(self):
        i = 1
        for operator, symbol in self.operations.items():
            button = Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=NSEW)
            i += 1

    def create_special_buttons(self):
        self.percentage_button()
        self.create_clear_entry_button()
        self.create_clear_all_button()
        self.create_backspace_button()
        self.create_pi_button()
        self.create_left_parentesis_button()
        self.create_right_parentesis_button()
        self.create_equals_button()
        self.create_plusminus_button()
    
    def create_scientific_buttons(self):
        self.create_lg_button()
        self.create_ln_button()
        self.create_e_button()
        self.create_sin_button()
        self.create_cos_button()
        self.create_tan_button()
        self.create_divided_by_number()
        self.create_square_button()
        self.create_sqrt_button()
        self.create_exp_button() # x\u02b8 or X^y
        self.create_ten_exp_button() # 10
        self.create_factorial_button() # x!

    def percentage_button(self):
        button = Button(self.buttons_frame, text="%", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.percentage)
        button.grid(row=0, column=1, sticky=NSEW) 

    def create_clear_entry_button(self):
        button = Button(self.buttons_frame, text="CE", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear_entry)
        button.grid(row=0, column=2, sticky=NSEW)   

    def create_clear_all_button(self):
        button = Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear_all)
        button.grid(row=0, column=3, sticky=NSEW)

    def create_backspace_button(self):
        button = Button(self.buttons_frame, text="⌫", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.backspace)
        button.grid(row=0, column=4, columnspan=1, sticky=NSEW)    

    def create_pi_button(self):
        button = Button(self.buttons_frame, text="π", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.pi_value)
        button.grid(row=1, column=1, sticky=NSEW)  

    def create_left_parentesis_button(self):
        button = Button(self.buttons_frame, text="(", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x='(': self.append_operator(x))
        button.grid(row=1, column=2, sticky=NSEW)     

    def create_right_parentesis_button(self):
        button = Button(self.buttons_frame, text=")", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=')': self.append_operator(x))
        button.grid(row=1, column=3, sticky=NSEW)  

    def create_equals_button(self):
        button = Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=5, column=4, columnspan=1, sticky=NSEW)

    def create_plusminus_button(self):
        button = Button(self.buttons_frame, text=chr(177), bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.plusminus)
        button.grid(row=5, column=1, sticky=NSEW)    

    def create_lg_button(self):
        button = Button(self.buttons_frame, text="lg", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.lg)
        button.grid(row=1, column=5, sticky=NSEW)          

    def create_ln_button(self):
        button = Button(self.buttons_frame, text="ln", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.ln)
        button.grid(row=1, column=6, sticky=NSEW)          

    def create_e_button(self):
        button = Button(self.buttons_frame, text="e", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.e_value)
        button.grid(row=1, column=7, sticky=NSEW)         

    def create_sin_button(self):
        button = Button(self.buttons_frame, text="sinθ", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.sin_op)
        button.grid(row=2, column=5, sticky=NSEW)           

    def create_cos_button(self):
        button = Button(self.buttons_frame, text="cosθ", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.cos_op)
        button.grid(row=2, column=6, sticky=NSEW)

    def create_tan_button(self):
        button = Button(self.buttons_frame, text="tanθ", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.tan_op)
        button.grid(row=2, column=7, sticky=NSEW) 

    def create_divided_by_number(self):
        button = Button(self.buttons_frame, text="1/x", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.divide_by_number)
        button.grid(row=3, column=5, sticky=NSEW)

    def create_square_button(self):
        button = Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.square)
        button.grid(row=3, column=6, sticky=NSEW)

    def create_sqrt_button(self):
        button = Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=3, column=7, sticky=NSEW)

    def create_exp_button(self):
        button = Button(self.buttons_frame, text="x\u02b8", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x='**': self.append_operator(x))
        button.grid(row=4, column=5, sticky=NSEW)      

    def create_ten_exp_button (self):
        button = Button(self.buttons_frame, text="10\u02E3", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.ten_exp_op)
        button.grid(row=4, column=6, sticky=NSEW) 

    def create_factorial_button(self):
        button = Button(self.buttons_frame, text="x!", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.factorial_op)
        button.grid(row=4, column=7, sticky=NSEW) 

    def update_current_label(self):
        self.label.config(text=self.total_value[:11])

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def percentage(self):
        self.total_value = str(eval(f"{self.total_value}/100"))
        self.update_current_label()        

    def clear_entry(self):
        self.total_value = ""
        self.update_current_label()
        self.update_total_label()

    def clear_all(self):
        self.total_value = ""
        self.total_expression = ""
        self.update_current_label()
        self.update_total_label()

    def backspace(self):
        numLen = len(self.total_value)
        if numLen == 1 or numLen == 0:
            self.total_value = ""
        else:
            self.total_value = self.total_value[:-1]
        self.update_current_label()

    def pi_value(self):
        if self.total_value == "":
            self.total_value = str(float(pi))
        else:
            self.total_value = str(float(self.total_value)*(pi))
        self.update_current_label()

    def plusminus(self):
        self.total_value = str(eval(f"{self.total_value}*-1"))
        self.update_current_label()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def lg(self):
        self.total_value = str(log10(float(self.total_value)))
        self.update_current_label() 

    def ln(self):
        self.total_value = str(log(float(self.total_value)))
        self.update_current_label() 

    def e_value(self):
        if self.total_value == "":
            self.total_value = str(float(pi))
        else:
            self.total_value = str(float(self.total_value)*(pi))
        self.update_current_label()

    def sin_op(self):
        self.total_value = str(sin(float(self.total_value)))
        self.update_current_label() 

    def cos_op(self):
        self.total_value = str(cos(float(self.total_value)))
        self.update_current_label()

    def tan_op(self):
        self.total_value = str(tan(float(self.total_value)))
        self.update_current_label()

    def divide_by_number(self):
        self.total_value = str(eval(f"1/{self.total_value}"))
        self.update_current_label()
    
    def square(self):
        self.total_value = str(eval(f"{self.total_value}**2"))
        self.update_current_label()

    def sqrt(self):
        self.total_value = str(eval(f"{self.total_value}**0.5"))
        self.update_current_label()

    def exp_op(self):
        self.total_value += '**'
# Do not know how I could fix so the '^' would be the symbol that appears ont the total label instear of 'x x'
        self.total_expression += self.total_value
        self.total_value = ""
        self.update_total_label()
        self.update_current_label()

    def ten_exp_op(self):
        if self.total_value == "":
            self.total_value = str(10**0)
# And here it shows the formula on the display, but when I try to continue it does not work.
#            self.total_expression = "10^(0)"
        else:
            self.total_value = str(10**float(self.total_value))
# Not sure how to present that. I want to show the calculus
#            self.total_expression += self.total_value
        self.update_total_label()
        self.update_current_label()

    def factorial_op(self):
#I would like to say if the number added is an integer then work. For some reason the dactorial is only working for integers
        if self.total_value == int(self.total_value):
            self.total_value = str(factorial(int(self.total_value)))
#            self.total_expression += self.total_value
        else:
#I would also like for this message to appear completely:
            self.total_value = "Error: Only allowed Integer numbers"
        self.update_current_label()

    def add_to_expression(self, value):
        self.total_value += str(value)
        self.update_current_label()

    def append_operator(self, operator):
        self.total_value += operator
        self.total_expression += self.total_value
        self.total_value = ""
        self.update_total_label()
        self.update_current_label()

    def evaluate(self):
        self.total_expression += self.total_value
        self.update_total_label()
        try:
            self.total_value = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.total_value = "Error"
        finally:
            self.update_current_label()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()