from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

jan = Tk()
jan.title("Solicite Aqui - Acess panel")
jan.geometry("500x600")
jan.configure(background="black")
jan.resizable(width=False, height=False)
jan.iconbitmap(default="images/Artboard-208-Copia.ico")

nome = PhotoImage(file="images/entrar.png")
senha = PhotoImage(file="images/quadra.png")
logo = PhotoImage(file="images/Untitled-1.png")

TopFrame = Frame(jan, width=500, height=250, relief="raise")
TopFrame.pack(side=TOP)

BotFrame = Frame(jan, width=500, height=350, relief="raise")
BotFrame.pack(side=BOTTOM)

LogoLabel = Label(TopFrame, image=logo)
LogoLabel.place(x=215, y=140)

UserLabel = Label(BotFrame, image=nome)
UserLabel.place(x=110, y=50)

UserEntry = ttk.Entry(BotFrame, width=35)
UserEntry.place(x=160, y=60)

SenhaLabel = Label(BotFrame, image=senha)
SenhaLabel.place(x=110, y=100)

SenhaEntry = ttk.Entry(BotFrame, width=35, show="•")
SenhaEntry.place(x=160, y=110)


def login():
    User = UserEntry.get()
    Pass = SenhaEntry.get()

    database.cursor.execute("""
            SELECT * FROM usuarios WHERE (nome = ? AND senha = ?)
            """, (User, Pass))

    verificar = database.cursor.fetchone()

    try:
        if (User in verificar and Pass in verificar):
            messagebox.showinfo(title="Login Info", message="Logado Com Sucesso, Bem Vindo!")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso Negado. Registre-se!")


LoginButton = ttk.Button(BotFrame, text="Entrar", width=25, command=login)
LoginButton.place(x=180, y=150)


def cadastro():
    UserLabel.place(x=99999)
    UserEntry.place(x=99999)
    SenhaEntry.place(x=99999)
    SenhaLabel.place(x=99999)
    LoginButton.place(x=99999)
    RegisterButton.place(x=99999)

    EmailLabel = Label(BotFrame, text="E-mail:", font=("Century Gothic", 20))
    EmailLabel.place(x=110, y=150)

    EmailEntry = ttk.Entry(BotFrame, width=35)
    EmailEntry.place(x=210, y=162)

    SLabel = Label(BotFrame, text="Senha:", font=("Century Gothic", 20))
    SLabel.place(x=110, y=100)

    SEntry = ttk.Entry(BotFrame, width=35)
    SEntry.place(x=210, y=63)

    ULabel = Label(BotFrame, text="Nome:", font=("Century Gothic", 20))
    ULabel.place(x=110, y=50)

    UEntry = ttk.Entry(BotFrame, width=35, show="•")
    UEntry.place(x=210, y=112)

    def RegisterBD():
        Nome = UEntry.get()
        Email = EmailEntry.get()
        Senha = SEntry.get()

        if (Nome == "" or Email == "" or Senha == ""):
            messagebox.showerror(title="Register Error", message="Preencha todos os campos.")

        else:
            database.cursor.execute("""
                                INSERT INTO usuarios(nome, email, senha) VALUES (?, ?, ?)
                            """, (Senha, Email, Nome))

            database.conn.commit()

            messagebox.showinfo(title="Register Info", message="Conta criada com sucesso!!!")

    RButton = ttk.Button(BotFrame, text="Registrar", width=25, command=RegisterBD)
    RButton.place(x=205, y=200)

    def Back():
        EmailEntry.place(x=99999)
        EmailLabel.place(x=99999)
        RButton.place(x=99999)
        Back.place(x=99999)
        SLabel.place(x=99999)
        SEntry.place(x=99999)
        ULabel.place(x=99999)
        UEntry.place(x=99999)

        RegisterButton.place(x=150)

        LoginButton.place(x=180)

        SenhaLabel = Label(BotFrame, image=senha)
        SenhaLabel.place(x=110, y=100)

        SenhaEntry = ttk.Entry(BotFrame, width=35, show="•")
        SenhaEntry.place(x=160, y=110)

        UserLabel = Label(BotFrame, image=nome)
        UserLabel.place(x=110, y=50)

        UserEntry = ttk.Entry(BotFrame, width=35)
        UserEntry.place(x=160, y=60)

    Back = ttk.Button(BotFrame, text="Voltar", width=35, command=Back)
    Back.place(x=172, y=230)


RegisterButton = ttk.Button(BotFrame, text="Registrar", width=35, command=cadastro)
RegisterButton.place(x=150, y=180)

jan.mainloop()
