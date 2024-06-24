# -*- coding: utf-8 -*-

from aviões.Avioes_set import Aviao
import tkinter as tk

class Airbus320(Aviao):
    def __init__(self, root: tk.Tk):
        super().__init__(root, num_rows=30, cols_layout=[3, 3], column_titles=['A', 'B', 'C', ' ', 'D', 'E', 'F'])
        
class Boeing777(Aviao):
    def __init__(self, root: tk.Tk):
        super().__init__(root, num_rows=30, cols_layout=[2, 3, 2], column_titles=['A', 'B', ' ', 'C', 'D', 'E', ' ', 'F', 'G'])
        
class AirBus370(Aviao):
    def __init__(self, root: tk.Tk):
        super().__init__(root, num_rows=35, cols_layout=[3, 4, 3], column_titles=['A', 'B','C', ' ', 'D', 'E', 'F', 'G', ' ','H','I','J'])
        
if __name__ == "__main__":
    root = tk.Tk()
    
    # Para criar uma instância do Airbus320
    plane1 = AirBus370(root)
    plane2 = Airbus320(root)
    
    # Para criar uma instância do Boeing777
    # plane = Boeing777(root)
    
    selected_seat = plane2.comprar_passagem()
    if selected_seat:
        print(f"Assento selecionado: {selected_seat}")
    else:
        print("Nenhum assento selecionado.")
        
    selected_seat = plane2.comprar_passagem()
    if selected_seat:
        print(f"Assento selecionado: {selected_seat}")
    else:
        print("Nenhum assento selecionado.")
    
    root.mainloop()
