import tkinter.messagebox
from ActionsCRUD.ClienteActions import ClienteActions
from GetSetters.ClienteGetSet import ClienteGetSetter
from datetime import datetime


class Cliente(ClienteGetSetter):

    @staticmethod
    def criar_tabela():
        tabela = ClienteActions()
        tabela.criar_tabela()

    @staticmethod
    def excluir_tabela():
        tabela = ClienteActions()
        tabela.excluir_tabela()

    @staticmethod
    def cadastrar(datas_cliente=[]):
        try:
            nome = datas_cliente[0]
            cep = datas_cliente[1]
            logradouro = datas_cliente[2]
            numero = datas_cliente[3]
            complemento = datas_cliente[4]
            bairro = datas_cliente[5]
            localidade = datas_cliente[6]
            uf = datas_cliente[7]
            celular = datas_cliente[8]
            telefone = datas_cliente[9]

            ClienteGetSetter.nome = nome.title()
            ClienteGetSetter.cep = cep
            ClienteGetSetter.logradouro = logradouro
            ClienteGetSetter.numero = numero
            ClienteGetSetter.complemento = complemento
            ClienteGetSetter.bairro = bairro
            ClienteGetSetter.localidade = localidade
            ClienteGetSetter.uf = uf
            ClienteGetSetter.celular = celular
            ClienteGetSetter.telefone = telefone

            dict_dados_cliente = {"nome": ClienteGetSetter.nome, "cep": ClienteGetSetter.cep,
                                  "logradouro": ClienteGetSetter.logradouro, "numero": ClienteGetSetter.numero,
                                  "complemento": ClienteGetSetter.complemento, "bairro": ClienteGetSetter.bairro,
                                  "localidade": ClienteGetSetter.localidade, "uf": ClienteGetSetter.uf,
                                  "celular": ClienteGetSetter.celular, "telefone": ClienteGetSetter.telefone}

            cadastrar_cliente = ClienteActions()
            cadastrar_cliente.cadastrar(dict_dados_cliente)

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar cadastrar o Cliente.")

    @staticmethod
    def gerar_relatorio():
        try:
            hoje = datetime.today()
            dia = hoje.day
            mes = hoje.month
            ano = hoje.year

            agora = datetime.now()
            horas = agora.hour
            minutos = agora.minute
            segundos = agora.second

            data_horario = f"{dia}/{mes}/{ano} - {horas}:{minutos}:{segundos}"

            arquivo = open("lista_clientes.txt", "w")
            relatorio = ClienteActions()
            dados_cliente = relatorio.gerar_relatorio_clientes()

            arquivo.write("_" * 80 + "\n")
            arquivo.write("\t \t \tRelatório de Clientes\n")
            arquivo.write(f"Data e Horário do Relatório Gerado: {data_horario}\n")
            arquivo.write("_"*80 + "\n")

            if dados_cliente is not None:
                for dados in dados_cliente:
                    nome = dados[0]
                    cep = dados[1]
                    logradouro = dados[2]
                    numero = dados[3]
                    complemento = dados[4]
                    bairro = dados[5]
                    localidade = dados[6]
                    uf = dados[7]
                    celular = dados[8]
                    telefone = dados[9]

                    if complemento is None or complemento == "":
                        complemento = "O Endereço não possuí complemento."

                    if celular is None or celular == "":
                        celular = "O Número do Celular não foi cadastrado."

                    if telefone is None or telefone == "":
                        telefone = "O Número do Telefone não foi cadastrado."

                    arquivo.write(f"Nome: {nome}\n")
                    arquivo.write(f"CEP: {cep}\n")
                    arquivo.write(f"Logradouro: {logradouro}\n")
                    arquivo.write(f"Número: {numero}\n")
                    arquivo.write(f"Complemento: {complemento}\n")
                    arquivo.write(f"Bairro: {bairro}\n")
                    arquivo.write(f"Localidade: {localidade}\n")
                    arquivo.write(f"UF: {uf}\n")
                    arquivo.write(f"Celular: {celular}\n")
                    arquivo.write(f"Telefone: {telefone}\n")
                    arquivo.write("_"*80 + "\n")

                arquivo.write(f"Quantidade de Clientes Cadastrados: {len(dados_cliente)}.\n")

            else:
                arquivo.write(f"Você Não tem Nenhum Cliente Cadastrado.\n")

            if arquivo.closed is False:
                arquivo.close()

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar gerar o relatório.")


"""dados = ["Lucas", "00000-000", "rua: teste 1", "12",
         "", "Teste", "Sao Paulo", "SP", "", ""]"""
# cliente = Cliente()
# cliente.excluir_tabela()
# cliente.criar_tabela()
# cliente.cadastrar(dados)
