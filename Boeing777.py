# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 20:26:32 2024

@author: Eduardo
"""


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from typing import List, Optional
from aviao import aviao

class Boeing777:
    def __init__(self, root: tk.Tk):
        self.root: tk.Tk = root
        self.root.title("Seleção de Assento de Avião")
        self.canvas: Optional[tk.Canvas] = None
        self.photo: Optional[ImageTk.PhotoImage] = None
        self.load_image()
        
        
    def load_image(self):
        # Carregando a imagem da cadeira e redimensionando
        image_path: str = "Images/Assento.png"
        image: Image.Image = Image.open(image_path)

        # Redimensionar a imagem para caber 30 fileiras na tela
        new_height: int = 20  # altura desejada para cada cadeira
        aspect_ratio: float = image.width / image.height
        new_width: int = int(new_height * aspect_ratio)
        image = image.resize((new_width, new_height), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)

        # Configuração do layout do avião
        self.num_rows: int = 30
        self.cols_layout: List[int] = [2, 3, 2]  # Definindo a estrutura 2-3-2
        self.num_cols: int = sum(self.cols_layout) + (len(self.cols_layout) - 1)  # Somando colunas e espaços

        # Obtendo as dimensões da imagem da cadeira redimensionada
        self.image_width: int
        self.image_height: int
        self.image_width, self.image_height = image.size

        # Tamanho total do Canvas
        self.canvas_width: int = self.num_cols * self.image_width + 40  # +40 para espaço para a numeração das fileiras
        self.canvas_height: int = self.num_rows * self.image_height + 20  # +20 para espaço para os títulos das colunas

    def on_seat_click(self, row: int, col_title: str) -> None:
        messagebox.showinfo("Seleção", f"Você selecionou o assento da fileira {row}, coluna {col_title}!")

    def create_plane_widget(self) -> None:
        # Criando o Canvas com o tamanho calculado
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack(pady=20)

        # Desenhando os títulos das colunas
        column_titles: List[str] = ['A', 'B', ' ', 'C', 'D', 'E', ' ', 'F', 'G']
        current_col: int = 0
        for section_index, section in enumerate(self.cols_layout):
            for col in range(section):
                x: int = (current_col + col) * self.image_width + self.image_width // 2 + 40  # +40 para espaço para a numeração das fileiras
                self.canvas.create_text(x, 10, text=column_titles[current_col + col], font=('Arial', 12, 'bold'))
            current_col += section + 1  # Pula para a próxima seção, adicionando um espaço

        # Desenhando a numeração das fileiras
        for row in range(self.num_rows):
            y: int = row * self.image_height + self.image_height // 2 + 20  # +20 para espaço para os títulos das colunas
            self.canvas.create_text(20, y, text=str(row + 1), font=('Arial', 8, 'bold'))

        # Criando as cadeiras no Canvas
        current_col = 0
        for section_index, section in enumerate(self.cols_layout):
            for row in range(self.num_rows):
                for col in range(section):
                    absolute_col_index: int = sum(self.cols_layout[:section_index]) + col
                    if absolute_col_index < len(column_titles):
                        x = (current_col + col) * self.image_width + 40  # +40 para espaço para a numeração das fileiras
                        y = row * self.image_height + 20  # +20 para espaço para os títulos das colunas
                        button = tk.Button(self.canvas, image=self.photo, width=self.image_width, height=self.image_height,
                                           bd=0, highlightthickness=0,
                                           command=lambda row=row+1, col_title=column_titles[absolute_col_index]: self.on_seat_click(row, col_title))
                        self.canvas.create_window(x, y, anchor=tk.NW, window=button)
            current_col += section + 1  # Pula para a próxima seção, adicionando um espaço

    def destroy_plane_widget(self) -> None:
        if self.canvas:
            self.canvas.destroy()
            self.canvas = None


if __name__ == "__main__":
    root = tk.Tk()

    plane = Boeing777(root)

    # Create and pack the plane widget
    def create() -> None:
        plane.create_plane_widget()

    # Destroy the plane widget
    def destroy() -> None:
        plane.destroy_plane_widget()

    create_button = tk.Button(root, text="Create Plane", command=create)
    create_button.pack(side=tk.LEFT, padx=10, pady=10)

    destroy_button = tk.Button(root, text="Destroy Plane", command=destroy)
    destroy_button.pack(side=tk.RIGHT, padx=10, pady=10)

    root.mainloop()
