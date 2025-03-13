import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x410")
        
        self.equation = ""
        
        self.display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(root, text=button, width=10, height=3, command=action).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        tk.Button(root, text='C', width=10, height=3, command=self.clear).grid(row=row_val, column=0, columnspan=4, padx=5, pady=5)

    def click_event(self, key):
        if key == '=':
            try:
                self.equation = str(eval(self.equation))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.equation)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
        else:
            self.equation += str(key)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.equation)
    
    def clear(self):
        self.equation = ""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculadora(root)
    root.mainloop()