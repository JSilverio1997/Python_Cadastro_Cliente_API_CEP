

class ClienteGetSetter:

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if nome != "":
            self.__nome = nome

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        if cep.isdigit() and len(cep) == 8:
            self.__cep = cep

    @property
    def logradouro(self):
        return self.__logradouro

    @logradouro.setter
    def logradouro(self, logradouro):
        if logradouro != "":
            self.__logradouro = logradouro

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        if numero != "" and numero.isdigit():
            self.__numero = numero

    @property
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self, complemento):
        if complemento != "":
            self.__complemento = complemento
        else:
            self.__complemento = None

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        if bairro != "":
            self.__bairro = bairro

    @property
    def localidade(self):
        return self.__localidade

    @localidade.setter
    def localidade(self, localidade):
        if localidade != "":
            self.__localidade = localidade

    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self, uf):
        if uf != "":
            self.__uf = uf

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, celular):
        if celular != "":
            if celular.isdigit():
                self.__celular = celular
        else:
            self.__celular = None

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        if telefone != "":
            if telefone.isdigit():
                self.__telefone = telefone
        else:
            self.__telefone = None
