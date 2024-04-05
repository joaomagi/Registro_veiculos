# Registo de veículos
Este código é uma aplicação gráfica construída com a biblioteca Tkinter em Python, projetada para gerenciar informações sobre veículos. Ele permite adicionar detalhes sobre veículos, como placa, cliente, marca, modelo, status e datas de entrada e saída. Aqui está uma descrição do código:

### Bibliotecas utilizadas:
- `Path` e `Pathlib`: Usadas para manipulação de caminhos de arquivos.
- `Tk`, `Canvas`, `Entry`, `Button`, `PhotoImage`: Classes do Tkinter para criar a interface gráfica.
- `pandas`: Biblioteca para manipulação de dados, usada para trabalhar com o DataFrame.

### Funcionalidades principais:
- **Adicionar Veículo**: Quando o botão é pressionado, os dados inseridos nos campos de entrada são coletados e adicionados a um DataFrame do Pandas.
- **Salvar Dados**: Os dados inseridos são salvos em um arquivo Excel chamado "veiculos.xlsx".
- **Limpar Campos**: Após adicionar um veículo, os campos de entrada são limpos para inserção de novos dados.
- **Interface Gráfica**: A interface é construída usando elementos gráficos como botões, entradas de texto e texto.

### Estrutura do Código:
- **Configuração da Janela Principal**: Define as dimensões, cor de fundo e outros atributos da janela.
- **Criação dos Elementos Visuais**: Define e posiciona os botões, entradas de texto e textos na interface.
- **Função para Adicionar Veículo**: Coleta os dados dos campos de entrada, cria um novo registro de veículo em um DataFrame do Pandas e salva os dados em um arquivo Excel.
- **Loop Principal**: Mantém a janela aberta e aguarda interações do usuário.

Este código constrói uma interface gráfica simples para gerenciar informações sobre veículos e é uma implementação básica de uma aplicação de desktop em Python usando Tkinter.
