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
                resumo_df = df.describe()
                traducao_describe = {
                'count': 'Contagem',
                'mean': 'Média',
                'std': 'Desvio Padrão',
                'min': 'Mínimo',
                'max': 'Máximo',
                }
                resumo_df = resumo_df.rename(index=traducao_describe)
                resumo = resumo_df.to_html(classes='tabela-dados')

                #2 head de df
                df_head = df.head(5)
                df_head.index = df_head.index + 1
                head = df_head.to_html(classes='tabela-dados')

                #3 info de df
                info_generica = {
                    'Total de linhas': [df.shape[0]],
                    'Total de colunas': [df.shape[1]],
                    'Colunas númericas': [len(df.select_dtypes(include=['number']).columns)],
                    'Colunas de texto': [len(df.select_dtypes(include=['object', 'string']).columns)],
                    'Total de dados vazios': [int(df.isnull().sum().sum())]

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