def IdadeAtual(nome,datanasc):
    from datetime import datetime, date
    if not nome or nome.isspace():
        print("Por favor digite um nome")
        return False
    try:
        datanasc = datetime.strptime(datanasc,"%d/%m/%Y").date()
    except:
        print("Formato de data inválida")
        return None
    
    dataatual= date.today()
    if(datanasc > dataatual):
        print("Por favor digite um Ano válido")
        return False
    idade= dataatual.year - datanasc.year
    print(nome+" você tem  ",idade," anos.")
    return idade

nome = input("Nome: ")
d1 = input("Data Nascimento(dia/mes/ano): ")
IdadeAtual(nome,d1)
