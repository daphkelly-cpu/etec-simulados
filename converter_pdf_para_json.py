#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Converter PDF Provas ETEC para JSON Estruturado
Extrai questões e alternativas de PDFs e gera JSON limpo
"""

import json
import re
from pdfplumber import PDF
import sys

def extract_questions_from_pdf(pdf_path, prova_num, gabarito):
    """Extrai questões de um PDF e retorna estrutura JSON"""
    questions = {}
    
    with PDF.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"
    
    # Padrão: "Questão XX" seguido de alternativas
    pattern = r'Questão\s*(\d+)\n(.+?)(?=Questão\s*\d+|$)'
    matches = re.finditer(pattern, full_text, re.DOTALL)
    
    for match in matches:
        q_num = int(match.group(1))
        q_content = match.group(2).strip()
        
        # Extrair texto da questão (antes de (A))
        text_pattern = r'^(.+?)\(A\)'
        text_match = re.match(text_pattern, q_content, re.DOTALL)
        
        if text_match:
            question_text = text_match.group(1).strip()
            question_text = ' '.join(question_text.split())  # Limpar espaços
            
            # Extrair alternativas
            alt_pattern = r'\(([A-E])\)\s*(.+?)(?=\([A-E]\)|$)'
            alt_matches = re.finditer(alt_pattern, q_content, re.DOTALL)
            
            alternatives = {}
            for alt_match in alt_matches:
                alt_letter = alt_match.group(1)
                alt_text = alt_match.group(2).strip()
                # Limitar a 300 caracteres e limpar
                alt_text = ' '.join(alt_text.split())
                if len(alt_text) > 300:
                    alt_text = alt_text[:297] + "..."
                alternatives[alt_letter] = alt_text
            
            # Pegar resposta do gabarito
            correct_answer = gabarito.get(q_num, "?")
            
            if alternatives:  # Só adicionar se tem alternativas
                questions[q_num] = {
                    "numero": q_num,
                    "texto": question_text,
                    "alternativas": alternatives,
                    "resposta_correta": correct_answer
                }
    
    return questions

def load_gabaritos():
    """Carrega os gabaritos das provas"""
    import glob
    import re
    
    gabaritos = {}
    
    # Procurar por qualquer arquivo com "abarito" no nome
    gabarito_files = glob.glob('*abarito*.json') + glob.glob('*abarito*.pdf')
    
    print(f"🔍 Procurando por gabaritos...")
    
    for fname in gabarito_files:
        try:
            with open(fname, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Extrair número da prova do nome do arquivo
                match = re.search(r'(\d+)', fname)
                if match:
                    num = int(match.group(1))
                    if 1 <= num <= 6:  # Validar se é prova 1-6
                        gabaritos[num] = {
                            int(item['question_number']): item['alternative'].split()[0]
                            for item in data['answers']
                        }
                        print(f"   ✅ Prova {num}: {len(gabaritos[num])} questões")
        except Exception as e:
            pass  # Silencioso se falhar
    
    return gabaritos

def main():
    print("=" * 60)
    print("🔄 Convertendo PDFs para JSON...")
    print("=" * 60)
    
    # Carregar gabaritos
    gabaritos = load_gabaritos()
    
    if not gabaritos:
        print("❌ Nenhum gabarito encontrado!")
        sys.exit(1)
    
    # Provas
    pdf_files = [
        ('Prova1.pdf', 1),
        ('Prova2.pdf', 2),
        ('Prova3.pdf', 3),
        ('Prova4.pdf', 4),
        ('prova5.pdf', 5),
        ('prova6.pdf', 6),
    ]
    
    all_questions = {}
    
    for pdf_path, num in pdf_files:
        print(f"\n📄 Processando Prova {num}...")
        try:
            questions = extract_questions_from_pdf(
                pdf_path, 
                num, 
                gabaritos.get(num, {})
            )
            all_questions[num] = questions
            print(f"   ✅ {len(questions)} questões extraídas")
            
            if questions:
                q1 = list(questions.values())[0]
                print(f"   Q1: {q1['texto'][:60]}...")
                print(f"   Alternativas: {list(q1['alternativas'].keys())}")
                print(f"   Resposta: {q1['resposta_correta']}")
        except FileNotFoundError:
            print(f"   ❌ Arquivo {pdf_path} não encontrado")
        except Exception as e:
            print(f"   ❌ Erro: {str(e)[:100]}")
    
    # Salvar JSON
    output = {str(k): {str(qk): qv for qk, qv in v.items()} 
              for k, v in all_questions.items()}
    
    output_file = 'questoes_etec_completas_limpo.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print("\n" + "=" * 60)
    print(f"✅ Arquivo salvo: {output_file}")
    print("=" * 60)
    
    # Estatísticas
    total = sum(len(v) for v in all_questions.values())
    print(f"\n📊 RESUMO:")
    for num in sorted(all_questions.keys()):
        print(f"   Prova {num}: {len(all_questions[num])} questões")
    print(f"   TOTAL: {total} questões")

if __name__ == "__main__":
    main()
