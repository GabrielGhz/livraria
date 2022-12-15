class Livraria:
    def __init__(self):
        self.__data_ent = ""
        self.__data_rec = ""
        self.__multa_p_dia = 0

    def get_data_ent(self):
        return self.__data_ent

    def set_data_ent(self, valor):
        if int(valor[0:2]) >= 1 and int(valor[0:2]) <= 30:
            print("Obrigado, volte daqui a 7 dias para renovar")
            self.__data_ent = valor
        else:
            print("Valor inválido, tente novamente")

    def get_data_rec(self):
        return self.__data_rec

    def set_data_rec(self, valor) -> str:
        if int(valor[0:2]) >= 1 and int(valor[0:2]) <= 30:
            dias = self.cal_multa(self.data_ent, valor)
            if int(dias) >= 1:
                valor_multa = dias * 3
                print(f"De acordo com o sistema, você atrasou {dias} dias para entregar o livro \nVocê deverá pagar uma multa de: \nR${valor_multa},00 \nEsse valor é gerado a partir dos dias pós vencimento da entrega Multiplicado por 3")
            elif int(dias) == 0:
                print("Muito obrigado ;)")
        else:
            print("Valor inválido, tente novamente")

    def cal_multa(self, val1, val2) -> str:
        dia_atras = int(val2[0:2]) - int(val1[0:2])
        dia_atras = abs(dia_atras)
        if dia_atras > 7:
            dia_atras -= 7
        return dia_atras

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
        if valor == 0:
            valor = "alugar"
            self.__tipo = valor
        elif valor == 1:
            valor = "venda"
            self.__tipo = valor
        else:
            raise ValueError("VALOR INVÁLDIO")

    def get_status(self):
        return self.__status
    
    def set_status(self, valor):
        if valor == 0:
            valor = "indisponivel"
            self.__status = valor
        elif valor == 1:
            valor = "disponivel"
            self.__status = valor
        else:
            raise ValueError("VALOR INVÁLDIO")
            
    nome = property(get_nome, set_nome)
    nm_pag = property(get_nm_pag, set_nm_pag)
    idioma = property(get_idioma, set_idioma)
    edit = property(get_edit, set_edit)
    tipo = property(get_tipo, set_tipo)
    status = property(get_status, set_status)

class Revista(Livro):
    def __init__(self, nome, nm_pag, idioma, edit, tipo, status):
        super().__init__(self, nome, nm_pag, idioma, edit, tipo, status)