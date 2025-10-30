import os
import re
import json
import unicodedata

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


class ProAnalyzer:
    """Analizador avanzado con IA de OpenAI"""
    
    def __init__(self):
        # Configurar API de OpenAI desde variable de entorno
        self.api_key = os.environ.get('OPENAI_API_KEY', '')
        
        if not self.api_key or len(self.api_key) < 20:
            print("⚠️ Warning: OPENAI_API_KEY no configurada")
            self.client = None
        elif OpenAI is None:
            print("⚠️ Warning: openai package no disponible")
            self.client = None
        else:
            try:
                # Inicializar con timeout más largo para Vercel
                self.client = OpenAI(
                    api_key=self.api_key,
                    timeout=60.0,
                    max_retries=2
                )
            except Exception as e:
                print(f"⚠️ Error inicializando OpenAI: {str(e)}")
                self.client = None
        
        self.model = os.environ.get('OPENAI_MODEL', 'gpt-3.5-turbo')
    
    def normalize_text(self, text):
        """Normaliza texto para detectar evasiones"""
        normalized = text.lower()
        
        # Normalizar caracteres especiales
        normalized = unicodedata.normalize('NFD', normalized)
        normalized = ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')
        
        # Remover separadores
        normalized = re.sub(r'[\s\-_\.\,\;\:\'\"\`\´\~\!\¡\¿\?\(\)\[\]\{\}\/\\\|]', '', normalized)
        
        # Reemplazar números por letras
        replacements = {
            '0': 'o', '1': 'i', '3': 'e', '4': 'a',
            '5': 's', '7': 't', '8': 'b', '9': 'g'
        }
        
        for num, letter in replacements.items():
            normalized = normalized.replace(num, letter)
        
        return normalized
    
    def build_prompt(self, text, normalized_text):
        """Construye el prompt para la IA"""
        total_words = len(text.split())
        
        prompt = f"""Eres un experto lingüista especializado en análisis de lenguaje inclusivo.

**TU MISIÓN**: Analizar el CONTEXTO y la INTENCIÓN, no solo las palabras superficiales.

**PRINCIPIOS DE ANÁLISIS CONTEXTUAL:**

1. **INTENCIÓN vs. FORMA**: 
   - "Mi amigo es negro" (descriptivo) ≠ "trabaja como negro" (ofensivo)
   - Analiza si el término se usa para DESCRIBIR o para DEGRADAR

2. **EVASIÓN DETECTADA**:
   Identifica intentos de ocultar lenguaje ofensivo:
   - Números: "p3nd3j0", "n3gr0", "m4r1c0n" "m4ld1 t 4"
   - Espacios: "p e n d e j o", "l o c a"
   - Símbolos: "p@ndejo", "n€gro" 

3. **CATEGORÍAS**:
   - **SEXISMO**: Insultos de género, masculino genérico, estereotipos
   - **CAPACITISMO**: Términos sobre salud mental o discapacidad como insultos
   - **RACISMO**: Términos raciales peyorativos, estereotipos étnicos
   - **OFENSIVO**: Insultos, clasismo, body shaming, homofobia

**TEXTO A ANALIZAR:**
"{text}" 

**TEXTO NORMALIZADO (detecta variaciones ocultas):**
"{normalized_text}"

**FORMATO DE RESPUESTA (SOLO JSON VÁLIDO):**
{{
  "issues": [
    {{
      "type": "sexist|ableist|ethnic|offensive",
      "original_text": "término_exacto",
      "suggestion": "alternativa_inclusiva",
      "severity": "high|medium|low",
      "explanation": "Explicación CONTEXTUAL de por qué es problemático",
      "confidence": 0.95
    }}
  ],
  "stats": {{
    "total_words": {total_words},
    "issues_found": 0,
    "inclusive_score": 100,
    "categories": {{
      "sexist": 0,
      "ableist": 0,
      "ethnic": 0,
      "offensive": 0
    }}
  }},
  "overall_feedback": "Análisis contextual profundo del texto"
}}

**INSTRUCCIONES CRÍTICAS:**
1. NO etiquetes como problemático si el uso es claramente neutral o descriptivo
2. SÍ detecta evasiones con números/espacios/símbolos
3. CONSIDERA el contexto completo antes de juzgar
4. DA explicaciones que eduquen
5. Devuelve SOLO JSON válido
6. Si NO hay problemas, devuelve issues como array vacío []

**EJEMPLO:**
- "Mi amiga negra es médica" → NEUTRAL (descriptivo)
- "Trabaja como n3gr0" → OFENSIVO (peyorativo + evasión)

ANALIZA CON INTELIGENCIA CONTEXTUAL."""
        
        return prompt
    
    def analyze(self, text):
        """Analiza texto usando IA de OpenAI"""
        if not self.client:
            return {
                'error': '⚠️ API Key de OpenAI no configurada. Configura OPENAI_API_KEY en variables de entorno.'
            }
        
        try:
            normalized = self.normalize_text(text)
            prompt = self.build_prompt(text, normalized)
            
            # Llamar a OpenAI
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "Eres un lingüista experto en análisis contextual de lenguaje inclusivo. Analizas el SIGNIFICADO y el CONTEXTO. Tu objetivo es educar y sugerir alternativas. Siempre devuelves respuestas en formato JSON válido."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.5,
                max_tokens=3000,
                response_format={"type": "json_object"}
            )
            
            ai_response = response.choices[0].message.content
            
            # Parsear respuesta JSON
            try:
                # Limpiar respuesta
                clean_response = ai_response.strip()
                clean_response = re.sub(r'```json\n?', '', clean_response)
                clean_response = re.sub(r'```\n?', '', clean_response)
                clean_response = clean_response.strip()
                
                analysis = json.loads(clean_response)
            except json.JSONDecodeError as e:
                print(f"❌ Error parseando JSON: {ai_response}")
                return {
                    'error': 'Error al procesar respuesta de IA. Intenta con modo básico.'
                }
            
            # Validar y corregir estructura de análisis
            if 'issues' not in analysis:
                analysis['issues'] = []
            
            if 'stats' not in analysis:
                analysis['stats'] = {
                    'total_words': len(text.split()),
                    'issues_found': len(analysis.get('issues', [])),
                    'inclusive_score': 100,
                    'categories': {
                        'sexist': 0,
                        'ableist': 0,
                        'ethnic': 0,
                        'offensive': 0
                    }
                }
            
            # Actualizar contadores de categorías
            if 'categories' in analysis['stats']:
                for issue in analysis['issues']:
                    issue_type = issue.get('type', 'offensive')
                    if issue_type in analysis['stats']['categories']:
                        analysis['stats']['categories'][issue_type] += 1
            
            # Actualizar issues_found
            analysis['stats']['issues_found'] = len(analysis['issues'])
            
            # Calcular inclusive_score si no está presente
            if analysis['stats']['inclusive_score'] == 100 and analysis['stats']['issues_found'] > 0:
                total_words = analysis['stats']['total_words']
                issues_found = analysis['stats']['issues_found']
                severity_weight = {'high': 3, 'medium': 2, 'low': 1}
                weighted_issues = sum(
                    severity_weight.get(issue.get('severity', 'medium'), 2) 
                    for issue in analysis['issues']
                )
                analysis['stats']['inclusive_score'] = max(
                    0, 
                    round(100 - (weighted_issues / max(1, total_words)) * 100)
                )
            
            # Construir resultado
            result = {
                'original_text': text,
                'issues': analysis['issues'],
                'suggestions': [
                    {
                        'original': issue.get('original_text', ''),
                        'replacement': issue.get('suggestion', ''),
                        'reason': issue.get('explanation', 'Sin explicación')
                    }
                    for issue in analysis['issues']
                ],
                'stats': analysis['stats'],
                'overall_feedback': analysis.get(
                    'overall_feedback', 
                    '✅ Análisis completado.' if len(analysis['issues']) == 0 
                    else f'⚠️ Detecté {len(analysis["issues"])} término(s) que podrían mejorarse.'
                )
            }
            
            return result
            
        except Exception as e:
            error_msg = str(e)
            
            if 'authentication' in error_msg.lower() or '401' in error_msg:
                return {
                    'error': '❌ API Key inválida. Verifica tu configuración de OPENAI_API_KEY.'
                }
            elif 'rate' in error_msg.lower() or '429' in error_msg:
                return {
                    'error': 'Límite de solicitudes alcanzado. Prueba el modo básico o espera un momento.'
                }
            elif '500' in error_msg or '503' in error_msg:
                return {
                    'error': '🔧 OpenAI está experimentando problemas. Intenta de nuevo en unos segundos.'
                }
            else:
                print(f"❌ Error detallado: {error_msg}")
                return {
                    'error': f'Error al conectar con OpenAI: {error_msg}\n\nIntenta con el modo básico.'
                }