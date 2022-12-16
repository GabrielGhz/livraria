class Livraria:
    def __init__(self):
        self.__data_ent = ""
        self.__data_rec = ""
        self.__multa_p_dia = abs(0)

    def get_data_ent(self):
        return self.__data_ent

    def set_data_ent(self, valor):
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
        if int(val[3:5]) >=1 and int(val[3:5]) <= 12:
            dias = int(val[3:5]) * 30
            return dias

    def cal_multa(self, val1, val2):
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

ob1 = Livraria()
ob1.data_ent = "10/03"

ob1.data_rec = "17/03"