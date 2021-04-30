<h2> Explicando o problema</h2>

O problema consiste em criar algumas métricas com base nas informações contidas nos CSV <a href="https://github.com/gLeitao/mobi7/blob/main/bases/base_pois_def.csv"> base_pois_def.csv</a> e <a href="https://github.com/gLeitao/mobi7/blob/main/bases/posicoes.csv"> posicoes.csv</a>, possibilitando uma analise mais aprofundada das informações. 

</br>

As métricas a serem criadas são:

    • Quantidade de tempo que os veículos passaram parados dentro de cada POI;
    • Quantidade de tempo que os veículos estavam dentro de cada POI;
    • Tempo total da frota gasto parado em cada POI;
    • Tempo total parado por veículo, independente do POI.

</br>

Para isso, foi criado o ETL <a href="https://github.com/gLeitao/mobi7/blob/main/etl_poi.py"> etl_poi.py </a>, que le os arquivos CSV, faz o tratamento de dado necessário e agrupa as informações com base nas métricas disponibilizando o resultado no arquivo arquivo <a href="https://github.com/gLeitao/mobi7/blob/main/%20resultados_consolidado_pois.csv">resultados_consoidados_pois.csv</a>.

</br>

<h2>Requisitos necessários para rodar o programa</h2>

    • Instalar as bibliotecas listadas abaixo:

        ◦ pip install pandas
        ◦ pip install geopy
        ◦ pip install DateTime

    • Baixar o projeto <a href=”https://github.com/gLeitao/mobi7”> mobi7 </a>

</br>

<h2> Resultados Obtidos </h2>
Como dito anteriormente, o programa <a href="https://github.com/gLeitao/mobi7/blob/main/etl_poi.py">etl_poi.py</a> irá gerar o arquivo
<a href="https://github.com/gLeitao/mobi7/blob/main/%20resultados_consolidado_pois.csv"> resultados_consolidados_pois.csv</a>. 

</br>

O qual terá contido os campos:

<table>
    <tr>
        <th>placa</th>
        <th>Placa do Veículo</th>
    </tr>
    <tr>
        <th>poi</th>
        <th>Nome do POI</th>
    </tr>
    <tr>
        <th>tempo_parado_poi</th>
        <th>Tempo em que o veículo ficou parado no POI (em minutos)</th>
    </tr>
    <tr>
        <th>tempo_total_poi</th>
        <th>Tempo em que o veículo ficou no POI (em minutos)</th>
    </tr>
    <tr>
        <th>nivel</th>
        <th>Nível de consolidação da informação: 1 – Placa e POI; 2 – POI; 3 – Placa</th>
    </tr>
</table>
