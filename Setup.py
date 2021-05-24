#Pega variveis do arquivo GameConfig.json
import json

def LoadConfig():
    # read file
    with open('GameConfig.json', 'r') as arquivo_com_configuracoes:
        data=arquivo_com_configuracoes.read()
    # parse file
    return json.loads(data)