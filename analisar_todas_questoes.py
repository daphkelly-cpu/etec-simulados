#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise Completa do JSON - Identifica problemas em TODAS as questões
"""

import json
import glob
import re

json_files = glob.glob('*questoes*.json')

if not json_files:
    print("❌ Nenhum arquivo encontrado!")
    exit(1)

json_file = json_files[0]
print(f"📄 Analisando: {json_file}\n")
print("=" * 80)

# Carregar
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

problemas = {
    'alternativas_muito_longas': [],
    'enunciados_misturados': [],
    'alternativas_vazias': [],
    'texto_questao_vazio': [],
    'sem_alternativas': [],
}

# Padrões que indicam mistura de questões
padroes_mistura = [
    r'Questão\s+\d+',
    r'assinale',
    r'indique',
    r'de acordo com',
    r'é correto afirmar',
    r'a alternativa que',
]

# Analisar cada prova
total_questoes = 0
total_alternativas = 0

for prova_num in sorted(data.keys()):
    prova = data[prova_num]
    
    print(f"\n🔍 PROVA {prova_num}:")
    print("-" * 80)
    
    for q_id in sorted([int(x) for x in prova.keys()]):
        q_id_str = str(q_id)
        q = prova[q_id_str]
        total_questoes += 1
        
        # 1. Verificar texto da questão
        if not q.get('texto', '').strip():
            problemas['texto_questao_vazio'].append((prova_num, q_id))
            print(f"  ❌ Q{q_id}: TEXTO VAZIO")
            continue
        
        # 2. Verificar se tem alternativas
        if 'alternativas' not in q or not q['alternativas']:
            problemas['sem_alternativas'].append((prova_num, q_id))
            print(f"  ❌ Q{q_id}: SEM ALTERNATIVAS")
            continue
        
        # 3. Verificar alternativas
        tem_problema = False
        for letra in ['A', 'B', 'C', 'D', 'E']:
            if letra not in q['alternativas']:
                continue
            
            alt = q['alternativas'][letra]
            total_alternativas += 1
            
            # Verificar se está vazia
            if not alt or not alt.strip():
                problemas['alternativas_vazias'].append((prova_num, q_id, letra))
                print(f"  ⚠️  Q{q_id} Alt({letra}): VAZIA")
                tem_problema = True
                continue
            
            # Verificar se tem enunciado de outra questão
            tem_mistura = False
            for padrao in padroes_mistura:
                if re.search(padrao, alt, re.IGNORECASE):
                    # Se tem "Questão XX" é mistura clara
                    if 'Questão' in alt or 'questão' in alt:
                        problemas['enunciados_misturados'].append((prova_num, q_id, letra))
                        print(f"  ❌ Q{q_id} Alt({letra}): MISTURADA COM PRÓXIMO ENUNCIADO")
                        print(f"     {alt[:100]}...")
                        tem_mistura = True
                        tem_problema = True
                        break
            
            # Verificar se está muito longa
            if len(alt) > 500 and not tem_mistura:
                problemas['alternativas_muito_longas'].append((prova_num, q_id, letra, len(alt)))
                print(f"  ⚠️  Q{q_id} Alt({letra}): MUITO LONGA ({len(alt)} chars)")
                print(f"     {alt[:80]}...")
                tem_problema = True
        
        if not tem_problema:
            print(f"  ✅ Q{q_id}: OK")

print("\n" + "=" * 80)
print("📊 RESUMO DA ANÁLISE:")
print("=" * 80)
print(f"\n✅ Total de questões analisadas: {total_questoes}")
print(f"✅ Total de alternativas analisadas: {total_alternativas}")

print(f"\n❌ PROBLEMAS ENCONTRADOS:\n")

if problemas['enunciados_misturados']:
    print(f"🔴 Enunciados misturados: {len(problemas['enunciados_misturados'])} alternativas")
    for prova, q_id, letra in problemas['enunciados_misturados'][:5]:
        print(f"   - Prova {prova}, Questão {q_id}, Alternativa {letra}")
    if len(problemas['enunciados_misturados']) > 5:
        print(f"   ... e mais {len(problemas['enunciados_misturados']) - 5}")

if problemas['alternativas_muito_longas']:
    print(f"\n🟡 Alternativas muito longas: {len(problemas['alternativas_muito_longas'])} alternativas")
    for prova, q_id, letra, length in problemas['alternativas_muito_longas'][:5]:
        print(f"   - Prova {prova}, Questão {q_id}, Alternativa {letra} ({length} chars)")
    if len(problemas['alternativas_muito_longas']) > 5:
        print(f"   ... e mais {len(problemas['alternativas_muito_longas']) - 5}")

if problemas['alternativas_vazias']:
    print(f"\n🟡 Alternativas vazias: {len(problemas['alternativas_vazias'])} alternativas")
    for prova, q_id, letra in problemas['alternativas_vazias'][:5]:
        print(f"   - Prova {prova}, Questão {q_id}, Alternativa {letra}")
    if len(problemas['alternativas_vazias']) > 5:
        print(f"   ... e mais {len(problemas['alternativas_vazias']) - 5}")

if problemas['texto_questao_vazio']:
    print(f"\n🔴 Textos vazios: {len(problemas['texto_questao_vazio'])} questões")
    for prova, q_id in problemas['texto_questao_vazio'][:5]:
        print(f"   - Prova {prova}, Questão {q_id}")

if problemas['sem_alternativas']:
    print(f"\n🔴 Sem alternativas: {len(problemas['sem_alternativas'])} questões")
    for prova, q_id in problemas['sem_alternativas'][:5]:
        print(f"   - Prova {prova}, Questão {q_id}")

total_problemas = sum(len(v) for v in problemas.values())
print(f"\n" + "=" * 80)
print(f"TOTAL DE PROBLEMAS: {total_problemas}")
print("=" * 80)

if total_problemas == 0:
    print("\n✅ NENHUM PROBLEMA ENCONTRADO! JSON está LIMPO!")
else:
    print(f"\n⚠️  ENCONTRADOS {total_problemas} PROBLEMAS")
    print("   Corrija antes de fazer upload!")
