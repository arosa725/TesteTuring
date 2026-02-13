import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

# 1. Configuração da sua chave
genai.configure(api_key="AIzaSyDOfwLJx3035-JswcuI1YY-pxOsqaO4gwA")

# 2. Em vez de usar 'gemini-1.5-pro', você usa o nome do seu GEM/Modelo Tunado
# Você encontra esse nome no AI Studio em "Saved Prompts" ou "Tuned Models"
NOME_DO_SEU_GEM = 'tunedModels/AllanTuring' 

model = genai.GenerativeModel(model_name=NOME_DO_SEU_GEM)

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    pergunta = data.get('msg')
    
    # O modelo já possui as instruções que você configurou no Gem
    response = model.generate_content(pergunta)
    
    return jsonify({"resposta": response.text})

if __name__ == '__main__':
    app.run(port=5000)