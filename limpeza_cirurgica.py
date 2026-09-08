#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remove APENAS metadados de alternativas, preservando o conteúdo real
"""

import json
import glob
import os
import re

json_files = glob.glob('*questoes*.json')

if not json_files:
    print("❌ Nenhum arquivo encontrado!")
    exit(1)

json_file = json_files[0]
print(f"📄 Limpeza CIRÚRGICA de: {json_file}\n")

# Carregar
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

removidas = 0
padroes_lixo = [
    # Metadados de exame
    r'VESTIBULINHO\s+\d+[a-z]*\s+semestre\s*\|\s*\d{4}',
    r'VESTIBULINHO\s+\d+[a-z]*\s+semestre\s*\|\s*\d{4}[^.]*\.',
    r'Exam:\s*\d+/\d+/\d{4}',
    r'\d{1,2}[a-z]*\s+VESTIBULINHO[^.]*',
    r'VESTIBULINHO\s+2o semestre',
    r'VESTIBULINHO\s+1o semestre',
    
    # Instruções de resposta
    r'Leia o texto para responder.*?(?=\(A\)|$)',
    r'responda às questões.*?(?=\(A\)|$)',
    r'assinale a alternativa.*?(?=\(A\)|$)',
    
    # Padrões de lixo OCR
    r'[A-Z]{2,}\s+CCAANNDDDD',
    r'[A-Z]{2,}\s+DDDEEEE',
    r'[A-Z]{2,}\s+FFOOOLLL',
    
    # Números de processo/código
    r'0\d{3}/\d{4}',
    r'\d{4}-\d{4}-\d{4}-\d{4}',
]

# Processar cada prova
for prova_num in sorted(data.keys()):
    prova = data[prova_num]
    
    for q_id in prova:
        q = prova[q_id]
        
        if 'alternativas' not in q:
            continue
        
        for letra in ['A', 'B', 'C', 'D', 'E']:
            if letra not in q['alternativas']:
                continue
            
            alt = q['alternativas'][letra]
            alt_original = alt
            
            # Aplicar cada padrão de lixo
            for padrao in padroes_lixo:
                # Encontrar e remover o padrão
                alt = re.sub(padrao, '', alt, flags=re.IGNORECASE | re.MULTILINE)
            
            # Limpar espaços múltiplos e quebras
            alt = re.sub(r'\s+', ' ', alt).strip()
            
            # Se mudou, registrar
            if alt != alt_original:
                print(f"🧹 Prova {prova_num}, Q{q_id}, Alt({letra}):")
                print(f"   Antes: {alt_original[:80]}...")
                print(f"   Depois: {alt[:80]}...")
                removidas += 1
            
            q['alternativas'][letra] = alt

# Renomear backup
backup_file = json_file + '.backup'
if os.path.exists(backup_file):
    os.remove(backup_file)
os.rename(json_file, backup_file)

# Salvar limpo
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n" + "=" * 70)
print(f"✅ LIMPEZA CIRÚRGICA CONCLUÍDA!")
print(f"   Alternativas limpas: {removidas}")
print("=" * 70)
