from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None

    if request.method == 'POST':
        file = request.files.get('csv')
        # Adicionei um ponto antes do csv aqui (.csv) para garantir a validação da extensão
        if file and file.filename.endswith('.csv'):
            try:
                df = pd.read_csv(file)
                resumo = df.describe()
                resultado = resumo.to_html(classes='tabela-dados')
            except Exception as e:
                resultado = f"Erro ao processar o arquivo: {e}"
                
    # VEJA AQUI: Recuado para a esquerda, fora do "if". 
    # Agora ele atende tanto o GET quanto o POST!
    return render_template('index.html', resultado_pandas=resultado)
  
if __name__ == '__main__':
    app.run(debug=True)