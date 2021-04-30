Explicando o problema
O problema consiste em criar algumas métricas com base nas informações contidas nos CSV <a href=”https://github.com/gLeitao/mobi7/blob/main/bases/base_pois_def.csv”> base_pois_def.csv</a> e <a href=”https://github.com/gLeitao/mobi7/blob/main/bases/posicoes.csv”> posições.csv</a> possibilitando uma analise mais aprofundada das informações. 

As métricas a serem criadas são:

    • Quantidade de tempo que os veículos passaram parados dentro de cada POI;
    • Quantidade de tempo que os veículos estavam dentro de cada POI;
    • Tempo total da frota gasto parado em cada POI;
    • Tempo total parado por veículo, independente do POI.

Para isso, foi criado o ETL <a href=”https://github.com/gLeitao/mobi7/blob/main/etl_poi.py”> etl_poi.py </a>, que le os arquivos CSV, faz o tratamento de dado necessário e agrupa as informações com base nas métricas disponibilizando o resultado no arquivo arquivo <a href=”https://github.com/gLeitao/mobi7/blob/main/%20resultados_consolidado_pois.csv”>resultados_consoidados_pois.csv</a>.

Requisitos necessários para rodar o programa
    • Instalar as bibliotecas listadas abaixo:

        ◦ pip install pandas
        ◦ pip install geopy
        ◦ pip install DateTime

    • Baixar o projeto <a href=”https://github.com/gLeitao/mobi7”> mobi7 </a>

Resultados Obtidos
Como dito anteriormente, o programa <a href=”https://github.com/gLeitao/mobi7/blob/main/etl_poi.py”> etl_poi.py </a> irá gerar o arquivo <a href=”https://github.com/gLeitao/mobi7/blob/main/%20resultados_consolidado_pois.csv”>resultados_consoidados_pois.csv</a>. O qual terá contido os campos:

placa
placa do veiculo
poi
nome do POI
tempo_parado_poi
Tempo em que o veiculo ficou parado no POI
tempo_total_poi
Tempo em que o veiculo ficou dentro do POI
nivel
Nível de consolidação da informação:

    • 1 – Placa e POI
    • 2 – POI
    • 3 – Placa


A base foi dividida dessa maneira visando facilitar a análise da informação posteriormente.
