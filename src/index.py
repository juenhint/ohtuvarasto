from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print((f'''Luonnin jälkeen:\nMehuvarasto: {mehua}\n
    Olutvarasto: {olutta}\nOlut getterit:\nsaldo = {olutta.saldo}\n
    tilavuus = {olutta.tilavuus}\npaljonko_mahtuu = {olutta.paljonko_mahtuu()}\n
    Mehu setterit:\nLisätään 50.7'''))

    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}\nOtetaan 3.14")

    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}\nVirhetilanteita:\nVarasto(-100.0);")

    olutta.lisaa_varastoon(1000.0)
    print(f'''Olutvarasto: {olutta}\nMehuvarasto: {mehua}\n
    mehua.lisaa_varastoon(-666.0)''')

    mehua.lisaa_varastoon(-666.0)
    print(f'''Mehuvarasto: {mehua}\nOlutvarasto: {olutta}\n
    olutta.ota_varastosta(1000.0)''')

    saatiin = olutta.ota_varastosta(1000.0)
    print(f'''saatiin {saatiin}\nOlutvarasto: {olutta}\n
    Mehuvarasto: {mehua}\nmehua.otaVarastosta(-32.9)''')

if __name__ == "__main__":
    main()
