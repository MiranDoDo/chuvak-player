# Импорты

from tkinter import *
from tkinter import filedialog, messagebox, ttk
import tkinter as tk
import pygame
import time

# Обязательная инциализация

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

# Окно

window = Tk()
window.title("Chuvak Player")
window.geometry("570x600")
window.maxsize(570, 600)
window.minsize(570, 600)
window.style = ttk.Style(window)
window.style.configure('TButton', font=('Helvetica', 11), background='#d1ea8f')


# Переменные

background_chuvak = PhotoImage(file = "./assets/backgrounds/chuvak.png")
music_path = ""


class MediaPlay:

#               Документация к классу MediaPlay
# Используется для выбора, воспроизведения, остановки и паузы музыки

    def __init__(self):
        pass


    def play_music(self):
        global music_path
        if music_path == "":
            messagebox.showerror("Error", "Error! You need to select file fisrt.")
        elif music_path != "":
         pygame.mixer.music.load(music_path)
         time.sleep(0.1) # Маленькая задержка
         pygame.mixer.music.play(-1)
         print(f"Play {music_path}")

    def select_music(self):
        global music_path
        music = filedialog.askopenfilename(filetypes=[
            ("MP3 Files",('*.mp3')),
            ("FLAC Files",('*.flac')),
            ("WAV Files",('*.wav'))]
        )
        # Проверка типа и пути файла
        if type(music) == tuple:
            pass
        elif music != "":
             music_path = music
             print(music_path)
             # Нахождение имени музыки
             music_name1 = music_path.rfind("/")
             music_name2 = music_path[music_name1+1:len(music_path)]
             label_name.config(text = music_name2)
                 
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()

musicplay = MediaPlay()


## UI

# Задний фон
label_background = Label(window, image = background_chuvak)
label_background.place(x = 0, y = -45)

# Label для кнопок

label_buttons = Label(window,
bg='#0b9b92',
width=150,
height=3,
text=""
)
label_buttons.place(x=0, y=553)

# Label для названия музыки

label_name = Label(window,
bg='#0b9b92',
fg='#ffffff',
width=40,
height=3,
font=('Helvetica', 11)
)
label_name.place(x=120, y=510)

# Кнопки

play_button = ttk.Button(
window,
text="Start music",
command=musicplay.play_music
)
play_button.place(x=5, y=564)

open_button = ttk.Button(
window,
text="Open file",
command=musicplay.select_music
)
open_button.place(x=232, y=564)

stop_button = ttk.Button(
window,
text="Stop music",
command=musicplay.stop_music
)
stop_button.place(x=88, y=564)

pause_button = ttk.Button(
window,
text="Pause music",
command=musicplay.pause_music
)
pause_button.place(x=364, y=564)

unpause_button = ttk.Button(
window,
text="Unpause music",
command=musicplay.unpause_music
)
unpause_button.place(x=457, y=564)

window.mainloop()
