from pathlib import Path

# Importações explícitas para satisfazer Flake8
from tkinter import Tk, Canvas, Entry, PhotoImage, StringVar, Label, Toplevel

#Modulo Para Rodar o Player VLC 
import vlc
#Modulo de Thread para a funçao get_tempo = "pegar o tempo da musica"
import threading
#Modulo de tempo para pausar por 5 segundos o bloco de codigo para conseguir pegar o comprimento da midia
import time

from tkinter import *


OUTPUT_PATH = Path(__file__).parent
#Voce tem de mudar para a pasta correta que vc estara usando
#Linux(r"assets/frame0") e Windows(r"assets\frame0)
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def inicio():
    def fechar(event=None):
        window.destroy()
        exit()

    def verificar_musica(event=None):
        import os
        musica = entry_1.get()
        if os.path.exists(musica + ".mp4"):
            player()
        else:
            entry_1.delete(0, END)
            erro = Toplevel()
            erro.geometry("1024x768")
            erro.attributes("-fullscreen", True)
            canvas = Canvas(
                erro,
                bg = "#FFFFFF",
                height = 768,
                width = 1024,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )
            #Configuração de janela do Canvas - Fim

            #Configuração de Estilização do Canvas
            canvas.place(x = 0, y = 0)
            image_4 = canvas.create_image(
                512.0,
                384.0,
                image=image_image_4
            )
            erro.after(4000, erro.destroy)
            
            
            
            


    def player(event=None):
        
        
        #Variavel que vai receber o codigo da musica
        musica = entry_1.get()
        window.destroy()
        #Configuração da janela player
        root = Tk()
        root.title("player")
        root.geometry("1024x768")
        root.attributes('-fullscreen', True)
        #Configuração da janela player - Fim

        def fechar_player(event):
            player.stop()
            root.destroy()
            
        
        #Configuração de janela do Canvas
        canvas = Canvas(
            root,
            bg = "#FFFFFF",
            height = 768,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        #Configuração de janela do Canvas - Fim

        #Configuração de Estilização do Canvas
        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            512.0,
            48.0,#48
            image=image_image_1
        )
        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            512.0,
            717.0,
            image=image_image_2
        )
        #Configuração de Estilização do Canvas - Fim
        root.bind(sequence="<Escape>", func=fechar_player)



        #Configuração e execução do VLC
        Instance = vlc.Instance("--no-xlib")
        player = Instance.media_player_new()
        Media = Instance.media_new(musica + ".mp4")
        player.set_xwindow(canvas.winfo_id())
        player.set_media(Media)
        player.play()
        #Configuração e execução do VLC -Fim

        def get_tempo():
            #Espera 5 minutos para o video executar 
            time.sleep(5)
            
            #Obtendo o comprimento da mídia atual em milissegundos
            valor = player.get_length()
            
            # printing value
            valor = valor - 4800 #4800 milisessegundos para sincronizar o fechamento
            #Fechando a janela do Player
            root.after(valor, root.destroy)
        #Utilizando threads para não colocar no mesmo ponto da janela base do player    
        threading.Thread(target=get_tempo, daemon=True).start()

        root.mainloop()
        inicio()

    #Limitando a 5 digitos na Entry (input)
    def limitar(*args):
        s = var.get()
        if len(s) > 0:
            if not s[-1].isdigit(): # retirar ultimo caracter caso nao seja digito
                var.set(s[:-1])
            else: # aproveitar apenas os primeiros 5 chars
                var.set(s[:max_len])

    #Configuração da Janela Principal-Inicial
    window = Tk()
    window.title("OPENVOICE")
    window.geometry("1024x768")
    window.configure(bg = "#FFFFFF")
    window.attributes('-fullscreen', True)
    #Configuração da Janela Principal-Inicial - Fim

    
    #Configuração de janela do Canvas
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 768,
        width = 1024,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    #Configuração de janela do Canvas - Fim

    #Configuração de Estilização do Canvas
    canvas.place(x = 0, y = 0)
    image_image_4 = PhotoImage(
                file=relative_to_assets("image_4.png"))
    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        512.0,
        384.0,
        image=image_image_3
    )
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        511.5,
        590.0,
        image=entry_image_1
    )
    
    ##Configuração da Função limitar, Ela tem de ficar antes do Entry
    var = StringVar()
    max_len = 5
    var.trace("w", limitar)
    ##Configuração da Função limitar - Fim


    entry_1 = Entry(
        bd=0,
        bg="#00AEEF",
        fg="#000716",
        highlightthickness=0,
        textvariable=var,
        font=('Arial', 65)
    )
    entry_1.place(
        x=387.0,
        y=544.0,
        width=249.0,
        height=90.0
    )
    #Configuração de Estilização do Canvas - Fim


    #Automaticamente já espera entrada do usuario(para nao precisar utilizar o mouse para clicar sempre na entry)
    entry_1.focus_set()


    #Configurações de Atalhos
    #Se apertar ENTER = (<Return>) , chama a funçao player
    
    entry_1.bind('<Return>',verificar_musica)

    #Se apertar F12 = (<F12>) , chama a funçao Fechar e fecha a janela ou desliga o sistema
    entry_1.bind('<F12>', fechar)
     #Se apertar F12 = (<F12>) , chama a funçao Atalhos e mostra os atalhos para ser usado

    


    window.mainloop()




inicio()
