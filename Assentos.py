import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def on_seat_click(row, col):
    messagebox.showinfo("Seleção", f"Você selecionou o assento da fileira {row}, coluna {col}!")

root = tk.Tk()
root.title("Seleção de Assento de Avião")

# Carregando a imagem da cadeira e redimensionando
image_path = "Assento.png"
image = Image.open(image_path)

# Redimensionar a imagem para caber 30 fileiras na tela
new_height = 20  # altura desejada para cada cadeira
aspect_ratio = image.width / image.height
new_width = int(new_height * aspect_ratio)
image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Configuração do layout do avião
num_rows = 30
cols_layout = [2, 3, 2]  # Definindo a estrutura 2-3-2
num_cols = sum(cols_layout) + (len(cols_layout) - 1)  # Somando colunas e espaços

# Obtendo as dimensões da imagem da cadeira redimensionada
image_width, image_height = image.size

# Tamanho total do Canvas
canvas_width = num_cols * image_width + 40  # +40 para espaço para a numeração das fileiras
canvas_height = num_rows * image_height + 20  # +20 para espaço para os títulos das colunas

# Criando o Canvas com o tamanho calculado
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack(pady=20)

# Desenhando os títulos das colunas
column_titles = ['A', 'B', ' ', 'C', 'D', 'E', ' ', 'F', 'G']
current_col = 0
for section_index, section in enumerate(cols_layout):
    for col in range(section):
        x = (current_col + col) * image_width + image_width // 2 + 40  # +40 para espaço para a numeração das fileiras
        canvas.create_text(x, 10, text=column_titles[current_col + col], font=('Arial', 12, 'bold'))
    current_col += section + 1  # Pula para a próxima seção, adicionando um espaço

# Desenhando a numeração das fileiras
for row in range(num_rows):
    y = row * image_height + image_height // 2 + 20  # +20 para espaço para os títulos das colunas
    canvas.create_text(20, y, text=str(row + 1), font=('Arial', 8, 'bold'))

# Criando as cadeiras no Canvas
current_col = 0
for section in cols_layout:
    for row in range(num_rows):
        for col in range(section):
            x = (current_col + col) * image_width + 40  # +40 para espaço para a numeração das fileiras
            y = row * image_height + 20  # +20 para espaço para os títulos das colunas
            # Adicionando a imagem da cadeira como um botão
            button = tk.Button(canvas, image=photo, bd=0, highlightthickness=0,
                               command=lambda row=row, col=current_col + col: on_seat_click(row + 1, column_titles[current_col + col]))
            canvas.create_window(x, y, anchor=tk.NW, window=button)
    current_col += section + 1  # Pula para a próxima seção, adicionando um espaço

root.mainloop()
