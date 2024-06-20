# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 20:30:50 2024

@author: Eduardo
"""

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
#from aviao import aviao

class Plane:
    def __init__(self, root):
        self.root = root
        self.root.title("Seleção de Assento de Avião")
        self.canvas = None
        self.photo = None
        self.num_rows = 30
        self.cols_layout = [3, 3]  # Definindo a estrutura 3-3
        self.column_titles = ['A', 'B', 'C', ' ', 'D', 'E', 'F']
        self.selected_seat:str = ""
        self.load_image()
        self.calculate_dimensions()

    def load_image(self):
        # Carregando a imagem da cadeira e redimensionando
        image_path = "Images/Assento.png"
        image = Image.open(image_path)

        # Redimensionar a imagem para caber 30 fileiras na tela
        new_height = 20  # altura desejada para cada cadeira
        aspect_ratio = image.width / image.height
        new_width = int(new_height * aspect_ratio)
        image = image.resize((new_width, new_height), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        self.image_width, self.image_height = image.size

    def calculate_dimensions(self):
        # Calcula as dimensões do canvas
        self.num_cols = sum(self.cols_layout) + (len(self.cols_layout) - 1)  # Somando colunas e espaços
        self.canvas_width = self.num_cols * self.image_width + 40  # +40 para espaço para a numeração das fileiras
        self.canvas_height = self.num_rows * self.image_height + 20  # +20 para espaço para os títulos das colunas

    def on_seat_click(self, row, col_title):
        result = messagebox.askquestion("Seleção", f"Você selecionou o assento da fileira {row}, coluna {col_title}! \n Deseja esse assento mesmo?")
        if result == 'yes':
            self.selected_seat = f"{row} {col_title}"
            self.destroy_plane_widget()
        else:
            self.selected_seat = None

    def create_plane_widget(self):
        # Criando o Canvas com o tamanho calculado
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack(pady=20)

        # Desenhando os títulos das colunas
        current_col = 0
        for section_index, section in enumerate(self.cols_layout):
            for col in range(section):
                x = (current_col + col) * self.image_width + self.image_width // 2 + 40  # +40 para espaço para a numeração das fileiras
                self.canvas.create_text(x, 10, text=self.column_titles[current_col + col], font=('Arial', 12, 'bold'))
            current_col += section + 1  # Pula para a próxima seção, adicionando um espaço

        # Desenhando a numeração das fileiras
        for row in range(self.num_rows):
            y = row * self.image_height + self.image_height // 2 + 20  # +20 para espaço para os títulos das colunas
            self.canvas.create_text(20, y, text=str(row + 1), font=('Arial', 8, 'bold'))

        # Criando as cadeiras no Canvas
        current_col = 0
        for section_index, section in enumerate(self.cols_layout):
            for row in range(self.num_rows):
                for col in range(section):
                    absolute_col_index = sum(self.cols_layout[:section_index]) + col + section_index
                    if absolute_col_index < len(self.column_titles):
                        x = (current_col + col) * self.image_width + 40  # +40 para espaço para a numeração das fileiras
                        y = row * self.image_height + 20  # +20 para espaço para os títulos das colunas
                        button = tk.Button(self.canvas, image=self.photo, width=self.image_width, height=self.image_height,
                                           bd=0, highlightthickness=0,
                                           command=lambda r=row+1, c=self.column_titles[absolute_col_index]: self.on_seat_click(r, c))
                        self.canvas.create_window(x, y, anchor=tk.NW, window=button)
            current_col += section + 1  # Pula para a próxima seção, adicionando um espaço

    def destroy_plane_widget(self):
        if self.canvas:
            self.canvas.destroy()
            self.canvas = None
            
    def comprar_passagem(self):
        self.create_plane_widget()
        self.root.wait_window(self.canvas)  # Espera até que o canvas seja destruído
        return self.selected_seat

if __name__ == "__main__":
    root = tk.Tk()
    plane = Plane(root)
    selected_seat = plane.comprar_passagem()
    if selected_seat:
        print(f"Assento selecionado: {selected_seat}")
    else:
        print("Nenhum assento selecionado.")
    root.mainloop()