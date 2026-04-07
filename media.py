# Импорты
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
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
chuvak = PhotoImage(file = "./assets/backgrounds/chuvak.png")
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
         print(f"Play {music}")
        elif music == "":
            messagebox.showerror("Error", "Error! You need to select file fisrt.")

    def get_music(self):
        global music
        media = filedialog.askopenfilename(filetypes=[("MP3 Files",('*.mp3')), ("FLAC Files",('*.flac')), ("WAV Files",('*.wav'))])
        music = media
        print(music)

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()


musicplay = MediaPlay(music)

# Задний фон
labelchuvak = Label(window, image = chuvak)
labelchuvak.place(x = 0, y = 0)



# Кнопки

open_button = ttk.Button(window, text="Open file", command=musicplay.get_music)
open_button.place(x=232, y=564)
play_button = ttk.Button(window, text="Start music", command=musicplay.play_music)
play_button.place(x=5, y=564)
stop_button = ttk.Button(window, text="Stop music", command=musicplay.stop_music)
stop_button.place(x=88, y=564)
pause_button = ttk.Button(window, text="Pause music", command=musicplay.pause_music)
pause_button.place(x=367, y=564)
unpause_button = ttk.Button(window, text="Unpause music", command=musicplay.unpause_music)
unpause_button.place(x=457, y=564)

window.mainloop()
