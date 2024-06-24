# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from typing import List, Optional

class Aviao:
    def __init__(self, root: tk.Tk, num_rows: int, cols_layout: List[int], column_titles: List[str]):
        self.root = root
        self.canvas = None
        self.photo = None
        self.num_rows = num_rows
        self.cols_layout = cols_layout
        self.column_titles = column_titles
        self.ocupacao = [[False for _ in range(len(self.column_titles))] for _ in range(self.num_rows)]
        self.selected_seat = ""
        self.return_button = None  # Botão "Retornar"
        self.load_image()
        self.calculate_dimensions()

    def load_image(self):
        # Carregando a imagem da cadeira e redimensionando
        image_path = "Images/Assento.png"
        try:
            image = Image.open(image_path)
        except FileNotFoundError:
            print("Imagem do assento não encontrada.")
            return

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
            self.selected_seat = f"{row},{col_title}"
            self.destroy_plane_widget()
        else:
            self.selected_seat = None

    def set_seat(self, ocupacao: List[str]) -> None:
        self.ocupacao = [[False for _ in range(len(self.column_titles))] for _ in range(self.num_rows)]
        for assento in ocupacao:
            seat = assento.split(',')
            row = int(seat[0]) - 1
            col = seat[1]
            col_index = self.column_titles.index(col)
            self.ocupacao[row][col_index] = True


    def create_plane_widget(self):
        # Criando o Canvas com o tamanho calculado
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack(pady=20)

        #reiniciando selected_seat
        self.selected_seat=None
        
        # Desenhando os títulos das colunas
        current_col = 0
        for section_index, section in enumerate(self.cols_layout):
            for col in range(section):
                x = (current_col + col) * self.image_width + self.image_width // 2 + 40  # +40 para espaço para a numeração das fileiras
                self.canvas.create_text(x, 10, text=self.column_titles[current_col + col], font=('Arial', 7, 'bold'))
            current_col += section + 1  # Pula para a próxima seção, adicionando um espaço

        # Desenhando a numeração das fileiras
        for row in range(self.num_rows):
            y = row * self.image_height + self.image_height // 2 + 20  # +20 para espaço para os títulos das colunas
            self.canvas.create_text(20, y, text=str(row + 1), font=('Arial', 8, 'bold'))

        # Criando o botão "Retornar"
        self.return_button = tk.Button(self.root, text="Retornar", command=self.destroy_plane_widget)
        x_button = 20  # posição x corrigida
        y_button = 0
        self.return_button.place(x=x_button, y=y_button)

        # Criando as cadeiras no Canvas
        current_col = 0
        for section_index, section in enumerate(self.cols_layout):
            for row in range(self.num_rows):
                for col in range(section):
                    absolute_col_index = sum(self.cols_layout[:section_index]) + col + section_index
                    if absolute_col_index < len(self.column_titles):
                        x = (current_col + col) * self.image_width + 40  # +40 para espaço para a numeração das fileiras
                        y = row * self.image_height + 20  # +20 para espaço para os títulos das colunas
                        if not self.ocupacao[row][absolute_col_index]:
                            button = tk.Button(self.canvas, image=self.photo, width=self.image_width, height=self.image_height,
                                               bd=0, highlightthickness=0,
                                               command=lambda r=row+1, c=self.column_titles[absolute_col_index]: self.on_seat_click(r, c))
                            self.canvas.create_window(x, y, anchor=tk.NW, window=button)
            current_col += section + 1  # Pula para a próxima seção, adicionando um espaço

    def destroy_plane_widget(self):
        if self.canvas:
            self.canvas.destroy()
            self.canvas = None
        if self.return_button:
            self.return_button.destroy()
            self.return_button = None

    def comprar_passagem(self):
        self.create_plane_widget()
        self.root.wait_window(self.canvas)  # Espera até que o canvas seja destruído
        return self.selected_seat
