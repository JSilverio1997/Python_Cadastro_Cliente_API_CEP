import tkinter.messagebox
from tkinter import *
from Functions.Endereco import Endereco
from Functions.Cliente import Cliente


class FormCliente:

    def __init__(self, master):
        self.master = master
        self.master.title("Cadastrar Clientes")
        self.criar_componentes(master)

    def criar_componentes(self, janela):
        lbl_titulo = Label(text="Cadastro de Clientes", font="arial, 18", bg="#6495ED")
        lbl_titulo.grid(row=2, column=3, columnspan=20, pady=5)

        canvas_image = Canvas(janela, width=225, height=225)
        bg_image = PhotoImage(file=r"Imagens/ImagemCliente.png")
        canvas_image.create_image((0, 0), image=bg_image, anchor=NW)
        canvas_image.image = bg_image
        canvas_image.grid(row=4, column=3, columnspan=20, pady=5)

        lbl_nome = Label(text="\t            Nome:", font="arial, 14", bg="#6495ED")
        lbl_nome.grid(row=6, column=2, pady=2)

        lbl_cep = Label(text="\t             " + "CEP:", font="arial, 14", bg="#6495ED")
        lbl_cep.grid(row=8, column=2, pady=2)

        lbl_logradouro = Label(text="\t  Logradouro:", font="arial, 14", bg="#6495ED")
        self.lbl_logradouro = lbl_logradouro

        lbl_numero = Label(text="\t        Número:", font="arial, 14", bg="#6495ED")
        self.lbl_numero = lbl_numero

        lbl_complemento = Label(text="               Complemento:", font="arial, 14", bg="#6495ED")
        self.lbl_complemento = lbl_complemento

        lbl_bairro = Label(text="\t           Bairro:", font="arial, 14", bg="#6495ED")
        self.lbl_bairro = lbl_bairro

        lbl_localidade = Label(text="\t  Localidade:", font="arial, 14", bg="#6495ED")
        self.lbl_localidade = lbl_localidade

        lbl_uf = Label(text="\t               UF:", font="arial, 14", bg="#6495ED")
        self.lbl_uf = lbl_uf

        lbl_celular = Label(text="\t        Celular:", font="arial, 14", bg="#6495ED")
        self.lbl_celular = lbl_celular

        lbl_telefone = Label(text="\t     Telefone:", font="arial, 14", bg="#6495ED")
        self.lbl_telefone = lbl_telefone

        txt_nome = Entry(width="25", font="arial")
        txt_nome.grid(row=6, column=3, pady=2)
        txt_nome.focus()
        self.txt_nome = txt_nome

        txt_cep = Entry(width="25", font="arial")
        txt_cep.grid(row=8, column=3, pady=2)
        self.txt_cep = txt_cep

        txt_logradouro = Entry(width="25", font="arial,12bold")
        txt_logradouro.configure(state="read")
        self.txt_logradouro = txt_logradouro

        txt_numero = Entry(width="25", font="arial,12bold")
        self.txt_numero = txt_numero

        txt_complemento = Entry(width="25", font="arial,12bold")
        self.txt_complemento = txt_complemento

        txt_bairro = Entry(width="25", font="arial,12bold")
        txt_bairro.configure(state="read")
        self.txt_bairro = txt_bairro

        txt_localidade = Entry(width="25", font="arial,12bold")
        txt_localidade.configure(state="read")
        self.txt_localidade = txt_localidade

        txt_uf = Entry(width="25", font="arial,12bold")
        txt_uf.configure(state="read")
        self.txt_uf = txt_uf

        txt_celular = Entry(width="25", font="arial,12bold")
        self.txt_celular = txt_celular

        txt_telefone = Entry(width="25", font="arial,12bold")
        self.txt_telefone = txt_telefone

        btn_confirmar = Button(text="Confirmar", width="18", font="arial", command=self.obter_dados_endereco)
        btn_confirmar.grid(row=20, column=3, columnspan=2, padx=3, pady=5)
        self.btn_confirmar = btn_confirmar

        btn_limpar = Button(text="Limpar", width="18", font="arial", command=self.limpar_componetes_iniciais)
        btn_limpar.grid(row=21, column=3, columnspan=2, padx=3, pady=5)
        self.btn_limpar = btn_limpar

        btn_gerar_relatorio = Button(text="Relatório", width="18", font="arial", command=self.gerar_relatorio)
        btn_gerar_relatorio.grid(row=24, column=3, columnspan=2, padx=3, pady=5)
        self.btn_gerar_relatorio = btn_gerar_relatorio

        btn_cadastrar = Button(text="Cadastrar", width="18", font="arial", command=self.cadastrar_cliente)
        self.btn_cadastrar = btn_cadastrar

    def exibir_componentes(self):
        self.btn_confirmar.grid_remove()
        self.btn_gerar_relatorio.grid_remove()

        self.lbl_logradouro.grid(row=10, column=2, pady=2)
        self.lbl_numero.grid(row=11, column=2, pady=2)
        self.lbl_complemento.grid(row=12, column=2, pady=2)
        self.lbl_bairro.grid(row=14, column=2, pady=2)
        self.lbl_localidade.grid(row=16, column=2, pady=2)
        self.lbl_uf.grid(row=17, column=2, pady=2)
        self.lbl_celular.grid(row=18, column=2, pady=2)
        self.lbl_telefone.grid(row=19, column=2, pady=2)

        self.txt_logradouro.grid(row=10, column=3, pady=2)
        self.txt_numero.grid(row=11, column=3, pady=2)
        self.txt_complemento.grid(row=12, column=3, pady=2)
        self.txt_bairro.grid(row=14, column=3, pady=2)
        self.txt_localidade.grid(row=16, column=3, pady=2)
        self.txt_uf.grid(row=17, column=3, pady=2)
        self.txt_celular.grid(row=18, column=3, pady=2)
        self.txt_telefone.grid(row=19, column=3, pady=2)
        self.btn_cadastrar.grid(row=22, column=3, columnspan=2, padx=3, pady=5)

        self.btn_limpar['command'] = self.limpar_todos_componentes
        self.btn_limpar.grid(row=23, column=3, columnspan=2, padx=3, pady=5)

    def obter_dados_endereco(self):
        nome = self.txt_nome.get()
        cep = self.txt_cep.get().replace(".", "").replace("-", "")

        if nome == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite o seu nome. ")
            self.txt_nome.focus()

        elif cep == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite o CEP.")
            self.txt_cep.focus()

        elif cep.isdigit() is False or len(cep) != 8:
            tkinter.messagebox.showwarning("Atenção", "Por favor digite o CEP de forma válida.")
            self.txt_cep.focus()

        else:
            endereco = Endereco()
            dados = endereco.obter_dados_endereco(cep)
            if dados is not None:
                self.exibir_componentes()
                self.ativar_componentes_endereco(ativar=True)

                self.txt_cep.delete(0, len(self.txt_cep.get()))
                self.txt_cep.insert(0, dados[0])
                self.txt_cep.configure(state="read")

                self.txt_logradouro.insert(1, dados[1])
                self.txt_bairro.insert(2, dados[3])
                self.txt_localidade.insert(3, dados[4])
                self.txt_uf.insert(4, dados[5])
                self.txt_numero.focus()

                self.ativar_componentes_endereco(ativar=False)

            else:
                tkinter.messagebox.showwarning("Atenção", "O CEP Digitado é inválido.")
                self.txt_cep.focus()

    def ativar_componentes_endereco(self, ativar):
        if ativar:
            self.txt_logradouro.configure(state="normal")
            self.txt_bairro.configure(state="normal")
            self.txt_localidade.configure(state="normal")
            self.txt_uf.configure(state="normal")

        else:
            self.txt_logradouro.configure(state="read")
            self.txt_bairro.configure(state="read")
            self.txt_localidade.configure(state="read")
            self.txt_uf.configure(state="read")

    def cadastrar_cliente(self):
        try:

            erro_numero_celular = False
            erro_numero_telefone = False
            nome = self.txt_nome.get()
            cep = self.txt_cep.get()
            logradouro = self.txt_logradouro.get()
            numero = self.txt_numero.get()
            complemento = self.txt_complemento.get()
            bairro = self.txt_bairro.get()
            localidade = self.txt_localidade.get()
            uf = self.txt_uf.get()
            celular = self.txt_celular.get().replace("-", "").replace(".", "")
            telefone = self.txt_telefone.get().replace("-", "").replace(".", "")

            if numero == "":
                tkinter.messagebox.showwarning("Atenção", "Por favor digite o Número da Casa ou Apartamento.")
                self.txt_numero.focus()

            elif numero.isdigit() is False:
                tkinter.messagebox.showwarning("Atenção", "Por favor digite o Número da Casa do Apartamento de forma"
                                                          "válida.")
                self.txt_numero.focus()

            if celular != "":
                if celular.isdigit() is False:
                    try:
                        checar_numero_celular = int(celular)

                    except ValueError:
                        erro_numero_celular = True
                        tkinter.messagebox.showwarning("Atenção",
                                                       "Por favor digite o número do Celular de forma válida.")
                        self.txt_celular.focus()

            if telefone != "":
                if telefone.isdigit() is False:
                    try:
                        checar_numero_telefone = int(telefone)

                    except ValueError:
                        erro_numero_telefone = True
                        tkinter.messagebox.showwarning("Atenção",
                                                       "Por favor digite o número do Telefone de forma válida.")
                        self.txt_telefone.focus()

            if erro_numero_telefone is False and erro_numero_celular is False and numero.isdigit():
                dados_cliente = [nome, cep, logradouro, numero, complemento, bairro, localidade, uf, celular,
                                 telefone]
                cadastrar_cliente = Cliente()
                cadastrar_cliente.cadastrar(dados_cliente)
                tkinter.messagebox.showinfo("Cadastrado", "O Cliente foi cadastrado com sucesso.")
                self.limpar_todos_componentes()

        except():
            tkinter.messagebox.showwarning("Atenção", "Não foi possível cadastrar o Cliente.")

    def limpar_componetes_iniciais(self):
        self.txt_nome.delete(0, len(self.txt_nome.get()))
        self.txt_cep.delete(0, len(self.txt_cep.get()))
        self.txt_nome.focus()

    def limpar_todos_componentes(self):
        self.txt_nome.delete(0, len(self.txt_nome.get()))
        self.txt_cep.configure(state="normal")
        self.txt_cep.delete(0, len(self.txt_cep.get()))

        self.ativar_componentes_endereco(ativar=True)
        self.txt_logradouro.delete(0, len(self.txt_logradouro.get()))
        self.txt_numero.delete(0, len(self.txt_numero.get()))
        self.txt_complemento.delete(0, len(self.txt_complemento.get()))
        self.txt_bairro.delete(0, len(self.txt_bairro.get()))
        self.txt_localidade.delete(0, len(self.txt_localidade.get()))
        self.txt_uf.delete(0, len(self.txt_uf.get()))
        self.txt_celular.delete(0, len(self.txt_celular.get()))
        self.txt_telefone.delete(0, len(self.txt_telefone.get()))
        self.ativar_componentes_endereco(ativar=False)

        self.lbl_logradouro.grid_remove()
        self.lbl_numero.grid_remove()
        self.lbl_complemento.grid_remove()
        self.lbl_bairro.grid_remove()
        self.lbl_localidade.grid_remove()
        self.lbl_uf.grid_remove()
        self.lbl_celular.grid_remove()
        self.lbl_telefone.grid_remove()

        self.txt_logradouro.grid_remove()
        self.txt_numero.grid_remove()
        self.txt_complemento.grid_remove()
        self.txt_bairro.grid_remove()
        self.txt_localidade.grid_remove()
        self.txt_uf.grid_remove()
        self.txt_celular.grid_remove()
        self.txt_telefone.grid_remove()

        self.btn_limpar['command'] = self.limpar_componetes_iniciais
        self.btn_cadastrar.grid_remove()
        self.btn_confirmar.grid(row=20, column=3, columnspan=2, padx=3, pady=5)
        self.btn_gerar_relatorio.grid(row=24, column=3, columnspan=2, padx=3, pady=5)

        self.txt_nome.focus()

    @staticmethod
    def gerar_relatorio():
        relatorio = Cliente()
        relatorio.gerar_relatorio()
        tkinter.messagebox.showinfo("Sucesso", "O Arquivo foi gerado com sucesso.")


def instanciar_form_cliente():
    form_cliente = Tk()
    FormCliente(form_cliente)
    form_cliente.iconbitmap(r"Imagens/IconeCliente.ico")
    form_cliente.resizable(0, 0)
    form_cliente.geometry("620x700+460+0")
    form_cliente.configure(relief="ridge", bg="#6495ED", border=4)
    form_cliente.mainloop()
    exit()


# instanciar_form_cliente()
