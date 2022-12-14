#def hora_entrada(entrada):
#    if int(entrada[0:2]) >= 0 and int(entrada[0:2]) < 24 and int(entrada[3:5]) >= 0 and int(entrada[3:5]) < 60:
#        converte_hora = converte(int(entrada[0:2]))
#        minutos = converte_hora + int(entrada[3:5])
#        self.__hora_entrada = minutos
#    else:
#        print("Verifique sua batida de ENTRADA!!!")
from datetime import timedelta

class Data:
    def __init__(self):
        self.__data_ent = ""
        self.__data_rec = ""
        self.__multa_p_dia = 0

    def get_data_ent(self):
        return self.__data_ent

    def set_data_ent(self, valor):
        if int(valor[0:2]) >= 1 and int(valor[0:2] <= 30):
            data = valor
            return data

    def get_data_rec(self):
        return self.__data_rec

    def set_data_rec(self,valor):
        if int(valor[0:2]) >= 1 and int(valor[0:2]) <= 30:
            if self.multa_p_dia >= 1:
                valor_multa = self.multa_p_dia * 3
                print("De acordo com o sistema, você atrasou a entrega do livro, deverá pagar uma multa de: \n" + valor_multa + "\n Esse é o valor dos Dias passados por 3")
            else:
                print("Muito obrigado ;)")

    def get_multa_p_dia(self):
        return self.__multa_p_dia
             
    def set_multa_p_dia(self, val1, val2) -> str:
        dia_atras = int(val1[0:2]) - int(val2[0:2])
        self.__multa_p_dia = abs(dia_atras)

    data_ent = property(get_data_ent, set_data_ent)
    data_rec = property(get_data_rec, set_data_rec)
    multa_p_dia = property(get_multa_p_dia, set_multa_p_dia)