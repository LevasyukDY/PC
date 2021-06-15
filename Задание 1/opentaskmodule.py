import tkinter as tk
from PIL import Image, ImageTk


def open_task(name):
    """
    Открытие окна с заданием
    
    Параметры:
    name -- имя файла с расширением

    """ 
    root = tk.Tk()

    # Создаем рабочую область
    frame = tk.Frame(root)
    frame.grid()

    # Добавим изображение
    image = Image.open(name)
    
    # Узнаём размер изображения и подгоняем окно под него
    (width, height) = image.size
    canvas = tk.Canvas(root, height=height, width=width)
    
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw',image=photo)
    canvas.grid(row=2,column=1)
    
    # Заголовок окна и главный цикл
    root.title("Задание")
    root.mainloop()
