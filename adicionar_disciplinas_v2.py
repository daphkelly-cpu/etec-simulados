#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Adiciona campo 'disciplina' em cada questão do JSON
Procura arquivo automaticamente e classifica por análise de texto
"""

import json
import glob
import os

def classify_question(text):
    """Classifica questão por disciplina baseado em palavras-chave"""
    text_lower = text.lower()
    
    keywords = {
        'Português': [
            'texto', 'frase', 'palavra', 'verbo', 'substantivo', 'adjetivo', 
            'gramática', 'coesão', 'coerência', 'reescrita', 'análise textual', 
            'interpretação', 'leitura', 'canção', 'poema', 'prosa'
        ],
        'Matemática': [
            'equação', 'número', 'cálculo', 'produto', 'soma', 'divisão', 
            'percentual', '%', 'gráfico', 'tabela', 'média', 'probabilidade', 
            'geometria', 'área', 'volume', 'ângulo', 'notação científica'
        ],
        'Geografia': [
            'mapa', 'região', 'clima', 'bioma', 'vegetação', 'rio', 'latitude', 
            'longitude', 'país', 'continente', 'território', 'amazônia', 'cerrado', 
            'oceano', 'altitude', 'relevo'
        ],
        'Ciências': [
            'célula', 'dna', 'genética', 'evolução', 'espécie', 'ecologia', 
            'cadeia alimentar', 'energia', 'força', 'velocidade', 'luz', 'som', 
            'temperatura', 'reação química', 'átomo', 'molécula', 'biologia', 
            'física', 'química', 'fenômeno', 'organismo'
        ],
        'História': [
            'século', 'ano', 'período', 'guerra', 'república', 'império', 
            'colonização', 'rebelião', 'revolução', 'brasil', 'portugal', 'escravidão', 
            'abolição', 'independência', 'ditadura', 'democracia'
        ]
    }
    
    scores = {disc: 0 for disc in keywords}
    
    for disciplina, words in keywords.items():
        for word in words:
            if word in text_lower:
                scores[disciplina] += 1
    
    if max(scores.values()) > 0:
        return max(scores, key=scores.get)
    return 'Outros'

# MAIN
print("=" * 70)
print("📚 Adicionando Disciplinas ao JSON...")
print("=" * 70)

# Procurar arquivo
json_files = glob.glob('*questoes*.json')

print(f"\nDiretório: {os.getcwd()}")
print(f"Arquivos encontrados: {json_files}")

if not json_files:
    print("\n❌ Nenhum arquivo de questões encontrado!")
    exit(1)

json_file = json_files[0]
print(f"✅ Usando: {json_file}\n")

# Carregar
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

total = 0
disciplinas_count = {}

# Processar
for prova_num in sorted(data.keys()):
    prova = data[prova_num]
    print(f"🔍 Prova {prova_num}:")
    
    prova_disciplinas = {}
    
    for q_id in prova:
        q = prova[q_id]
        
        # Combinar texto + alternativas
        texto_completo = q.get('texto', '') + ' ' + ' '.join(q.get('alternativas', {}).values())
        
        # Classificar
        disciplina = classify_question(texto_completo)
        q['disciplina'] = disciplina
        
        # Contar
        prova_disciplinas[disciplina] = prova_disciplinas.get(disciplina, 0) + 1
        total += 1
    
    # Mostrar resumo
    for disc, count in sorted(prova_disciplinas.items()):
        print(f"   {disc:20s}: {count:2d}")
        disciplinas_count[disc] = disciplinas_count.get(disc, 0) + count

# Salvar
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 70)
print("✅ JSON Atualizado com Disciplinas!")
print("=" * 70)
print("\n📊 RESUMO TOTAL:")
for disc in ['Português', 'Matemática', 'Geografia', 'História', 'Ciências', 'Outros']:
    count = disciplinas_count.get(disc, 0)
    if count > 0:
        print(f"   {disc:20s}: {count:3d}")

print(f"\n   TOTAL: {total} questões")
