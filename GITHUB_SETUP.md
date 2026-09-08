# 🚀 Como Subir o Dashboard no GitHub Pages

Guia completo e simples para hospedar o dashboard ETEC no GitHub (GRÁTIS!).

## ⚙️ Pré-requisitos

- Conta no GitHub (gratuita): https://github.com/signup
- Git instalado no PC: https://git-scm.com/download/win

## 📋 Passo a Passo (5 minutos)

### PASSO 1: Criar repositório no GitHub

1. Acesse https://github.com/new
2. Preencha:
   - **Repository name:** `etec-simulados`
   - Deixe como **Public** (para que o link funcione)
3. Clique em **Create repository**

### PASSO 2: Preparar os arquivos no PC

1. Crie uma pasta no seu PC:
   ```
   C:\Users\SEU_USUARIO\Documents\etec-simulados
   ```

2. Copie para essa pasta:
   - `index.html` (renomeie de dashboard-etec-completo-v2.html)
   - `dashboard-etec-plano-reformulado.html`
   - `questoes_etec_completas.json`
   - `README.md`
   - Crie um arquivo vazio chamado `.gitignore`

### PASSO 3: Inicializar Git Localmente

1. Abra **Terminal** ou **Command Prompt** na pasta:
   - Windows: Shift + Clique direito → "Abrir PowerShell aqui"
   - Mac/Linux: Clique direito → "Abrir Terminal"

2. Execute os comandos:

```bash
# Inicializar Git
git init

# Adicionar todos os arquivos
git add .

# Fazer commit
git commit -m "Initial commit: ETEC Dashboard com 299 questões"

# Renomear branch para main (se necessário)
git branch -M main

# Adicionar repositório remoto (COPIE DO GITHUB!)
git remote add origin https://github.com/SEU_USUARIO/etec-simulados.git

# Fazer upload
git push -u origin main
```

**⚠️ Importante:** Substitua `SEU_USUARIO` pelo seu usuário GitHub

### PASSO 4: Ativar GitHub Pages

1. Vá para seu repositório no GitHub
2. Clique em **Settings** (engrenagem)
3. No menu esquerdo, clique em **Pages**
4. Em "Source", selecione:
   - Branch: `main`
   - Folder: `/ (root)`
5. Clique em **Save**

### PASSO 5: Compartilhar o Link

Após 2-3 minutos, seu dashboard estará disponível em:

```
https://seu-usuario.github.io/etec-simulados/
```

Exemplo: Se seu usuário é `fernanda-silva`, o link será:
```
https://fernanda-silva.github.io/etec-simulados/
```

**Copie este link e compartilhe com quem quiser! 🎉**

---

## ✨ Como Atualizar o Dashboard (se precisar)

Se você quiser adicionar mais questões ou modificar algo:

```bash
# Modifique os arquivos no PC

# Faça commit das mudanças
git add .
git commit -m "Descrição do que mudou"

# Envie para GitHub
git push
```

Em 1-2 minutos, as mudanças estarão online!

---

## 🎯 Resultado Final

Seu dashboard estará:
- ✅ Online e compartilhável
- ✅ Com histórico de 299 questões
- ✅ 100% funcional (sem backend necessário)
- ✅ Grátis para sempre
- ✅ Disponível 24/7

---

## ❓ FAQ

### P: Posso usar em mobile?
**R:** Sim! O link funciona em PC, tablet e celular.

### P: Funciona sem internet?
**R:** Não. Precisa de internet para acessar o GitHub Pages, mas depois que carrega, o localStorage funciona offline.

### P: Posso fazer backup?
**R:** Sim! Git é controle de versão. Todo push cria um backup automático.

### P: Quanto custa?
**R:** GRATUITO! GitHub Pages é totalmente grátis para projetos públicos.

### P: Preciso mexer em código?
**R:** Não! Só copiar arquivos e executar comandos git.

---

## 📞 Troubleshooting

### "Não consigo encontrar o Terminal"
- Windows: Abra "Command Prompt" ou "PowerShell" pelo menu Iniciar
- Mac: Applications → Utilities → Terminal
- Linux: Já sabe, hehe 😉

### "Git não é reconhecido"
- Instale Git novamente: https://git-scm.com/download/win
- Reinicie o PC após instalar

### "GitHub Pages não aparece"
- Aguarde 5-10 minutos
- Verifique se o repositório é **Public** (não Private)
- Vá em Settings → Pages e confirme que está ativado

### "Meus dados sumiram"
- localStorage foi limpo do navegador
- Isso é normal - dados ficam salvos apenas no seu navegador/PC

---

**Dúvidas?** Consulte:
- https://docs.github.com/pt/pages/getting-started-with-github-pages
- https://git-scm.com/book/pt-br

**Bom luck! 🍀**
