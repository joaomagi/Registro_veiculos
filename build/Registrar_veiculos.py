# Importa a classe Path para manipulação de caminhos de arquivos
from pathlib import Path
# Importa as classes necessárias do tkinter
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import pandas as pd  # Importa a biblioteca pandas para manipulação de dados

# Define o caminho para os recursos (imagens)
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / \
    Path(r"C:\Users\joaoc\OneDrive\Área de Trabalho\vscode\carros\build\assets\frame0")

# Função para converter caminhos relativos em relação aos ativos


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# DataFrame inicial vazio para armazenar informações sobre os veículos
dados_iniciais = {
    'Placa': [],
    'Cliente': [],
    'Marca': [],
    'Modelo': [],
    'Status': [],
    'Data_Entrada': [],
    'Data_Saida': [],
}

df = pd.DataFrame(dados_iniciais)  # Cria o DataFrame inicial vazio

# Função para adicionar um novo veículo ao DataFrame


def adicionar_veiculo():
    # Obtém os valores dos campos de entrada
    placa = entry_placa.get()
    cliente = entry_cliente.get()
    marca = entry_marca.get()
    modelo = entry_modelo.get()
    status = entry_status.get()
    data_entrada = entry_data_entrada.get()
    data_saida = entry_data_saida.get()

    # Cria um dicionário com as informações do novo veículo
    novo_veiculo = {
        'Placa': placa,
        'Cliente': cliente,
        'Marca': marca,
        'Modelo': modelo,
        'Status': status,
        'Data_Entrada': data_entrada,
        'Data_Saida': data_saida,
    }

    global df
    # Cria um DataFrame temporário com o novo veículo
    novo_df = pd.DataFrame([novo_veiculo])
    # Concatena o DataFrame temporário ao DataFrame principal
    df = pd.concat([df, novo_df], ignore_index=True)

    # Salva o DataFrame em um arquivo Excel
    df.to_excel("veiculos.xlsx", index=False)

    # Limpa os campos de entrada após adicionar o veículo
    entry_placa.delete(0, 'end')
    entry_cliente.delete(0, 'end')
    entry_marca.delete(0, 'end')
    entry_modelo.delete(0, 'end')
    entry_status.delete(0, 'end')
    entry_data_entrada.delete(0, 'end')
    entry_data_saida.delete(0, 'end')


# Configuração da janela principal
window = Tk()
window.geometry("1024x576")  # Define as dimensões da janela
window.configure(bg="#FFFFFF")  # Define a cor de fundo da janela

# Cria um canvas para desenhar elementos gráficos
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=576,
    width=1024,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)  # Posiciona o canvas na janela

# Cria elementos visuais na tela (botão, texto, entradas)
# As coordenadas e outras propriedades são definidas para cada elemento
# Os elementos são colocados na tela usando o método place()
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    512.0,
    288.0,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    0.0,
    1024.0,
    77.0,
    fill="#292D77",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=adicionar_veiculo,
    relief="flat"
)
button_1.place(
    x=863.0,
    y=476.0,
    width=153.0,
    height=85.0
)

canvas.create_text(
    34.0,
    93.0,
    anchor="nw",
    text="Placa:\n",
    fill="#000000",
    font=("ComicSansMS", 20 * -1)
)

canvas.create_text(
    35.0,
    163.0,
    anchor="nw",
    text="Cliente:\n",
    fill="#000000",
    font=("ComicSansMS", 20 * -1)
)

canvas.create_text(
    35.0,
    237.0,
    anchor="nw",
    text="Marca:\n",
    fill="#000000",
    font=("ComicSansMS", 20 * -1)
)

canvas.create_text(
    35.0,
    310.0,
    anchor="nw",
    text="Modelo:\n",
    fill="#000000",
    font=("ComicSansMS", 20 * -1)
)

canvas.create_text(
    35.0,
    384.0,
    anchor="nw",
    text="Status:\n",
    fill="#000000",
    font=("ComicSansMS", 20 * -1)
)

canvas.create_text(
    609.0,
    93.0,
    anchor="nw",
    text="Data de Entrada:\n",
    fill="#000000",
    font=("ComicSansMS", 20 * -1)
)

canvas.create_text(
    613.0,
    163.0,
    anchor="nw",
    text="Previsão de Saída:\n",
    fill="#000000",
    font=("ComicSansMS", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    207.5,
    141.0,
    image=entry_image_1
)
entry_placa = Entry(
    bd=0,
    bg="#C8C3C3",
    fg="#000716",
    highlightthickness=0
)
entry_placa.place(
    x=45.0,
    y=126.0,
    width=325.0,
    height=28.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    207.5,
    215.0,
    image=entry_image_2
)
entry_cliente = Entry(
    bd=0,
    bg="#C8C3C3",
    fg="#000716",
    highlightthickness=0
)
entry_cliente.place(
    x=45.0,
    y=200.0,
    width=325.0,
    height=28.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    207.5,
    362.0,
    image=entry_image_3
)
entry_modelo = Entry(
    bd=0,
    bg="#C8C3C3",
    fg="#000716",
    highlightthickness=0
)
entry_modelo.place(
    x=45.0,
    y=347.0,
    width=325.0,
    height=28.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    212.5,
    436.0,
    image=entry_image_4
)
entry_status = Entry(
    bd=0,
    bg="#C8C3C3",
    fg="#000716",
    highlightthickness=0
)
entry_status.place(
    x=50.0,
    y=421.0,
    width=325.0,
    height=28.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    781.5,
    141.0,
    image=entry_image_5
)
entry_data_entrada = Entry(
    bd=0,
    bg="#C8C3C3",
    fg="#000716",
    highlightthickness=0
)
entry_data_entrada.place(
    x=619.0,
    y=126.0,
    width=325.0,
    height=28.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    781.5,
    215.0,
    image=entry_image_6
)
entry_data_saida = Entry(
    bd=0,
    bg="#C8C3C3",
    fg="#000716",
    highlightthickness=0
)
entry_data_saida.place(
    x=619.0,
    y=200.0,
    width=325.0,
    height=28.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    207.5,
    288.0,
    image=entry_image_7
)
entry_marca = Entry(
    bd=0,
    bg="#C8C3C3",
    fg="#000716",
    highlightthickness=0
)
entry_marca.place(
    x=45.0,
    y=273.0,
    width=325.0,
    height=28.0
)
# Impede redimensionamento da janela
window.resizable(False, False)
# Loop principal para manter a janela aberta
window.mainloop()
