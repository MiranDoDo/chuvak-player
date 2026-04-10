# Импорты
from tkinter import *
from tkinter import filedialog, messagebox, ttk
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
background_chuvak = PhotoImage(file = "./assets/backgrounds/chuvak.png")
window.iconphoto(False, background_chuvak)
window.style = ttk.Style(window)
window.style.configure('TButton', font=('Helvetica', 11), background='#d1ea8f')

# Переменные

music_path = ""
IS_PLAY = False


class MediaPlay:

#               Документация к классу MediaPlay
# Используется для выбора, воспроизведения, остановки и паузы музыки

    def __init__(self):
        pass


    def play_music(self):
        global music_path
        global IS_PLAY
        if music_path == "":
            messagebox.showerror("Error", "Error! You need to select file fisrt.")
        elif music_path != "":
         pygame.mixer.music.load(music_path)
         IS_PLAY = True
         time.sleep(0.1)
         pygame.mixer.music.play(-1)


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
             music_name1 = music_path.rfind("/") # Удаляет путь к файлу, оставляя только его название
             music_name2 = music_path.rfind(".") # Удаляет расширение файла
             music_name3 = music_path[music_name1+1:music_name2]
             label_name.config(font=('Helvetica', 11), text = music_name3)


    def stop_music(self):
        global IS_PLAY           
        pygame.mixer.music.stop()
        IS_PLAY = False

    def pause_music(self):
        global IS_PLAY
        if IS_PLAY == True: # Проверка: Играет ли музыка
            pygame.mixer.music.pause() # Если да, то ставит на паузу
            IS_PLAY = False
        elif IS_PLAY == False: # Иначе:
            pygame.mixer.music.unpause() # Убирает с паузы
            IS_PLAY = True

musicplay = MediaPlay()


## UI

# Задний фон

label_background = Label(window, image = background_chuvak)
label_background.place(x = 0, y = -45)


# Меню

menubar = Menu(window,
bg='#0b9b92',
borderwidth=3.2)
file = Menu(menubar, tearoff = 0)

menubar.add_cascade(label ='File ',
menu = file,
background='#d1ea8f',
activebackground='#d1ea8f',
font=('Helvetica', 11)
)

file.add_command(label ='Open Audio',
command = musicplay.select_music,
background='#d1ea8f',
activebackground='#d1ea8f',
font=('Helvetica', 11)
)

file.add_separator(background='#d1ea8f')

file.add_command(label ='Exit',
command = window.destroy,
background='#d1ea8f',
activebackground='#d1ea8f',
font=('Helvetica', 11)
)


# Label для кнопок

label_buttons = Label(window,
bg='#0b9b92',
width=150,
height=3,
text=""
)
label_buttons.place(x=0, y=510)

# Label для названия музыки

label_name = Label(window,
bg="#107c75",
fg='#ffffff',
width=40,
height=3,
font=('Helvetica', 11),
relief="raised",
text="In the Silence.."
)
label_name.pack(side=BOTTOM)


# Кнопки

play_button = ttk.Button(
window,
text="Play",
command=musicplay.play_music
)
play_button.place(x=5, y=513)

stop_button = ttk.Button(
window,
text="Stop",
command=musicplay.stop_music
)
stop_button.place(x=5, y=539)

BPstyle = ttk.Style()
BPstyle.configure('Large.TButton', padding=9)

pause_button = ttk.Button(
window,
text="Pause",
command=musicplay.pause_music,
style="Large.TButton"
)
pause_button.place(x=470, y=520)


window.config(menu = menubar)
window.mainloop()