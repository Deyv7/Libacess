import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Importa funções reais do main.py
from main import selecionar, ler, exibir_img, conv_audio_texto, iniciar_webcam

# Caminho da imagem do logo
LOGO_PATH = r"imagens\logo.jpg"
FUNDO_BOAS_VINDAS_PATH = r"imagens\fundo_boas_vindas.jpg"

def gravar_audio_seguro():
    try:
        texto = conv_audio_texto()
        if texto:
            print("Texto reconhecido:", texto)
            abrir_janela_libras(texto)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao gravar o áudio:\n{e}")

def abrir_janela_libras(texto):
    # Cria uma nova janela para exibir o texto em Libras
    janela_libras = tk.Toplevel()
    janela_libras.title("Texto em Libras")
    janela_libras.geometry("600x400")
    janela_libras.configure(bg="white")

    # Frame para exibir imagens das letras em Libras
    imagens_frame = tk.Frame(janela_libras, bg="white")
    imagens_frame.pack(pady=20)

    # Lista para armazenar referências das imagens
    imagens_ref = []

    # Divide o texto em palavras
    palavras = texto.split()

    # Itera sobre as palavras
    for palavra in palavras:
        for letra in palavra:
            caminho_imagem = f"libras/{letra}.png"
            print("Buscando:", caminho_imagem)  # Debug

            if os.path.exists(caminho_imagem):
                try:
                    img = Image.open(caminho_imagem)
                    img = img.resize((50, 50), Image.Resampling.LANCZOS)
                    img_tk = ImageTk.PhotoImage(img)

                    # Mantém referência da imagem na lista
                    imagens_ref.append(img_tk)

                    lbl = tk.Label(imagens_frame, image=img_tk, bg="white")
                    lbl.image = img_tk  # Previne garbage collection
                    lbl.pack(side="left", padx=2)
                except Exception as img_error:
                    print(f"Erro ao carregar imagem {caminho_imagem}: {img_error}")
            else:
                print("Imagem não encontrada:", caminho_imagem)

        # Adiciona um espaço entre as palavras
        espaco_label = tk.Label(imagens_frame, bg="white", width=2)
        espaco_label.pack(side="left", padx=20)  # Espaçamento entre palavras

    # Adiciona um botão para fechar a nova janela
    btn_fechar = tk.Button(
        janela_libras,
        text="Fechar",
        font=("Arial", 12, "bold"),
        bg="#FFA500",
        fg="white",
        padx=20,
        pady=10,
        borderwidth=0,
        activebackground="#e69500",
        command=janela_libras.destroy
    )
    btn_fechar.pack(pady=10)


def mostrar_libras(texto):
    # Limpa os widgets anteriores
    for widget in imagens_frame.winfo_children():
        widget.destroy()

    # Lista para armazenar referências das imagens
    imagens_ref = [] 

    # Itera sobre o texto e exibe as imagens correspondentes
    for letra in texto.lower():
        caminho_imagem = f"libras/{letra}.png"
        print("Buscando:", caminho_imagem)  # Debug

        if os.path.exists(caminho_imagem):
            try:
                img = Image.open(caminho_imagem)
                img = img.resize((50, 50), Image.Resampling.LANCZOS)
                img_tk = ImageTk.PhotoImage(img)
                
                # Mantém referência da imagem na lista
                imagens_ref.append(img_tk)  
                
                lbl = tk.Label(imagens_frame, image=img_tk, bg="white")
                lbl.image = img_tk  # Previne garbage collection
                lbl.pack(side="left", padx=2)
            except Exception as img_error:
                print(f"Erro ao carregar imagem {caminho_imagem}: {img_error}")
        else:
            print("Imagem não encontrada:", caminho_imagem)

def iniciar_interface():
    # Criação da janela principal
    root = tk.Tk()
    root.title("Libaccess - Execução Principal")
    root.geometry("800x600")
    root.configure(bg="white")

    # Centraliza a janela na tela
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (800 / 2))
    y = int((screen_height / 2) - (600 / 2))
    root.geometry(f"800x600+{x}+{y}")

    # Exibe o logo
    try:
        img = Image.open(LOGO_PATH)
        img = img.resize((450, 450), Image.Resampling.LANCZOS)
        logo_img = ImageTk.PhotoImage(img)
        logo_label = tk.Label(root, image=logo_img, bg="white")
        logo_label.image = logo_img  # Previne garbage collection
        logo_label.pack(pady=(10, 10))
    except Exception as e:
        logo_label = tk.Label(root, text="[Logo não encontrado]", bg="white", font=("Arial", 14), fg="gray")
        logo_label.pack(pady=(10, 10))

    # Frame para botões
    button_frame = tk.Frame(root, bg="white")
    button_frame.pack(pady=20)

    # Função utilitária para criar botões estilizados
    def criar_botao(texto, comando, coluna):
        btn = tk.Button(
            button_frame,
            text=texto,
            font=("Arial", 12, "bold"),
            bg="#FFA500",
            fg="white",
            padx=20,
            pady=10,
            borderwidth=0,
            activebackground="#e69500",
            command=comando
        )
        btn.grid(row=0, column=coluna, padx=10, pady=10)

    # Botões reais
    criar_botao("Selecionar PDF", selecionar, 0)
    criar_botao("Ler PDF", ler, 1)
    criar_botao("Exibir Imagens", exibir_img, 2)
    criar_botao("Converter Áudio", gravar_audio_seguro, 3)

    # Botão para iniciar webcam (em nova linha)
    webcam_frame = tk.Frame(root, bg="white")
    webcam_frame.pack(pady=10)

    btn_webcam = tk.Button(
        webcam_frame,
        text="Ligar Webcam",
        font=("Arial", 12, "bold"),
        bg="#FFA500",
        fg="white",
        padx=30,
        pady=10,
        borderwidth=0,
        activebackground="#e69500",
        command=iniciar_webcam
    )
    btn_webcam.pack()

    # Frame para exibir imagens das letras em Libras
    global imagens_frame
    imagens_frame = tk.Frame(root, bg="white")
    imagens_frame.pack(pady=20)

    root.mainloop()

# Janela de boas-vindas
splash = tk.Tk()
splash.title("Boas-vindas")
splash.geometry("500x300")
splash.configure(bg="white")

screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()
x = int((screen_width / 2) - (500 / 2))
y = int((screen_height / 2) - (300 / 2))
splash.geometry(f"500x300+{x}+{y}")
# Adiciona imagem à janela de boas-vindas
try:
    fundo_img = Image.open(FUNDO_BOAS_VINDAS_PATH)
    fundo_img = fundo_img.resize((200, 200), Image.Resampling.LANCZOS)
    fundo_photo = ImageTk.PhotoImage(fundo_img)
    fundo_label = tk.Label(splash, image=fundo_photo, bg="white")
    fundo_label.image = fundo_photo
    fundo_label.pack(pady=(10, 5))
except Exception as e:
    print(f"Erro ao carregar imagem: {e}")

# Mensagem com "Libaccess" estilizado
welcome_frame = tk.Frame(splash, bg="white")
welcome_frame.pack(pady=10)

label1 = tk.Label(welcome_frame, text="Bem-vindo ao ", font=("Arial", 16, "bold"), bg="white", fg="#FFA500")
label1.pack(side="left")
label2 = tk.Label(welcome_frame, text="Libaccess!", font=("Arial", 16, "bold"), bg="white", fg="#003366")
label2.pack(side="left")


btn_iniciar = tk.Button(
    splash,
    text="Iniciar",
    font=("Arial", 12, "bold"),
    bg="#FFA500",
    fg="white",
    padx=20,
    pady=10,
    borderwidth=0,
    activebackground="#e69500",
    command=lambda: [splash.destroy(), iniciar_interface()]
)
btn_iniciar.pack()

splash.mainloop()
