# 🤖 Amazon Q Developer - Guia Prático

## 📋 O que é?

Amazon Q Developer é um **assistente de IA da AWS** que acelera desenvolvimento de código, especialmente Python. Oferece autocompletar inteligente, chat para dúvidas e geração de código.

## 🚀 Instalação Rápida

1. **VS Code** → Extensions (Ctrl+Shift+X)
2. Busque **"Amazon Q Developer"**
3. **Install** → Clique no ícone Q na barra lateral
4. **"Use for free"** → Login com conta AWS

## 🆓 Plano Gratuito

### ✅ Ilimitado:
- **Autocompletar** enquanto digita
- **Sugestões inline** (Ctrl+I)
- **Geração de código** básica

### 📊 Limitado:
- **50 conversas/mês** no chat
- Uma conversa = múltiplas mensagens
- **Sem contador visível** de uso

## 🛠 Funcionalidades Principais

### 1. Autocompletar Inteligente
```python
# Digite "def calcular" e veja sugestões automáticas
def calcular_media(lista):
    return sum(lista) / len(lista)
```

### 2. Chat para Dúvidas
**Exemplos de perguntas:**
- "Como ler CSV com pandas?"
- "Diferença entre list e tuple?"
- "Explique este código: [cole código]"

### 3. Geração de Código
- Descreva o que precisa
- Receba código funcional
- Suporte a bibliotecas populares

## ⚡ Atalhos Essenciais

- **Tab**: Aceita sugestão
- **Esc**: Cancela sugestão
- **Ctrl+I**: Chat inline no editor
- **Alt+C**: Abre painel Q

## 🐍 Para Python

### Bibliotecas Suportadas:
- **Data Science**: pandas, numpy, matplotlib
- **ML**: scikit-learn, tensorflow
- **Web**: flask, django, fastapi
- **Automação**: requests, selenium

### Recursos Python:
- **PEP 8** compliance
- **Type hints** automáticos
- **Docstrings** geradas
- **Debug** de erros

## 💡 Dicas de Uso

### ✅ Seja Específico:
```
❌ "Como usar pandas?"
✅ "Como filtrar DataFrame por múltiplas condições?"
```

### ✅ Forneça Contexto:
```
❌ "Meu código não funciona"
✅ "KeyError ao acessar dict. Código: [cole aqui]"
```

## 🎯 Casos de Uso

1. **Aprendizado**: Explicações de conceitos
2. **Desenvolvimento**: Código boilerplate rápido
3. **Debug**: Análise de erros
4. **Testes**: Geração de unit tests
5. **Refatoração**: Melhoria de código

## ⚠️ Limitações

- **50 conversas/mês** (chat)
- **Sem monitoramento** de uso
- **Conexão internet** necessária
- **Sempre revisar** código gerado

## 📝 Exemplo Prático

```python
# 1. Comente o que quer
# Função para conectar API e retornar JSON

# 2. Q sugere automaticamente:
import requests

def conectar_api(url):
    response = requests.get(url)
    return response.json()

# 3. Use chat: "Gere testes para esta função"
```

## 🔗 Links Úteis

- [Documentação AWS](https://aws.amazon.com/q/developer/)
- Tutoriais no painel da extensão
- Comunidade AWS Forums

---

**💡 Dica**: Use Amazon Q como **assistente inteligente** que complementa suas habilidades. Autocompletar é ilimitado, então aproveite ao máximo enquanto programa!