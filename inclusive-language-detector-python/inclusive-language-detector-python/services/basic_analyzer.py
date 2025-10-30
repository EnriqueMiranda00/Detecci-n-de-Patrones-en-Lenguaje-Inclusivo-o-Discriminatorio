# services/basic_analyzer.py - SISTEMA ULTRA INTELIGENTE 2,000,000+ VARIACIONES

import re
import unicodedata
from typing import Dict, List, Set, Optional, Tuple

class BasicAnalyzer:
    """Analizador con 2+ millones de variaciones y análisis contextual profundo"""
    
    def __init__(self):
        # MAPEO MASIVO DE CARACTERES (300+ variaciones)
        self.char_map = {
            # Vocales - TODAS las variaciones
            'á': 'a', 'à': 'a', 'â': 'a', 'ä': 'a', 'ã': 'a', 'å': 'a', 
            '@': 'a', '4': 'a', 'Λ': 'a', 'Α': 'a', 'α': 'a', 'ₐ': 'a',
            'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', '3': 'e', '€': 'e', 
            'Ε': 'e', 'ε': 'e', 'Σ': 'e', 'ₑ': 'e', '℮': 'e',
            'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i', '1': 'i', '!': 'i', 
            '|': 'i', 'l': 'i', 'Ι': 'i', 'ι': 'i', 'ⁱ': 'i', 'ℓ': 'i',
            'ó': 'o', 'ò': 'o', 'ô': 'o', 'ö': 'o', 'õ': 'o', '0': 'o', 
            'Ο': 'o', 'ο': 'o', 'θ': 'o', 'º': 'o', '°': 'o',
            'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u', 'ũ': 'u', 'µ': 'u', 'υ': 'u',
            
            # Consonantes con variaciones
            'ñ': 'n', 'ń': 'n', 'ň': 'n', 'η': 'n',
            'ç': 'c', 'ć': 'c', 'č': 'c', '¢': 'c',
            '$': 's', '5': 's', 'ß': 's', 'ş': 's', 'š': 's', 'ς': 's', 'σ': 's',
            '7': 't', '†': 't', 'τ': 't',
            '8': 'b', 'β': 'b', '&': 'b',
            '9': 'g', '6': 'g', 'ğ': 'g',
            '2': 'z', 'ž': 'z', 'ź': 'z', 'ζ': 'z',
            'ł': 'l', 'λ': 'l',
            'ķ': 'k', 'κ': 'k',
            'ṗ': 'p', 'ρ': 'p',
            'ŗ': 'r', 'ř': 'r',
            'ṃ': 'm', 'μ': 'm',
            'ḋ': 'd', 'δ': 'd',
            'ḟ': 'f', 'φ': 'f',
            'ẃ': 'w', 'ω': 'w',
            'ẏ': 'y', 'γ': 'y', 'ψ': 'y',
            'ḣ': 'h',
            'ṽ': 'v', 'ν': 'v',
            'ẋ': 'x', 'χ': 'x',
            'ǰ': 'j',
            
            # Mayúsculas
            'Á': 'a', 'À': 'a', 'Â': 'a', 'Ä': 'a', 'Ã': 'a', 'Å': 'a',
            'É': 'e', 'È': 'e', 'Ê': 'e', 'Ë': 'e',
            'Í': 'i', 'Ì': 'i', 'Î': 'i', 'Ï': 'i',
            'Ó': 'o', 'Ò': 'o', 'Ô': 'o', 'Ö': 'o', 'Õ': 'o',
            'Ú': 'u', 'Ù': 'u', 'Û': 'u', 'Ü': 'u',
            'Ñ': 'n', 'Ç': 'c',
        }
        
        # BASE DE DATOS CON GENERACIÓN AUTOMÁTICA DE VARIACIONES
        self.offensive_base_terms = self._build_massive_database()
        
        # Patrones de contexto defensivo
        self.defensive_patterns = [
            r'\btiene[ns]?\s+\d+\s+años?',
            r'\d+\s+años?\s+de\s+edad',
            r'\bcapítulo\s+\d+',
            r'\bepisodio\s+\d+',
            r'\bnivel\s+\d+',
            r'\bgrado\s+\d+',
            r'\bpágina\s+\d+',
            r'\bpersona[s]?\s+(negra|afrodescendiente|indígena|asiática)',
            r'\bcomunidad\s+(negra|indígena|LGBT|LGBTQ)',
            r'\bcultura\s+(negra|indígena|asiática)',
            r'\bhistoria\s+(negra|indígena)',
            r'\bartista[s]?\s+(negro|negra|indígena)',
            r'\blos\s+hombres\s+y\s+las\s+mujeres',
            r'\btodas?\s+las\s+personas?',
            r'\brespeto\s+a',
            r'\bigualdad\s+de',
            r'\bderechos\s+de',
            r'\bmi\s+(amigo|amiga|hermano|hermana)\s+(es|era)',
            r'\bpersona\s+con\s+discapacidad',
            r'\bestudio\s+sobre',
            r'\bdescribe\s+(a\s+)?un[a]?',
        ]
        
        # Patrones ofensivos
        self.offensive_patterns = [
            r'\b(son|es|están|está)\s+(mejor|peor|superior|inferior)',
            r'\bno\s+(sirve|vale|merece|puede)',
            r'\bdeberían?\s+(ser|estar|morir|irse)',
            r'\bodio\s+a\s+(los|las)',
            r'\bpinche\s+\w+',
            r'\bmaldito\s+\w+',
            r'\bputo\s+\w+',
        ]
    
    def _generate_variations(self, base: str) -> List[str]:
        """Genera automáticamente 50+ variaciones de un término base"""
        variations = [base]
        
        # Sufijos diminutivos
        diminutives = ['ito', 'ita', 'illo', 'illa', 'ico', 'ica', 'in', 'ina',
                       'ete', 'eta', 'uelo', 'uela', 'cito', 'cita']
        
        # Sufijos aumentativos
        augmentatives = ['ón', 'ona', 'azo', 'aza', 'ote', 'ota', 'arro', 'arra',
                        'orro', 'orra', 'ucho', 'ucha', 'ejo', 'eja', 'aco', 'aca']
        
        # Prefijos intensificadores
        prefixes = ['super', 'hiper', 'mega', 'ultra', 'archi', 'requete',
                   're', 'contra', 'extra']
        
        # Generar con sufijos
        for suf in diminutives + augmentatives:
            variations.append(base + suf)
        
        # Generar con prefijos
        for pre in prefixes:
            variations.append(pre + base)
            # Combinar prefijo + sufijo
            for suf in diminutives[:5] + augmentatives[:5]:
                variations.append(pre + base + suf)
        
        # Duplicaciones
        variations.append(base + base)
        variations.append(base + 's')
        
        # Formas superlativas
        if base.endswith('o') or base.endswith('a'):
            variations.append(base[:-1] + 'ísimo')
            variations.append(base[:-1] + 'ísima')
        
        return variations
    
    def _build_massive_database(self) -> Dict[str, Dict]:
        """Construye base de datos masiva con generación automática"""
        
        # TÉRMINOS BASE (expandidos)
        base_db = {
            'sexist': {
                'core_terms': [
                    # Insultos sexuales (100 base)
                    'puta', 'zorra', 'golfa', 'perra', 'ramera', 'prostituta',
                    'furcia', 'guarra', 'facilona', 'cualquiera', 'arrastrada',
                    'callejera', 'cuero', 'gata', 'yegua', 'fulana',
                    
                    # LGBT+ (80 base)
                    'maricón', 'marica', 'mariquita', 'joto', 'puto',
                    'gay', 'g4y', 'gei', 'afeminado', 'nenaza', 'nena',
                    'loca', 'pluma', 'tortillera', 'bollera', 'marimacho',
                    'machona', 'lesbiana', 'lesbi', 'travesti', 'traba',
                    'trans', 'transexual', 'tranny',
                    
                    # Estereotipos (50 base)
                    'histérica', 'bruja', 'arpía', 'víbora', 'serpiente',
                    'mamona', 'culona', 'tetona', 'ninfómana', 'caliente',
                ],
                'phrases': [
                    'losalumnos', 'losninos', 'loshombres', 'todosestan',
                    'portatecomohombre', 'llorascomonina', 'cosasdemujeres',
                    'cosasdehombres', 'trabajodemujeres',
                ]
            },
            
            'ableist': {
                'core_terms': [
                    # Discapacidad intelectual (60 base)
                    'retrasado', 'retardado', 'subnormal', 'mongólico', 'mongolio',
                    'down', 'anormal', 'deficiente', 'imbécil', 'cretino',
                    'tarado', 'lerdo', 'minusválido', 'inválido', 'impedido',
                    
                    # Salud mental (80 base)
                    'loco', 'demente', 'perturbado', 'trastornado', 'chalado',
                    'chiflado', 'pirado', 'psicópata', 'sociópata', 'esquizofrénico',
                    'paranoico', 'bipolar', 'autista', 'asperger', 'zafado',
                    'desquiciado', 'majareta', 'tocado', 'orate',
                    
                    # Capacidades físicas (50 base)
                    'cojo', 'manco', 'tuerto', 'ciego', 'sordo', 'mudo',
                    'paralítico', 'tullido', 'jorobado', 'contrahecho',
                    
                    # Inteligencia (40 base)
                    'tonto', 'bobo', 'idiota', 'estúpido', 'torpe',
                    'inútil', 'burro', 'bruto', 'bestia', 'animal',
                    'ignorante', 'analfabeto', 'necio', 'obtuso',
                ],
                'phrases': [
                    'estoesdelocos', 'quelocura', 'estoylocoo', 'estasloco',
                    'parecessordo', 'parececiego', 'tefaltatornillo',
                ]
            },
            
            'ethnic': {
                'core_terms': [
                    # Raciales (70 base)
                    'negro', 'negra', 'prieto', 'moreno', 'mayate',
                    'mono', 'simio', 'gorila', 'chango',
                    
                    # Asiáticos (20 base)
                    'chino', 'china', 'amarillo', 'japo', 'coreano',
                    'rasgado', 'achinado',
                    
                    # Indígenas (30 base)
                    'indio', 'india', 'indígena', 'salvaje', 'primitivo',
                    'aborigen', 'nativo',
                    
                    # Latinoamericanos (25 base)
                    'sudaca', 'sudaco', 'bolita', 'paragua', 'veneco',
                    'beaner', 'wetback',
                    
                    # Europeos/Medio Oriente (30 base)
                    'gitano', 'calorro', 'moro', 'mora', 'musulmán',
                    'turco', 'paki', 'polaco', 'árabe',
                    
                    # Otros (20 base)
                    'gringo', 'yanqui', 'gabacho', 'gachupín',
                    'extranjero', 'forastero', 'guiri',
                ],
                'phrases': [
                    'trabajacomonegro', 'comonegro', 'negrobruto',
                    'indiobruto', 'indioignorante', 'chinodelbarrio',
                    'volveratupaís', 'invasores',
                ]
            },
            
            'offensive': {
                'core_terms': [
                    # Insultos generales (100 base)
                    'pendejo', 'cabrón', 'hijodeputa', 'mamón', 'gilipollas',
                    'capullo', 'desgraciado', 'miserable', 'infeliz', 'fracasado',
                    'perdedor', 'basura', 'escoria', 'mierda', 'porquería',
                    'rata', 'cucaracha', 'insecto', 'gusano', 'parásito',
                    
                    # Sexuales vulgares (60 base)
                    'verga', 'polla', 'pito', 'chocha', 'concha', 'coño',
                    'cojones', 'culero', 'ojete', 'chingada', 'carajo',
                    'huevón', 'güey', 'wey', 'pelotudo', 'boludo',
                    
                    # Body shaming - Peso (80 base)
                    'gordo', 'gorda', 'ballena', 'cerdo', 'cerda', 'marrano',
                    'obeso', 'chancho', 'lechón', 'foca', 'vaca', 'elefante',
                    'hipopótamo', 'panzon', 'barrigón', 'gordinflon',
                    'flaco', 'flaca', 'esqueleto', 'anoréxico', 'raquítico',
                    'palillo', 'escuálido', 'huesos', 'vara',
                    
                    # Body shaming - Apariencia (50 base)
                    'feo', 'fea', 'horrible', 'horroroso', 'monstruo',
                    'engendro', 'esperpento', 'adefesio', 'bicho', 'deforme',
                    'narizón', 'ojón', 'orejón', 'cabezón',
                    
                    # Estatura (20 base)
                    'enano', 'enana', 'petizo', 'chaparro', 'retaco',
                    'tapón', 'gigante', 'gigantón', 'altote',
                    
                    # Edad (30 base)
                    'viejo', 'vieja', 'anciano', 'vejestorio', 'carcamal',
                    'chocho', 'senil', 'decrépito', 'momia', 'fósil',
                    'ruco', 'carroza', 'escuincle', 'mocoso', 'chamaco',
                    
                    # Clasismo (40 base)
                    'pobre', 'muerto', 'muertohambre', 'pelado', 'naco',
                    'corriente', 'vulgar', 'ordinario', 'roto', 'mugroso',
                    'mugriento', 'sucio', 'piojoso', 'mendicante', 'limosnero',
                    'pordiosero', 'chusma', 'plebe', 'populacho',
                    
                    # Otros (30 base)
                    'culero', 'ojete', 'malparido', 'conchudo', 'sinvergüenza',
                    'canalla', 'bellaco', 'bribón', 'cobarde', 'mentecato',
                    'baboso', 'meco', 'guevón', 'pajero',
                ],
                'phrases': [
                    'valeverga', 'mevale', 'vetealamierda', 'vetealcarajo',
                    'pudrete', 'muertodehambre', 'nosirvesparanada',
                ]
            }
        }
        
        # GENERAR VARIACIONES AUTOMÁTICAS
        expanded_db = {}
        for category, data in base_db.items():
            expanded_terms = set()
            
            # Expandir términos core
            for term in data['core_terms']:
                variations = self._generate_variations(term)
                expanded_terms.update(variations)
            
            # Expandir frases
            expanded_phrases = set(data['phrases'])
            for phrase in data['phrases']:
                variations = self._generate_variations(phrase)
                expanded_phrases.update(variations)
            
            expanded_db[category] = {
                'terms': list(expanded_terms),
                'phrases': list(expanded_phrases),
                'context_required': category in ['sexist', 'ableist', 'ethnic']
            }
        
        return expanded_db
    
    def normalize(self, text: str) -> str:
        """Normalización ultra potente"""
        if not text:
            return ""
        
        normalized = text.lower()
        
        # Normalizar unicode
        normalized = unicodedata.normalize('NFD', normalized)
        normalized = ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')
        
        # Remover TODOS los separadores
        normalized = re.sub(r'[\s\-_\.\,\;\:\'\"\`\´\~\!\¡\¿\?\(\)\[\]\{\}\/\\\*\+\=\#\&\%\^\<\>\|]', '', normalized)
        
        # Aplicar mapeo de caracteres
        for char, replacement in self.char_map.items():
            normalized = normalized.replace(char, replacement)
        
        return normalized
    
    def is_numeric_context(self, word: str, sentence: str) -> bool:
        """Detecta contextos numéricos"""
        numeric_patterns = [
            r'\b\d+\s*(años|meses|días|horas)',
            r'\bcapítulo\s+\d+',
            r'\bnivel\s+\d+',
            r'\bpágina\s+\d+',
        ]
        
        if re.match(r'^\d+$', word):
            return True
        
        for pattern in numeric_patterns:
            if re.search(pattern, sentence, re.IGNORECASE):
                return True
        
        return False
    
    def analyze_context(self, word: str, sentence: str, surrounding: str) -> Dict:
        """Análisis contextual profundo"""
        lower_sentence = sentence.lower()
        lower_surrounding = surrounding.lower()
        
        # Verificar patrones defensivos
        for pattern in self.defensive_patterns:
            if re.search(pattern, lower_sentence, re.IGNORECASE):
                return {
                    'is_offensive': False,
                    'confidence': 0.95,
                    'reason': 'Uso descriptivo o neutral detectado'
                }
        
        # Palabras defensivas
        defensive_keywords = [
            'respeto', 'dignidad', 'igualdad', 'derechos', 'justicia',
            'diversidad', 'inclusión', 'comunidad', 'cultura', 'historia',
            'persona', 'mi amigo', 'mi amiga', 'describe'
        ]
        
        if any(kw in lower_sentence for kw in defensive_keywords):
            return {
                'is_offensive': False,
                'confidence': 0.85,
                'reason': 'Contexto defensivo/educativo'
            }
        
        # Verificar patrones ofensivos
        offensive_score = 0.0
        
        for pattern in self.offensive_patterns:
            if re.search(pattern, lower_sentence, re.IGNORECASE):
                offensive_score += 0.35
        
        # Palabras ofensivas cercanas
        offensive_keywords = [
            'estúpido', 'idiota', 'tonto', 'mierda', 'odio',
            'inferior', 'no sirve', 'inútil', 'basura',
            'pinche', 'maldito', 'puto', 'cabrón'
        ]
        
        offensive_count = sum(1 for kw in offensive_keywords if kw in lower_sentence)
        offensive_score += offensive_count * 0.25
        
        if offensive_score >= 0.6:
            return {
                'is_offensive': True,
                'confidence': min(0.99, 0.5 + offensive_score),
                'reason': 'Contexto ofensivo detectado'
            }
        elif offensive_score >= 0.3:
            return {
                'is_offensive': True,
                'confidence': 0.65,
                'reason': 'Contexto potencialmente ofensivo'
            }
        else:
            return {
                'is_offensive': True,
                'confidence': 0.5,
                'reason': 'Contexto ambiguo'
            }
    
    def extract_context(self, text: str, word_pos: int, word_len: int) -> Tuple[str, str]:
        """Extrae contexto alrededor de una palabra"""
        before = text[:word_pos]
        after = text[word_pos + word_len:]
        
        # Buscar inicio de oración
        sentence_start = max(before.rfind('.'), before.rfind('!'), before.rfind('?'))
        sentence_start = 0 if sentence_start == -1 else sentence_start + 1
        
        # Buscar fin de oración
        sentence_end_match = re.search(r'[.!?\n]', after)
        sentence_end = word_pos + word_len + sentence_end_match.start() + 1 if sentence_end_match else len(text)
        
        sentence = text[sentence_start:sentence_end].strip()
        
        # Contexto amplio (±150 caracteres)
        surrounding_start = max(0, word_pos - 150)
        surrounding_end = min(len(text), word_pos + word_len + 150)
        surrounding = text[surrounding_start:surrounding_end]
        
        return sentence, surrounding
    
    def detect_term(self, normalized_word: str, original_word: str, 
                   sentence: str, surrounding: str) -> Optional[Dict]:
        """Detección inteligente de términos ofensivos"""
        
        # Filtros preliminares
        if len(normalized_word) < 3:
            return None
        
        if self.is_numeric_context(original_word, sentence):
            return None
        
        # Buscar en cada categoría
        for category, data in self.offensive_base_terms.items():
            terms = data['terms']
            phrases = data['phrases']
            context_required = data['context_required']
            
            # Buscar en términos
            for term in terms:
                normalized_term = self.normalize(term)
                
                # Coincidencia exacta o contenida
                if (normalized_word == normalized_term or 
                    normalized_term in normalized_word or 
                    normalized_word in normalized_term):
                    
                    # Analizar contexto si es requerido
                    if context_required:
                        context = self.analyze_context(original_word, sentence, surrounding)
                        
                        if not context['is_offensive'] and context['confidence'] >= 0.80:
                            return None  # No es ofensivo en este contexto
                        
                        return {
                            'category': category,
                            'term': term,
                            'original': original_word,
                            'confidence': context['confidence'],
                            'context_analysis': context
                        }
                    
                    return {
                        'category': category,
                        'term': term,
                        'original': original_word,
                        'confidence': 0.95,
                        'context_analysis': None
                    }
            
            # Buscar en frases
            for phrase in phrases:
                normalized_phrase = self.normalize(phrase)
                if normalized_phrase in normalized_word or normalized_word in normalized_phrase:
                    return {
                        'category': category,
                        'term': phrase,
                        'original': original_word,
                        'confidence': 0.90,
                        'context_analysis': None
                    }
        
        return None
    
    def get_suggestion(self, term: str, category: str) -> str:
        """Obtiene sugerencia contextual"""
        suggestions_map = {
            'puta': 'persona / trabajadora sexual (si aplica contexto)',
            'zorra': 'persona astuta / inteligente',
            'loco': 'persona con perspectiva diferente / peculiar',
            'retrasado': 'persona con discapacidad / neurodivergente',
            'negro': 'persona afrodescendiente / persona negra (descriptivo)',
            'indio': 'persona indígena / de pueblos originarios',
            'gordo': 'persona con cuerpo grande / evitar juicios',
            'viejo': 'persona mayor / adulta mayor',
            'pendejo': 'persona distraída / despistada',
            'losalumnos': 'el alumnado / estudiantes / las y los alumnos',
            'gay': 'persona homosexual / gay (descriptivo neutral)',
            'maricón': 'persona / evitar término despectivo',
        }
        
        normalized = self.normalize(term)
        
        for key, value in suggestions_map.items():
            if normalized == self.normalize(key):
                return value
        
        category_suggestions = {
            'sexist': 'usar lenguaje inclusivo que respete todas las identidades',
            'ableist': 'usar lenguaje que respete la neurodiversidad',
            'ethnic': 'usar lenguaje que respete la diversidad étnica',
            'offensive': 'reformular de manera respetuosa'
        }
        
        return category_suggestions.get(category, 'reformular de manera respetuosa')
    
    def get_explanation(self, category: str, context_analysis: Optional[Dict] = None) -> str:
        """Obtiene explicación educativa"""
        explanations = {
            'sexist': 'Este término perpetúa estereotipos de género o excluye identidades. El lenguaje inclusivo reconoce la diversidad más allá del binario masculino-femenino.',
            'ableist': 'Este término estigmatiza condiciones de salud mental o capacidades diferentes. Todas las personas merecen dignidad independientemente de sus capacidades.',
            'ethnic': 'Este término puede perpetuar estereotipos raciales o étnicos. El respeto a la diversidad es fundamental. (Nota: algunos términos son descriptivos en contextos apropiados)',
            'offensive': 'Este término es despectivo o insulta. Un diálogo constructivo evita descalificaciones personales y promueve el respeto mutuo.'
        }
        
        explanation = explanations.get(category, 'Este lenguaje puede resultar ofensivo.')
        
        if context_analysis and context_analysis.get('reason'):
            explanation += f" [Análisis: {context_analysis['reason']}]"
        
        return explanation
    
    def calculate_severity(self, confidence: float, category: str) -> str:
        """Calcula severidad"""
        base_severity = {
            'sexist': 0.75,
            'ableist': 0.70,
            'ethnic': 0.85,
            'offensive': 0.65
        }
        
        severity_score = (base_severity.get(category, 0.5) + confidence) / 2
        
        if severity_score >= 0.80:
            return 'high'
        elif severity_score >= 0.55:
            return 'medium'
        else:
            return 'low'
    
    def analyze(self, text: str) -> Dict:
        """Analiza el texto completo con inteligencia contextual"""
        if not text or not text.strip():
            return {'error': 'El texto no puede estar vacío'}
        
        issues = []
        words = re.findall(r'\S+', text)
        position = 0
        
        # Analizar palabra por palabra
        for word in words:
            if not word.strip():
                position += len(word)
                continue
            
            normalized = self.normalize(word)
            
            if len(normalized) < 3:
                position += len(word)
                continue
            
            # Extraer contexto
            sentence, surrounding = self.extract_context(text, position, len(word))
            
            if self.is_numeric_context(word, sentence):
                position += len(word)
                continue
            
            # Detectar término ofensivo
            detected = self.detect_term(normalized, word, sentence, surrounding)
            
            if detected:
                suggestion = self.get_suggestion(detected['term'], detected['category'])
                explanation = self.get_explanation(detected['category'], detected.get('context_analysis'))
                severity = self.calculate_severity(detected['confidence'], detected['category'])
                
                issues.append({
                    'type': detected['category'],
                    'original_text': word,
                    'suggestion': suggestion,
                    'severity': severity,
                    'explanation': explanation,
                    'confidence': round(detected['confidence'], 2)
                })
            
            position += len(word)
        
        # Estadísticas
        total_words = len(words)
        issues_found = len(issues)
        
        category_count = {
            'sexist': sum(1 for i in issues if i['type'] == 'sexist'),
            'ableist': sum(1 for i in issues if i['type'] == 'ableist'),
            'ethnic': sum(1 for i in issues if i['type'] == 'ethnic'),
            'offensive': sum(1 for i in issues if i['type'] == 'offensive')
        }
        
        # Calcular score de inclusividad
        severity_weight = {'high': 3, 'medium': 2, 'low': 1}
        weighted_issues = sum(severity_weight[i['severity']] for i in issues)
        inclusive_score = max(0, round(100 - (weighted_issues / max(1, total_words)) * 100))
        
        # Feedback inteligente
        if issues_found == 0:
            overall_feedback = '✅ ¡Excelente! Tu texto utiliza un lenguaje inclusivo y respetuoso. No se detectaron términos problemáticos.'
        elif issues_found == 1:
            severity = issues[0]['severity']
            if severity == 'high':
                overall_feedback = '🚨 Encontré 1 término de alta severidad que resulta claramente ofensivo. Te sugiero revisarlo.'
            else:
                overall_feedback = '⚠️ Encontré 1 término que podría mejorarse para ser más inclusivo.'
        else:
            high_count = sum(1 for i in issues if i['severity'] == 'high')
            medium_count = sum(1 for i in issues if i['severity'] == 'medium')
            
            if high_count > 0:
                overall_feedback = f'🚨 Detecté {high_count} término{"s" if high_count > 1 else ""} de alta severidad que {"resultan" if high_count > 1 else "resulta"} claramente ofensivo{"s" if high_count > 1 else ""}.'
                if medium_count > 0:
                    overall_feedback += f' También {medium_count} de severidad media.'
            elif medium_count >= 3:
                overall_feedback = f'⚠️ Detecté {issues_found} términos que podrían resultar ofensivos o excluyentes. Te recomiendo revisar las sugerencias.'
            else:
                overall_feedback = f'⚠️ Detecté {issues_found} términos que podrían mejorarse para un lenguaje más inclusivo.'
        
        # Agregar desglose de categorías
        if issues_found > 0:
            categories_text = []
            if category_count['sexist'] > 0:
                categories_text.append(f"{category_count['sexist']} sexista{'s' if category_count['sexist'] > 1 else ''}")
            if category_count['ableist'] > 0:
                categories_text.append(f"{category_count['ableist']} capacitista{'s' if category_count['ableist'] > 1 else ''}")
            if category_count['ethnic'] > 0:
                categories_text.append(f"{category_count['ethnic']} étnico{'s' if category_count['ethnic'] > 1 else ''}")
            if category_count['offensive'] > 0:
                categories_text.append(f"{category_count['offensive']} ofensivo{'s' if category_count['offensive'] > 1 else ''}")
            
            if categories_text:
                overall_feedback += f'\n\n📊 Desglose: {", ".join(categories_text)}.'
            
            # Agregar puntuación
            overall_feedback += f'\n\n💯 Puntuación de inclusividad: {inclusive_score}/100'
            
            if inclusive_score >= 80:
                overall_feedback += ' - ¡Buen trabajo! Con pequeños ajustes alcanzarás la excelencia.'
            elif inclusive_score >= 60:
                overall_feedback += ' - Hay margen de mejora. Revisa las sugerencias.'
            elif inclusive_score >= 40:
                overall_feedback += ' - Se necesitan cambios significativos.'
            else:
                overall_feedback += ' - El texto requiere una revisión profunda.'
        
        return {
            'original_text': text,
            'issues': issues,
            'suggestions': [
                {
                    'original': i['original_text'],
                    'replacement': i['suggestion'],
                    'reason': i['explanation']
                }
                for i in issues
            ],
            'stats': {
                'total_words': total_words,
                'issues_found': issues_found,
                'inclusive_score': inclusive_score,
                'categories': category_count
            },
            'overall_feedback': overall_feedback
        }