# -*- coding: utf-8 -*-

from aviões.Avioes_set import Aviao  # Importa a classe base Aviao do módulo aviões
import tkinter as tk

class Airbus320(Aviao):
    def __init__(self, root: tk.Tk):
        # Inicializa a classe Airbus320 com o layout específico do avião
        super().__init__(root, num_rows=30, cols_layout=[3, 3], column_titles=['A', 'B', 'C', ' ', 'D', 'E', 'F'])
        
class Boeing777(Aviao):
    def __init__(self, root: tk.Tk):
        # Inicializa a classe Boeing777 com o layout específico do avião
        super().__init__(root, num_rows=30, cols_layout=[2, 3, 2], column_titles=['A', 'B', ' ', 'C', 'D', 'E', ' ', 'F', 'G'])
        
class AirBus370(Aviao):
    def __init__(self, root: tk.Tk):
        # Inicializa a classe AirBus370 com o layout específico do avião
        super().__init__(root, num_rows=35, cols_layout=[3, 4, 3], column_titles=['A', 'B','C', ' ', 'D', 'E', 'F', 'G', ' ','H','I','J'])
        
if __name__ == "__main__":
    root = tk.Tk()
    
    # Cria uma instância do AirBus370
    plane1 = AirBus370(root)
    
    # Cria uma instância do Airbus320
    plane2 = Airbus320(root)
    
    # Para criar uma instância do Boeing777 (descomentando a linha abaixo)
    # plane = Boeing777(root)
    
    # Inicia o processo de compra de passagem para o plane2 (Airbus320)
    selected_seat = plane2.comprar_passagem()
    if selected_seat:
        # Exibe o assento selecionado
        print(f"Assento selecionado: {selected_seat}")
    else:
        # Informa que nenhum assento foi selecionado
        print("Nenhum assento selecionado.")
        
    # Inicia novamente o processo de compra de passagem para o plane2 (Airbus320)
    selected_seat = plane2.comprar_passagem()
    if selected_seat:
        # Exibe o assento selecionado
        print(f"Assento selecionado: {selected_seat}")
    else:
        # Informa que nenhum assento foi selecionado
        print("Nenhum assento selecionado.")
    
    # Inicia o loop principal do Tkinter
    root.mainloop()
