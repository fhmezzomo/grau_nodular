import google.generativeai as genai

def grau_nodular(chave, imagem):
    try:
        # Configuração do modelo
        genai.configure(api_key=chave)
        modelo = genai.GenerativeModel('gemini-1.5-flash')

        # Prompt
        prompt = '''Analise a imagem fornecida e estime o grau de nodularização, que é a porcentagem de nódulos de grafita
        em relação a área total de grafita. 
        Considere a forma, distribuição e quantidade dos nódulos.

        A imagem é uma metalografia de ferro fundido. Os nódulos de grafita aparecem como estruturas escuras e arredondadas
        distribuídas na matriz metálica. 
        Sua tarefa é contar ou estimar a porcentagem desses nódulos em relação à área total escura, que é a área de grafita.
        O Grau de nodularização estimado é a área de grafita nodular dividida pela área total de grafita.

        A resposta deve ser somente no formato:
        "O grau de nodularização estimado é de X%"

        Onde X é um valor entre 0 e 100, baseado na análise da imagem.
        '''

        # criação da resposta
        resposta = modelo.generate_content([prompt, imagem])
        nodularizacao = resposta.text

        return nodularizacao
    except Exception as e:
        return f"Erro ao analisar a imagem: {str(e)}"
