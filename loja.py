# Programação Orientada a Objetos
# AC03 ADS-EaD - Implementação de classes, herança, polimorfismo e lançamento de exceções.
#
# Email Impacta: rogerkechichian@aluno.faculdadeimpacta.com.br


class Produto:

    def __init__(self, nome, preco):

        self.nome = nome
        self.preco = preco

    @property
    def nome(self):

        return self.__nome

    @property
    def preco(self):

        return self.__preco

    @nome.setter
    def nome(self, novo_nome):

        if (len(novo_nome) == 0):
            raise ValueError

        self.__nome = novo_nome

    @preco.setter
    def preco(self, novo_preco):

        if (isinstance(novo_preco, int) or isinstance(novo_preco, float)):
            if(novo_preco < 0):
                raise ValueError
            self.__preco = novo_preco
        else:
            raise TypeError

    def calcular_preco_com_frete(self):

        return self.__preco


class ProdutoFisico(Produto):

    def __init__(self, nome, preco, peso):

        super().__init__(nome, preco)
        self.peso = peso

    @property
    def peso(self):

        return self.__peso

    @peso.setter
    def peso(self, novo_peso):

        if (isinstance(novo_peso, int)):
            if (novo_peso <= 0):
                raise ValueError
            self.__peso = novo_peso
        else:
            raise TypeError

    def peso_em_kg(self):

        return self.peso/1000.0

    def calcular_preco_com_frete(self):

        return self.preco + 5*self.peso_em_kg()


class ProdutoEletronico(ProdutoFisico):

    def __init__(self, nome, preco, peso, tensao, tempo_garantia):

        super().__init__(nome, preco, peso)
        self.tensao = tensao
        self.__tempo_garantia = tempo_garantia

    @property
    def tensao(self):

        return self.__tensao

    @property
    def tempo_garantia(self):

        return self.__tempo_garantia

    @tensao.setter
    def tensao(self, nova_tensao):

        if (isinstance(nova_tensao, int)):
            if (nova_tensao in [0, 127, 220]):
                self.__tensao = nova_tensao
            else:
                raise ValueError
        else:
            raise TypeError

    def calcular_preco_com_frete(self):

        return super().calcular_preco_com_frete()*1.01


class Ebook(Produto):

    def __init__(self, nome, preco, autor, numero_paginas):

        super().__init__(nome, preco)
        self.__autor = autor
        self.__numero_paginas = numero_paginas

    @property
    def nome_exibicao(self):

        return "%s (%s)" % (self.nome, self.__autor)

    @property
    def numero_paginas(self):

        return self.__numero_paginas

    @numero_paginas.setter
    def numero_paginas(self, valor):

        if (valor <= 0):
            raise ValueError

        self.__numero_paginas = valor
