# 📚 Dashboard ETEC Vestibulinho - Simulados Completos

Um dashboard interativo para praticar e acompanhar o progresso nos simulados do Vestibulinho ETEC.

## 🎯 Funcionalidades

✅ **6 Provas Completas** - 300+ questões extraídas de provas reais (2023-2026)  
✅ **Modo Simulado** - 50 questões, 4 horas, cronômetro (como prova real)  
✅ **Histórico Completo** - Todos os simulados salvos localmente  
✅ **Estatísticas** - Desempenho por disciplina (Português, Matemática, Geografia, etc)  
✅ **Plano de 12 Semanas** - Cronograma integrado com vídeos de aula  
✅ **Sem Login Necessário** - Funciona 100% no navegador (localStorage)  
✅ **Offline** - Estudar em qualquer lugar, sem internet  

## 🚀 Como Usar

### Opção 1: Online (GitHub Pages)

Abra o link no navegador:
```
https://seu-usuario.github.io/etec-simulados/
```

### Opção 2: Local

1. Clone ou baixe os arquivos
2. Abra `dashboard-etec-completo-v2.html` no navegador
3. Pronto! Comece a estudar

## 📱 Funcionalidades Detalhadas

### 🎯 Simulado
- Escolha uma prova (1 a 6)
- Responda 50 questões em 4 horas
- Cronômetro em tempo real
- Alerta quando falta 30 minutos
- Resultado imediato com score

### 📊 Histórico
- Veja todos os simulados que fez
- Data, prova, acertos e score
- Tempo utilizado em cada um
- Salvo automaticamente

### 📈 Estatísticas
- Desempenho por disciplina
- Gráfico visual de progresso
- Identifique pontos fracos

### 📋 Plano de Estudos
- 12 semanas de preparação
- Tópicos por semana
- Vídeos de aula integrados (YouTube)
- Checkboxes para marcar conclusão

## 💾 Dados Salvos

Todos os dados são salvos **localmente** no seu navegador usando `localStorage`:
- Histórico de simulados
- Respostas às questões
- Tempo de estudo

**Importante:** Os dados não são sincronizados entre dispositivos. Se você estudar em PC, mobile e tablet, cada um terá seu próprio histórico.

## 🔧 Instalação no GitHub Pages

### Passo 1: Criar repositório
```bash
mkdir etec-simulados
cd etec-simulados
git init
```

### Passo 2: Adicionar arquivos
```
Copie os seguintes arquivos para a pasta:
- dashboard-etec-completo-v2.html (renomeie para index.html)
- dashboard-etec-plano-reformulado.html
- questoes_etec_completas.json
```

### Passo 3: Push para GitHub
```bash
git add .
git commit -m "Initial commit: ETEC Dashboard"
git branch -M main
git remote add origin https://github.com/seu-usuario/etec-simulados.git
git push -u origin main
```

### Passo 4: Ativar GitHub Pages
1. Vá para Settings → Pages
2. Source: Branch `main`, folder `/root`
3. Salve

Seu dashboard estará em: `https://seu-usuario.github.io/etec-simulados/`

## 📊 Estrutura do Projeto

```
etec-simulados/
├── index.html (dashboard principal)
├── dashboard-etec-plano-reformulado.html (plano 12 semanas)
├── questoes_etec_completas.json (299 questões + gabaritos)
├── README.md (este arquivo)
└── .gitignore
```

## 🎓 Conteúdo das Provas

Cada prova contém 50 questões sobre:

### Disciplinas
- **Português** (10 questões) - Leitura, interpretação, análise textual
- **Matemática** (10 questões) - Cálculos, geometria, estatística
- **Geografia** (10 questões) - Biomas, clima, urbanização
- **História** (10 questões) - Brasil colonial, República, movimentos
- **Ciências/Biologia** (10 questões) - Célula, evolução, ecologia

### Provas Disponíveis
- Prova 1 (Dez 2023) - 50 questões
- Prova 2 (Jun 2024) - 50 questões  
- Prova 3 (Jun 2024) - 50 questões
- Prova 4 (Dez 2024) - 50 questões
- Prova 5 (Dez 2025) - 50 questões
- Prova 6 (Jun 2026) - 49 questões

**Total: 299 questões extraídas de provas reais**

## 🛠️ Tecnologia

- **Frontend:** HTML5, CSS3, JavaScript puro
- **Armazenamento:** localStorage (navegador)
- **Hosting:** GitHub Pages (gratuito)
- **Banco de Dados:** JSON local

## 📝 Dica de Ouro

1. Faça simulados regularmente (1x por semana)
2. Revise seus erros after each simulado
3. Estude os tópicos onde errou (veja o plano de 12 semanas)
4. Acompanhe seu progresso nas estatísticas
5. **Consistência > Perfeição** - Um dia ruim não derruba semanas de estudo!

## ⚠️ Conhecimentos Técnicos Necessários

**Nenhum!** Basta abrir o arquivo HTML no navegador. Não é necessário:
- Conhecimento de programação
- Instalação de nada
- Conexão com internet (após carregar os arquivos)

## 🐛 Problemas Comuns

### Questões não carregam
- Certifique-se que `questoes_etec_completas.json` está na mesma pasta do HTML
- Se usar servidor local, confirme que o JSON está sendo servido

### Histórico desapareceu
- localStorage foi limpo (cache do navegador)
- Abra DevTools (F12) → Application → localStorage para verificar

### Cronômetro não funciona
- Verifique se JavaScript está ativado
- Tente outro navegador

## 📞 Suporte

Se encontrar problemas:
1. Verifique os requisitos acima
2. Limpe o cache do navegador (Ctrl+Shift+Delete)
3. Tente outro navegador

## 📄 Licença

Este projeto é livre para uso pessoal e educacional.

---

**Versão:** 2.0  
**Data de Atualização:** Setembro 2026  
**Questões:** 299 (6 provas completas)  
**Última Prova:** Junho 2026  

**Boa sorte na prova! 🍀**
