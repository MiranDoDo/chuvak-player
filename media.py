# Импорты
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pygame

# Обязательная инциализация
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()


# Окно
window = Tk()
window.title("Chuvak Player")
window.geometry("570x600")
window.maxsize(570, 600)
window.minsize(570, 600)

# Переменные
chuvak = PhotoImage(file = "chuvak.png")
music = ""

class MediaPlay:

#"""Документация к классу MediaPlay
# Используется для выбора, воспроизведения, остановки и паузы музыки"""

    def __init__(self, media):
        self.media = media

    def play_music(self):
        global music
        if music != "":
         pygame.mixer.music.load(music)
         pygame.mixer.music.play()
         print(f"Сейчас играет {music}")

    def get_music(self):
        global music
        media = filedialog.askopenfilename(filetypes=[("MP3 Files",('*.mp3')), ("FLAC Files",('*.flac'))])
        music = media
        print(music)

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()


musicplay = MediaPlay(music)

# Картинка с Чуваком
labelchuvak = Label(window, image = chuvak)
labelchuvak.place(x = 0, y = 0)


# Кнопки

open_button = ttk.Button(text="Открыть файл", command=musicplay.get_music)
open_button.pack(side=BOTTOM)
play_button = ttk.Button(text="Воспроизвести музыку", command=musicplay.play_music)
play_button.pack(side=BOTTOM)
stop_button = ttk.Button(text="Остановить музыку", command=musicplay.stop_music)
stop_button.pack(side=BOTTOM)
pause_button = ttk.Button(text="Поставить на паузу музыку", command=musicplay.pause_music)
pause_button.pack(side=BOTTOM)
unpause_button = ttk.Button(text="Убрать с паузы музыку", command=musicplay.unpause_music)
unpause_button.pack(side=BOTTOM)

window.mainloop()
