import re

# ([0-9]{1,3}.[0-9]{3}.[0-9]{3},[0-9]{2})

anos = ["2019", "2020", "2021", "2022"]

valores = []
for ano in anos:
    with open(f"relatorio{ano}.txt", encoding='latin') as arquivo:
        txt = arquivo.read()
        x = re.findall("([0-9]{1,3}.[0-9]{3}.[0-9]{3},[0-9]{2})", txt)

    for valor in x:
        if "\t" in valor:
            valor = valor[3:].replace(".", "").replace(",", ".")
            valores.append(float(valor))
        else:
            valor = valor.replace(".", "").replace(",", ".")
            valores.append(float(valor))
    
    with open(f"top5maioresgastostaubate{ano}(ATUALIZADO).txt", "a") as arquivo:
        c = 0
        for valor in sorted(valores, reverse=True)[:5]:
            arquivo.write(f"{c}, {valor}\n")
            print(c, valor)
            c += 1