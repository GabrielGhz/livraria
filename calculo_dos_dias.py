from datetime import timedelta
#foi
class Data:
    def __init__(self):
        self.__data_ent = ""
        self.__data_rec = ""
        self.__multa_p_dia = abs(0)

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

livro1 = Data()
livro1.data_ent = ("15/23")
print("*"*50)
livro1.data_rec = ("30/23")

