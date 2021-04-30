import pandas as pd
from geopy.distance import great_circle
import datetime as dt

# importando os arquivos de origen das informações
df_posicoes = pd.read_csv('bases/posicoes.csv')
df_pois = pd.read_csv('bases/base_pois_def.csv')

# procedimento para pegar o nome POI de cada veiculo
#
# params: long -> longitude de um determinado ponto
#         lat  -> latitude de um determinado ponto  
#
# return: retorna o nome do POI referente as cordenadas passadas por parametro
#
def get_poi(long, lat):
    for row in df_pois.iterrows():
        if great_circle((long, lat), (row[1][3], row[1][2]), ).meters <= row[1][1]:
            return row[1][0]

# procedimento para formatar a data
#
# params: date -> data a ser formatada
#
# return: retorna a data data no padrão yyyy-mm-dd HH:MM:SS
def get_date(date):
    return dt.datetime.strptime(date.replace(" (Hora oficial do Brasil)", ""), '%a %b %d %Y %H:%M:%S GMT-0200')

# procedimento para retornar o estado do veiculo
#
# params: ignicao -> indicador de ignicao ligada ou deseligada
#         velocidade -> velocidade informada do veiculo
#
# return: retorna o estado do veiculo   (Parado ou Andando)   
def get_status(ignicao, velocidade):
    if ignicao == False & velocidade < 5:
        return 'Parado'
    else:
        return 'Andando'

# procedimento para pegar o tempo em que cada veiculo ficou em um determiado estado (Parado ou Andando)
#
# params: poi    -> nome do POI
#         placa  -> placa do veiculo
#         status -> estado do veiculo em que se deseja fazer a consulta de horas gastas (Parado ou Andando)
#
# return: retorna o tempo gasto, em minutos, de um veiculo em determiado poi no estado solicitado (Parado ou Andando)
def get_time(poi, placa, status):
    time = []
    change = True
    stop_time = 0
    
    if status == 'Parado':
        d_status = {1: 'Parado',
                    2: 'Andando'}
    else:
        d_status = {1: 'Andando',
                    2: 'Parado'}
        
    
    for row in df_posicoes[(df_posicoes.poi == poi) & (df_posicoes.placa == placa)].iterrows():
        if row[1][7] == d_status[1]:
            time.append(row[1][1])
            change = True
        
        elif (row[1][7] == d_status[2]) & (change == True) & (len(time) > 0):
            time.sort()
            duration = time[-1] - time[0]
            stop_time += divmod(duration.total_seconds(), 60)[0] 
            
            time   = []
            change = False
            
    return stop_time

# aplica procedimentos para tratar os dados obtidos originalmente
df_posicoes['poi'] = df_posicoes.apply(lambda x: get_poi(x['longitude'], x['latitude']), axis=1)
df_posicoes['data_posicao'] = df_posicoes['data_posicao'].apply(get_date)
df_posicoes['status'] = df_posicoes.apply(lambda x: get_status(x['ignicao'], x['velocidade']), axis=1)

# consolida as informacoes por POI e PLACA
df_consolidate = df_posicoes[df_posicoes['poi'].str.contains('PONTO', na=False)][['placa','poi']].drop_duplicates()
df_consolidate.reset_index(inplace=True, drop=True)

# busca informacoes de tempo gasto Parado e Andando para cada Placa e POI
df_consolidate['tempo_parado_poi']  = df_consolidate.apply(lambda x: get_time(x['poi'], x['placa'], 'Parado'), axis=1)
df_consolidate['tempo_andando_poi'] = df_consolidate.apply(lambda x: get_time(x['poi'], x['placa'], 'Andando'), axis=1)
df_consolidate['tempo_total_poi']   = df_consolidate['tempo_parado_poi'] + df_consolidate['tempo_andando_poi']
df_consolidate['nivel'] = 1

# consolida os tempos de veiculos parados agrupando por POI
df_consolidate_poi = df_consolidate[['poi','tempo_parado_poi']].groupby(['poi']).sum()
df_consolidate_poi.reset_index(inplace=True)
df_consolidate_poi['nivel'] = 2

# consolida os tempos de veiculos parados agrupando por placa
df_consolidate_placa = df_consolidate[['placa','tempo_parado_poi']].groupby(['placa']).sum()
df_consolidate_placa.reset_index(inplace=True)
df_consolidate_placa['nivel'] = 3

# concatena as informações dos tres niveis de informações obtidos em um unico dataframe
df = pd.concat([df_consolidate, df_consolidate_poi, df_consolidate_placa], sort=False)
df.drop('tempo_andando_poi', axis='columns', inplace=True)

# faz uma limpeza em informações nulas 
values = {'placa': '', 'poi': '', 'tempo_parado_poi': 0, 'tempo_total_poi': 0}
df.fillna(value=values, inplace=True)

# exporta o dataset gerado para 
df.to_csv(' resultados_consolidado_pois.csv', index=False)



