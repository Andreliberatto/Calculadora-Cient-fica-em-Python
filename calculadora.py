import tkinter as tk
import math

class CalculadoraCientifica(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Calculadora Científica")
        self.geometry("400x600")
        self.config(bg="#2E2E2E")  # Cor de fundo mais escura para um visual mais moderno
        
        # Display da calculadora
        self.display = tk.Entry(self, width=20, font=("Arial", 24), borderwidth=0, relief="solid", justify="right", bg="#1E1E1E", fg="white")
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=20)
        
        self.create_widgets()
        self.bind("<Key>", self.on_key_press)  # Permite capturar os comandos do teclado

    def create_widgets(self):
        # Definindo os botões com texto e suas posições na grade
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('sqrt', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('sin', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('cos', 4, 4),
            ('tan', 5, 0), ('log', 5, 1), ('(', 5, 2), (')', 5, 3), ('pi', 5, 4),
            ('!', 6, 0), ('^', 6, 1), ('nCr', 6, 2)
        ]
        
        # Criando os botões com a aparência moderna
        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, width=5, height=2, font=("Arial", 18), bg="#3A3A3A", fg="white", relief="flat", activebackground="#5A5A5A", command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
    
    def on_button_click(self, button_text):
        current_text = self.display.get()
        
        if button_text == 'C':
            self.display.delete(0, tk.END)
        elif button_text == '=':
            self.calculate_result()
        elif button_text == 'pi':
            self.display.insert(tk.END, str(math.pi))
        elif button_text == 'sqrt':
            self.display.insert(tk.END, 'math.sqrt(')
        elif button_text == 'sin':
            self.display.insert(tk.END, 'math.sin(')
        elif button_text == 'cos':
            self.display.insert(tk.END, 'math.cos(')
        elif button_text == 'tan':
            self.display.insert(tk.END, 'math.tan(')
        elif button_text == 'log':
            self.display.insert(tk.END, 'math.log(')
        elif button_text == '!':
            self.display.insert(tk.END, 'math.factorial(')
        elif button_text == 'nCr':
            self.display.insert(tk.END, 'math.comb(')
        elif button_text == '^':
            self.display.insert(tk.END, '**')
        elif button_text == '(' or button_text == ')':
            self.display.insert(tk.END, button_text)
        else:
            self.display.insert(tk.END, button_text)
    
    def on_key_press(self, event):
        key = event.char
        
        # Verifica se a tecla pressionada é válida para a entrada de cálculos
        if key in '0123456789+-*/.()':
            self.display.insert(tk.END, key)
        elif key == 'Enter':
            self.calculate_result()  # Calcula o resultado quando a tecla Enter é pressionada
        elif key == 'BackSpace':
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current_text[:-1])
    
    def calculate_result(self):
        current_text = self.display.get()
        try:
            result = self.evaluate_expression(current_text)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Erro")

    def evaluate_expression(self, expression):
        expression = expression.replace('^', '**')  # Substitui ^ por **
        expression = expression.replace('math.sqrt', 'math.sqrt')  # Mantém a raiz quadrada
        expression = expression.replace('math.sin', 'math.sin')  # Mantém seno
        expression = expression.replace('math.cos', 'math.cos')  # Mantém cosseno
        expression = expression.replace('math.tan', 'math.tan')  # Mantém tangente
        expression = expression.replace('math.log', 'math.log')  # Mantém logaritmo
        expression = expression.replace('math.factorial', 'math.factorial')  # Mantém fatorial
        expression = expression.replace('math.comb', 'math.comb')  # Mantém combinação
        return eval(expression)


if __name__ == "__main__":
    app = CalculadoraCientifica()
    app.mainloop()
