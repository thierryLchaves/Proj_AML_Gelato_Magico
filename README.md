<div style="position: relative; width: 100%;">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=100&color=B2FFFF&section=header&reversal=false&animation=fadeIn" width="100%">
<div>
  <div style="display: flex; align-items: center;">
    <h1 style="margin: 0; font-size: 50px;">Gelato Mágico.</h1>
  </div>
  <p style="margin: 6px 0 0 0; font-size: 25px;">
    Treinando Seu Primeiro Modelo de Machine Learning para Prever Vendas
  </p>
</div>

O documento a seguir descreve o processo de ciração de um modelo de predição de vendas futuras utilizando a plataforma do Azure Machine Learning, durante esse projeto foi utilizado como base o arquivo criado em python, para ciração de dataset (base de dados),sabendo que o objetivo da predição a ser realizada tem como base a quantidade de vendas realizadas conforme a temperatura do dia, foi utilizado então esse código que gera um arquivo **".csv "** , foi criado esse arquivo
[Cria base de dados](src/script_data_set.py). Após a configuração e de ambiente de trabalho, provisioanmento de máquinas, foram utilizadas técnicas distintas para gerar diferentes resultados, 
sendo eles códigos em notebooks python, para computação e criação de scripts e modelos com MLflow, Automated ML com Designer, até o deploy do arquivo conforme veremos durante o documento. 


## Configuração de Workspace, e provisionamento de computação
Durante a confecção do projeto em questão foi utilizado o Azure Machine Learning para criação de um workspace nomeado de 
**"GeleatoMagicoWorkspace"**:

![GeleatoMagicoWorkspace](imgs/worskpace.png)

Após a ciração do workspace e utilizando os recursos fornecidos pela Azure,foi criado o recurso "Azure Machine Learning" hospedado nesse espaço de trabalho, sendo nomeado de  

**"gelato-previsoes"**:
![GeleatoMagicoWorkspace](imgs/aml_criacao.png)
![GrupoDeRecursoscomAML](imgs/workspaceplusAMLStudio.png)

Neste estúdio do Azure Machine Leaning foi utilizado as configurações padrões do azure.  
Após a criação do recurso, foi realizado então a configuração de computação, sendo utilizado tanto a computação de instância com CPU, quando o cluster de automação para criar e "rodar" os notebooks diretamente da Azure Machine Learning Studio.  
Para a criação da instância de computação normal foram utilizados os seguintes recursos:  
| Nome | Tamanho da máquina virtual | Unidade de processamento | Custo estimado |
| --- | --- | --- | --- |
| cpu-geleto-instance | Standard_D2_v2 (2 núcleos, 7 GB de RAM, disco de 100 GB) | CPU – General purpose | $0.17/h (ao executar) |


![cpu_instance](imgs/cpu_instance.png)

Para a criação do Cluster de computação foram utilizados os seguintes recursos:
| Nome da computacao| Tipo de computação | Tamanho da máquina virtual | Unidade de processamento | Custo estimado | Nº de nós |
| --- | --- | --- | --- | --- | --- |
| cluester-geleto-instance | Computação do Machine Learning | Standard_D2_v2 (2 núcleos, 7 GB de RAM, disco de 100 GB) | CPU – General purpose | $0.17/h por nó | 2 |  

![cluster_instance](imgs/cluster_instance.png)

 Ambos os recursos foram criados com o objetivo, de realizar rodar os diferentes modelos e trabalhos que foram criados.  

 ## Scitps e Pipelines
 Após o provisionamento de máquinas virtuais no ambiente Azure, foi realizado a criação de modelos utilizando o MLflow, através de notebooks python, para tal tarefa foi realizado a excução do scritp [Cria base de dados](src/script_data_set.py), para geração do dataset a ser utilizado, bem como foi realizado o a criação de um diretório dentro do ambiente bem upload da pasta contendo o arquivo e notebook python para gerar o Job junto ao MLflow, o arquivo utilizado foi [Script MLflow](src/sorvetes_mlflow.ipynb),ambos os arquivos foram importados para as pastas criadas e os assim como os arquivos. 
 ![Arquivos notebooks AML](imgs/NotebookAML_1.png),
 ![Arquivos notebooks AML](imgs/NotebookAML_2.png)
 ![Arquivos notebooks AML](imgs/NotebookAML_3.png) para o desenvolvimento do notebook em questão foi tomado como base o arquivo 
 [Labs AML6](https://github.com/MicrosoftLearning/mslearn-azure-ml/blob/main/Labs/06/Classification%20with%20Automated%20Machine%20Learning.ipynb), após a condiguração do pipline, e do scritp corretamente, como pode ser visualizado foi realizado a inicialização do job respectivos do pip line em questão, gerando 2 jobs correlatos do mesmo experimento. 
  ![Jobs Pipeline](imgs/jobs_runing.png), ao final do treinamento houveram falhas de execução 

 ## Import de dado
 Após a modelagem e criação, de pipe lines foi realizado a criação de um modelo com base em dados diretamente do Azure Machine Learning, importando o data set para criação futura de ML automatizado, bem como via Designer
 ![import dados](imgs/import_dados.png)
 ![escolha dados](imgs/escolha_de_dados.png)
 ![tipo de dados](imgs/tipo_dado.png)
 ![selecao de dados](imgs/selecao_dado.png)
 ![configurando os dados](imgs/config_database.png)
 ![defindo esquema de dados](imgs/defindo_esquema_dados.png)
 ![revisando criação dos dados](imgs/criando_dados_1.png)
 ![final import dados](imgs/data_set.png)
 
 ## Criando trabalho com Auto ML
 Com os dados devidamente importados no ambiente, foi dado inicio a configuração do Auto ML,o experimento em questão foi nomeado de 
 **"venda_sorves_automl"**:  
 ![configuracao experimento](imgs/venda_sorves_automl.png)  

 Para o experimento em questão foi selecionado o modelo de regressão, visto que desejamos ter uma previsão com base no histórico de tempetura com relação as vendas do sorvete.
 ![configuracao experimento](imgs/tipo_tarefa_automl.png)  
 Para o experimento em questão foi escolhido apenas o algoritimo de XGBoostregressor, ainda foi configurado também que o modelo de previsão será nas vendas.
  ![configução adicional](imgs/config_params_automl.png) 
 Também foram configurados limites de tempo e utilização de nós.
   ![configução de limites automl](imgs/limites_automl.png) 
No final foi selecionado o tipo de computação a ser utilizada, que no caso foi a instância de cluster previamente provisionada e configurada.  
![configução de computacao](imgs/computacao_automl.png) 
Ao final da configuração, foi dado inicio a execução do trabalho criado pelo AutoML
![Trabalho AutoML running](imgs/running_automl.png)




<table style="text-align: center; width: 100%;">
 <caption><b>Project skils</b></caption>
  <tr>
    <td style="text-align: center;">
      <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/>
    </td>
    <td style="text-align: center;">
      <img src="https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white"/>
    </td>
    <td style="text-align: center;">
      <img alt="Markdown" src="https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white"/>
    </td>
    <td style="text-align: center;">
      <img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/>
    </td>
  </tr>
  <tr>
    <td style="text-align: center;">
      <img alt="Visual Studio Code" src="https://img.shields.io/badge/VisualStudioCode-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
    </td>
    <td style="text-align: center;">
      <img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>
    </td>
    <td style="text-align: center;">
      <img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/>
    </td>
    <td style="text-align: center;">
      <img alt="Azure" src="https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=azure-devops&logoColor=white"/>
    </td>
  </tr>
</table>


