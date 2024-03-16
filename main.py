import subprocess
import time
from datetime import datetime
from dbConnect import DataBaseConnection

conexao = DataBaseConnection()
connection = conexao.connection

sites = ['google.com', 'bing.com', 'yahoo.com']

def ping_site(site):
    try:
        ping = subprocess.run(f'ping -n 1 {site}', text=True, capture_output=True, shell=True)
    except Exception as e:
        print(f"Erro ao Executar o ping: {e}")
    return ping.stdout

while(True):
    time.sleep(2)
    for site in sites:
        tempo_resposta   = ping_site(site)
        site_pos_inicial = tempo_resposta.find(site)
        site_pos_final   = tempo_resposta.find(']')
        site             = tempo_resposta[site_pos_inicial:site_pos_final+1]
        pos_tempo        = tempo_resposta.find('=')
        tempo            = tempo_resposta[pos_tempo+1]


        print('-' * 50)

        agora = datetime.now()
        data_hora_formatada = agora.strftime('%Y-%m-%d %H:%M:%S')
        conexao.inserir(tempo, site, data_hora_formatada)
    print('=' * 50)