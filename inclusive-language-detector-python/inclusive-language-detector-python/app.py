from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from services.basic_analyzer import BasicAnalyzer
from services.pro_analyzer import ProAnalyzer
import os
from dotenv import load_dotenv  # ← AÑADIR ESTO

# ← CARGAR VARIABLES DE ENTORNO ANTES DE TODO
load_dotenv()

app = Flask(__name__)
CORS(app)

# Inicializar analizadores
basic_analyzer = BasicAnalyzer()
pro_analyzer = ProAnalyzer()

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    """Endpoint para análisis de texto"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        mode = data.get('mode', 'basic')  # 'basic' o 'pro'
        
        if not text or not text.strip():
            return jsonify({
                'error': 'El texto no puede estar vacío'
            }), 400
        
        if len(text) > 5000:
            return jsonify({
                'error': 'El texto es demasiado largo (máximo 5000 caracteres)'
            }), 400
        
        # Realizar análisis según el modo
        if mode == 'pro':
            result = pro_analyzer.analyze(text)
        else:
            result = basic_analyzer.analyze(text)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            'error': f'Error al procesar el texto: {str(e)}'
        }), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Endpoint de salud"""
    return jsonify({
        'status': 'ok',
        'service': 'Inclusive Language Detector',
        'version': '1.0.0',
        'openai_configured': bool(os.environ.get('OPENAI_API_KEY'))
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    
    # Verificar configuración
    api_key = os.environ.get('OPENAI_API_KEY', '')
    if api_key:
        print(f"✅ OpenAI API Key configurada (primeros 10 chars: {api_key[:10]}...)")
    else:
        print("⚠️  OpenAI API Key NO configurada - Modo Pro no disponible")
    
    app.run(host='0.0.0.0', port=port, debug=False)