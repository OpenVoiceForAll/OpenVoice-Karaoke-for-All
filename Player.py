from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import vlc

def player():
    root = Tk()
    root.attributes("-fullscreen", True)
    canvas = Canvas(
        root,
        bg="#FFFFFF",
        height=768,
        width=1024,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=1, y=1)
    canvas.create_rectangle(
    0.0,
    690.0,
    1024.0,
    768.0,
    fill="#1E90FF",
    outline="")

    canvas.create_rectangle(
    0.0,
    0.0,
    1024.0,
    78.0,
    fill="#1E90FF",
    outline="")

    canvas.create_text(
    143.0,
    16.0,
    anchor="nw",
    text="O palco é seu, com o karaokê SENAC Registro!",
    fill="#FFFFFF",
    font=("IrishGrover Regular", 36 * -1)
    )

    canvas.create_text(
    143.0,
    705.0,
    anchor="nw",
    text="SENAC Karaokê: Onde Talento Ganha Voz!",
    fill="#FFFFFF",
    font=("IrishGrover Regular", 36 * -1)
    )

    canvas.create_rectangle(
    0.0,
    78.0,
    1024.0,
    699.0,
    fill="#000000",
    outline="")
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(musica)
    player.set_xwindow(canvas.winfo_id())
    player.set_media(Media)
    player.play()

    root.mainloop()

musica = "119933.mp4"

player()