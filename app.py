from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resumo = None
    head = None
    info = None

    if request.method == 'POST':
        file = request.files.get('csv')
        if file and file.filename.endswith('.csv'):
            try:
                df = pd.read_csv(file)
                
                #1 resumo de df 
                resumo = df.describe().to_html(classes='tabela-dados')

                #2 head de df
                head = df.head(5).to_html(classes='tabela-dados')

                #3 info de df
                info_generica = {
                    'Total de linhas': [df.shape[0]],
                    'Total de colunas': [df.shape[1]],
                    'Colunas númericas': [len(df.select_dtypes(include=['number']).columns)],
                    'Colunas de texto': [len(df.select_dtypes(include=['object', 'string']).columns)]
                }
                info = pd.DataFrame(info_generica).to_html(classes='tabela-dados', index=False)

            except Exception as e:
                resultado = f"Erro ao processar o arquivo: {e}"
                
    return render_template(
        'index.html', 
        resultado_pandas=resumo,
        head_pandas=head,
        info_pandas=info
        )
  
if __name__ == '__main__':
    app.run(debug=True)