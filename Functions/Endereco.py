import requests
import json
import tkinter.messagebox


class Endereco:

    @staticmethod
    def obter_dados_endereco(cep):
        try:
            requisicao = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            status_requisicao = requisicao.status_code

            if status_requisicao == 200:
                arquivo_json = json.loads(requisicao.text)
                dados_json = dict(arquivo_json).values()

                list_dados_endereco = []

                for (i, valores) in enumerate(dados_json):
                    list_dados_endereco.insert(i, valores)

                # True é o valor que retorna quando tem erro no CEP
                if list_dados_endereco.__contains__(True):
                    return None
                else:
                    return list_dados_endereco

            else:
                tkinter.messagebox.showwarning("Atenção", "Não foi possível recuperar os dados do endereço, "
                                                          "provavelmente este não é um CEP válido.")

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar executar a função para obter dados do Endereço.")


"""teste = Endereco()
print(teste.obter_dados_endereco("04612210"))"""
