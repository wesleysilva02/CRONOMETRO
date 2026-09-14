from tkinter import *
import tkinter as tk

class Cronometro:
    def __init__(self,janela):
        self.janela = janela
        self.janela.title("Cronômetro")
        self.janela.geometry("470x280")
        self.janela.resizable(False, False)
        self.janela.configure(bg="#C9BDBD")

        #variaveis de estado
        self.tempo_atual ="00:00:00"
        self.segundo = 0
        self.rodando = False
        self.timer_id = None

        self.criar_interface()

    def criar_interface(self):
        container = Frame(self.janela, bg="#F6EDED")
        container.pack(expand=True, fill=BOTH, padx=20, pady=20)

        card = Frame(container, bg="white", relief="ridge", bd=2)
        card.pack(expand=True, fill=BOTH)

        #titulo
        titulo = Label(
            card,
            text="🟢Cronômetro",
            font=("Arial", 16, "bold"),
            fg="#1E1D22",
            bg="white"
        )
        titulo.pack(pady=20, padx=5)

        # display tempo
        self.display = Label(
            card,
            text=self.tempo_atual,
            font=("Arial", 40, "bold"),
            fg="#382293",
            bg="white"
        )
        self.display.pack(pady=15)

#frame botoes
        frame_botoes = Frame(card, bg="white")
        frame_botoes.pack(pady=20)

        #botao iniciar

        self.btn_iniciar = Button(
            frame_botoes,
            command=self.iniciar,
            text="Iniciar",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#4CAF50",
            activebackground="#45A049",
            width=10,
            bd=2,
            relief="raised"
        )

        self.btn_iniciar.grid(row=0, column=0, padx=5)


        self.btn_pausar = Button(
            frame_botoes,
            command=self.pausar,
            text="Pausar",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#FF9800",
            activebackground="#45A049",
            width=10,
                        bd=2,
                        relief="raised"
                )

        self.btn_pausar.grid(row=0, column=1, padx=5)


        self.btn_resetar = Button(
            frame_botoes,
            command=self.resetar,
            text="Resetar",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#F44336",
            activebackground="#45A049",
            width=10,
                        bd=2,
                        relief="raised"
                )

        self.btn_resetar.grid(row=0, column=2, padx=5)


    def atualizar_tempo(self):
        if self.rodando:
            self.segundo += 1
            horas = self.segundo // 3600
            minutos = (self.segundo % 3600) // 60
            segundos = self.segundo % 60
            self.tempo_atual = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
            self.display.config(text=self.tempo_atual)
            self.timer_id = self.janela.after(1000, self.atualizar_tempo)


    def iniciar(self):
        if not self.rodando:
            self.rodando = True
            self.atualizar_tempo()


    def pausar(self):
        if self.rodando:
            self.rodando = False
            if self.timer_id:
                self.janela.after_cancel(self.timer_id)
                self.timer_id = None


    def resetar(self):
        self.pausar()
        self.segundo = 0
        self.tempo_atual = "00:00:00"
        self.display.config(text=self.tempo_atual)  


if __name__ == "__main__":
    janela =tk.Tk()
    app =Cronometro(janela)
    janela.mainloop()