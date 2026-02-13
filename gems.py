import os
import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from google.genai import types

app = Flask(__name__)
CORS(app)

# --- CONFIGURAÇÃO IA ---
API_KEY = "AIzaSyDOfwLJx3035-JswcuI1YY-pxOsqaO4gwA" 
client = genai.Client(api_key=API_KEY)
MODEL_ID = "gemini-2.5-flash"

# FILAS DE MENSAGENS
mensagens_para_humano = [] 
respostas_do_humano = []   

SYSTEM_INSTRUCTION = """Você é Allan, 17 anos...""" # Mantenha seu prompt aqui

@app.route('/enviar_juiz', methods=['POST'])
def enviar_juiz():
    data = request.json
    canal = data.get('canal')
    msg = data.get('msg')

    if canal == 'B':
        try:
            time.sleep(2) # Delay simulado
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=msg,
                config=types.GenerateContentConfig(system_instruction=SYSTEM_INSTRUCTION)
            )
            return jsonify({"resposta": response.text})
        except Exception as e:
            return jsonify({"resposta": "vixe, deu erro na rede..."}), 500
    else:
        # LÓGICA HUMANO (TERMINAL A)
        mensagens_para_humano.append(msg)
        
        # Espera resposta por até 45 segundos
        for _ in range(45):
            if respostas_do_humano:
                return jsonify({"resposta": respostas_do_humano.pop(0)})
            time.sleep(1)
        return jsonify({"resposta": "Allan (A) demorou demais pra responder..."})

@app.route('/humano/painel', methods=['GET', 'POST'])
def painel_humano():
    if request.method == 'POST':
        res_texto = request.json.get('res')
        respostas_do_humano.append(res_texto)
        return jsonify({"status": "ok"})
    
    pergunta = mensagens_para_humano.pop(0) if mensagens_para_humano else "Nenhuma pergunta ainda."
    return jsonify({"pergunta": pergunta})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)