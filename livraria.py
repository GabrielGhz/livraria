import re
class Livraria:
    def __init__(self):
        self.__data_ent = ""
        self.__data_rec = ""
    padrao = re.compile("[0-9]{2}[/][0-9]{2}")
    
    def valida_data(self, valor):
        busca = self.padrao.search(valor).group
        return busca

    def get_data_ent(self):
        return self.__data_ent

    def set_data_ent(self, valor):
        if self.valida_data(valor):
            if int(valor[0:2]) >= 1 and int(valor[0:2]) <= 30:
                print("Obrigado pela compra ;)")
                self.__data_ent = valor
            else:
                print("Valor inválido, tente novamente")

    def get_data_rec(self):
        return self.__data_rec

    def set_data_rec(self, valor) -> str:
        if int(valor[0:2]) >= 1 and int(valor[0:2]) <= 30:
            dias = self.cal_multa(self.data_ent, valor)
            if dias >= 1:
                valor_multa = dias * 2.5
                print(f"De acordo com o sistema, você atrasou {dias} dias para entregar o livro \nVocê deverá pagar uma multa de: \nR${valor_multa} \nEsse valor é gerado a partir dos dias pós vencimento da entrega Multiplicado por R$2,50")
            elif dias == 0:
                print("Muito obrigado pela devolução;)")
        else:
            print("Valor inválido, tente novamente")

    def trans_mes_dia(self, val):
        # pega os meses Ex:("**/03"), /o valor não pode passar de 12/ para transformar em dias totais
        if int(val[3:5]) >=1 and int(val[3:5]) <= 12:
            dias = (int(val[3:5]) - 1) * 30
            return dias

    def cal_multa(self, val1, val2):
        #soma os dias dos meses com os dias do mes atual
        di_tot1 = self.trans_mes_dia(val1) + int(val1[0:2])
        di_tot2 = self.trans_mes_dia(val2) + int(val2[0:2])
        dia_atras = di_tot1 - di_tot2
        dia_atras = abs(dia_atras)
        if dia_atras > 7:
            dia_atras -= 7
            return dia_atras
        else:
            return 0

    data_ent = property(get_data_ent, set_data_ent)
    data_rec = property(get_data_rec, set_data_rec)

class Livro(Livraria):
    def __init__(self, nome, nm_pag, idioma, edit, tipo, status):
        super().__init__()
        self.__nome = nome
        self.__nm_pag = nm_pag
        self.__idioma = idioma
        self.__edit = edit
        self.__tipo = tipo
        self.__status = status

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if type(nome) == str:
            self.__nome = nome
        else:
            raise ValueError("VALOR INVÁLIDO")
    
    def get_nm_pag(self):
        return self.__nm_pag
    
    def set_nm_pag(self, valor):
        if valor > 0:
            self.__nm_pag = valor
        else:
            raise ValueError("VALOR INVALIDO")
    
    def get_idioma(self):
        return self.__idioma

    def set_idioma(self, idioma):
        if type(idioma) == str:
            self.__idioma = idioma
        else:
            raise ValueError("VALOR INVÁLIDO")
    
    def get_edit(self):
        return self.__edit

    def set_edit(self, edit):
        if type(edit) == str:
            self.__edit = edit
        else:
            raise ValueError("VALOR INVÁLIDO")    
    
    def get_tipo(self):
        return self.__tipo
    
    def set_tipo(self, valor):
        if valor == True:
            raise ValueError("NÃO É POSSÍVEL ALTERAR O TIPO DO LIVRO JÁ CADASTRADO")

    def get_status(self):
        return self.__status
    
    def set_status(self, valor):
        if valor == 0:
            print("Modificado para indisponivel")
            valor = "indisponivel"
            self.__status = valor
        elif valor == 1:
            print("Modificado para disponivel")
            valor = "disponivel"
            self.__status = valor
        else:
            raise ValueError("VALOR INVÁLIDO")

    def __str__(self):
        return "Nome do Livro: {}\nQuantidade de páginas: {}\nIdioma: {}\nEditora: {}\nEle esta para: {}\nNo momento esta: {}" .format(self.nome, self.nm_pag, self.idioma, self.edit, self.tipo, self.status)

    nome = property(get_nome, set_nome)
    nm_pag = property(get_nm_pag, set_nm_pag)
    idioma = property(get_idioma, set_idioma)
    edit = property(get_edit, set_edit)
    tipo = property(get_tipo, set_tipo)
    status = property(get_status, set_status)

class Revista(Livro):
    def __init__(self, nome, nm_pag, idioma, edit, tipo, status):
        super().__init__(self, nome, nm_pag, idioma, edit, tipo, status)

livro1 = Livro("As teorias de Darwin", 200, "portugues", "desconhecido", "alugar", "disponivel")
print(livro1)
livro1.data_ent = "03/09"
print("*" * 50)
livro1.status = 0
print("*" * 50)
livro1.data_rec = "12/12"
print("*" * 50)
livro1.status = 1
print("*" * 50)
print(livro1)
print("*" * 50)
