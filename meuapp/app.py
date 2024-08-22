from flask import Flask
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route("/")
def helloworld():
    # Dados fictícios para o gráfico
    anos = ['2018', '2019', '2020', '2021', '2022']
    media_calvos = [30, 45, 50, 60, 70]

    # Criação do gráfico
    plt.figure(figsize=(10,5))
    plt.plot(anos, media_calvos, marker='o', color='blue')
    plt.title('Média de Calvos por Ano')
    plt.xlabel('Ano')
    plt.ylabel('Média de Calvos')
    plt.grid(True)

    # Salvando o gráfico em um buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode()

    # Retornando o gráfico como imagem embutida
    return f'<img src="data:image/png;base64,{image_base64}"/>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

