import tkinter.messagebox
from Database.ConexaoBancoDados import ConexaoBancoDados


class ClienteActions(ConexaoBancoDados):

    def criar_tabela(self):
        try:
            self.abrir_conexao()
            sql = f"create table cliente(" \
                  f"id_cliente integer primary key autoincrement," \
                  f"nome varchar(250) not null," \
                  f"cep varchar(8) not null," \
                  f"logradouro varchar(250) not null," \
                  f"numero varchar(10) not null," \
                  f"complemento varchar(150)," \
                  f"bairro varchar(200) not null," \
                  f"localidade varchar(250) not null," \
                  f"uf varchar(2) not null," \
                  f"celular varchar(20)," \
                  f"telefone varchar(20));"

            self.cursor.execute(sql)
            print("A Tabela foi criada com sucesso.")
            print(sql)

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar criar a tabela de Cliente.")
        finally:
            self.fechar_conexao()

    def excluir_tabela(self):
        try:
            self.abrir_conexao()
            sql = f"drop table cliente;"
            self.cursor.execute(sql)
            print("A Tabela foi excluida.")

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar excluir a tabela de Cliente.")
        finally:
            self.fechar_conexao()

    def cadastrar(self, dados_cliente={}):
        try:
            self.abrir_conexao()
            sql = (f"insert into cliente (nome, cep, logradouro, numero, complemento, bairro, localidade, uf, "
                   f"celular, telefone ) values('{dados_cliente['nome']}', '{dados_cliente['cep']}'"
                   f",'{dados_cliente['logradouro']}', '{dados_cliente['numero']}', '{dados_cliente['complemento']}'"
                   f", '{dados_cliente['bairro']}','{dados_cliente['localidade']}', '{dados_cliente['uf']}'"
                   f", '{dados_cliente['celular']}', '{dados_cliente['telefone']}'  );")
            self.cursor.execute(sql)
            self.conexao.commit()
            print("Cliente cadastrado com sucesso.")

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar cadastrar o cliente.")
        finally:
            self.fechar_conexao()

    def gerar_relatorio_clientes(self):
        try:
            self.abrir_conexao()
            sql = ("select nome, cep, logradouro, numero, complemento, bairro, localidade, uf, telefone, celular "
                   "from cliente order by nome;")
            self.cursor.execute(sql)
            dados_cliente = self.cursor.fetchall()

            if dados_cliente is not None:
                return dados_cliente
            else:
                return None

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar gerar o relatório de clientes.")
        finally:
            self.fechar_conexao()


"""dados = {"nome": "Lucas", "cep": "00000-000", "logradouro": "rua: teste 1", "numero": "12",
         "complemento": "", "bairro": "Teste", "localidade": "Sao Paulo", "uf": "SP", "celular": "", "telefone": ""}"""
# cliente = ClienteActions()
# cliente.excluir_tabela()
# cliente.criar_tabela()
# cliente.cadastrar(dados)
# cliente.gerar_relatorio_clientes()

