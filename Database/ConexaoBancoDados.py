import sqlite3
import tkinter.messagebox


class ConexaoBancoDados:

    def abrir_conexao(self):
        try:
            conexao = sqlite3.connect(database="BD_CLIENTE")
            self.conexao = conexao
            cursor = conexao.cursor()
            self.cursor = cursor
            print("Conexão aberta.")

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar realizar a conexão com o Banco de Dados.")

    def fechar_conexao(self):
        try:
            self.conexao.close()
            print("Conexão fechada.")
        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar fechar a conexão.")

