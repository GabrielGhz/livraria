class Livraria:
    def __init__(self, nome, editora, quant_pag, idioma, tipo, status, estoque):
        self.__nome = nome
        self.__editora = editora
        self.__quant_pag = quant_pag
        self.__idioma = idioma
        self.__tipo = tipo.lower()
        self.__status = status.lower()
        self.__estoque = self.limite_estoque(estoque)
        self.__alugados = 0
        self.__vendidos = 0
        self.__limite_estoque_livros = 100

    @property
    def livros_alugados(self):
        return self.__alugados

    @livros_alugados.setter
    def livros_alugados(self, qntd):
        if qntd > 0 and qntd + self.estoque == self.__limite_estoque_livros:
            self.__alugados = qntd
        else:
            print("valor inválido")
    
    @property
    def livros_vendidos(self):
        return self.__vendidos

    @livros_vendidos.setter
    def livros_vendidos(self, qntd):
        if qntd > 0 and qntd + self.estoque == self.__limite_estoque_livros:
            self.__vendilivros_vendidos = qntd
        else:
            print("valor inválido")

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def editora(self, nova_editora):
        if nova_editora.isnumeric():
            print("please do not enter numbers but letters")
        else:
            self.__editora = nova_editora

    @property
    def quant_pag(self):
        return self.__quant_pag
    
    @quant_pag.setter
    def quant_pag(self, new_numeral):
        if type(new_numeral) == type(str()):
            print("please do not enter letters but numbers ")
        else:
            self.__quant_pag = new_numeral

    @property
    def idioma(self):
        return self.__idioma
    
    @idioma.setter
    def idioma(self, new_language):
        self.__nome = new_language

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, novo_tipo):
        if novo_tipo == 0:
            self.__tipo = "alugar"
            print("Modificado para aluguel")
        elif novo_tipo == 1:
            self.__tipo = "venda"
            print("Modificado para venda")
        else:
            print("Impossível modificar, chame o reponsável da loja")
        
    @property
    def limite_do_estoque(self):
        return self.__limite_estoque_livros
    
    @limite_do_estoque.setter
    def limite_do_estoque(self, novo_limite):
        if novo_limite > 0 and novo_limite <= 1000:
            self.__limite_estoque_livros = novo_limite
        else:
            print("inválido")

    def limite_estoque(self, quantidade):
        if quantidade > 0 and quantidade <= 100:
            return quantidade
        else:
            raise ValueError("Limite max de 100, dados inválidos")

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, novo_status):
        if novo_status == 0:
            self.__status = "disponivel"
            print("Modificado para disponivel")
        elif novo_status == 1:
            self.__status = "indisponivel"
            print("Modificado para indisponivel")
        else:
            raise ValueError("impossível modificar, chame o responsável da loja")

    @property
    def estoque(self):
        return self.__estoque

    @estoque.setter
    def estoque(self, novo_estoque):
        if novo_estoque + self.__estoque <= self.__limite_estoque_livros:
            self.__estoque += novo_estoque
        else:
            print("O limite no estoque foi excedido!") 

    def alugar(self, qntd=0):
        if self.__tipo == "alugar" and self.__status == "disponivel":
            if qntd > 0 and qntd <= self.__estoque:
                self.__estoque -= qntd
                print("seu livro foi alugado, volte daqui a 7 dias para renovar o aluguel ou somente devolve-lo")
                self.__alugados += qntd
            else:
                print("Você não pode alugar essa quantidade de livros, aqui esta a quantia no estoque atual: \n{}" .format(self.__estoque))
        elif self.__status == "indisponivel":
            print("Esse livro esta indisponivel")
        else:
            print("Você esta tentando comprar um livro que é para alugar")

    def vender(self, qntd=0):
        if self.__tipo == "venda" and self.__status == "disponivel":
            if qntd > 0 and qntd <= self.__estoque:
                self.__estoque -= qntd
                print("Obrigado pela compra do livro, volte sempre!!")
                self.__vendidos += qntd
            else:
                print("Não temos essa capacidade de livros para vender, aqui esta a quantida no estoque atual: \n{}" .format(self.__estoque))
        elif self.__status == "indisponivel":
            print("Esse livro esta indisponivel")
        else:
            print("Você esta tentando alugar um livro que é para venda")
            
    def devolver_livro(self, qntd = 0):
        if qntd > 0 and qntd + self.__estoque <= self.__limite_estoque_livros:
            self.__estoque += qntd
        else:
            print("você esta devolvendo livros a mais! veja se está correto")

    def __str__(self):
        return f"O livro é: {self.__nome}\nSua editora: {self.editora}\nAs quantidades de Páginas: {self.__quant_pag}\nSeu tipo atual é para {self.__tipo} mas pode ser modificado para venda ou aluguel\nSeu status: {self.__status}\nE o estoque atual: {self.estoque}"


class Manga(Livraria):
    def __init__(self, nome, editora, quant_pag, idioma, tipo, status, estoque):
        super().__init__(nome, editora, quant_pag, idioma, tipo, status, estoque)
    pass

class Livro(Livraria):
    def __init__(self, nome, editora, quant_pag, idioma, tipo, status, estoque):
        super().__init__(nome, editora, quant_pag, idioma, tipo, status, estoque)
    pass

livro1 = Livro("Pequeno principe", "SARAIVA", 300, "portugues", "Venda", "disponivel", 100)
livro1.vender(12)
livro1.vender(88)
livro1.alugar(90)
livro1.tipo = 0
livro1.tipo = 2
print(livro1.livros_vendidos)
livro1.limite_do_estoque = 1232323
print(livro1)