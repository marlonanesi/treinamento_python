# 📝 Aula 16: Introdução ao Hugging Face Transformers

## 📌 Introdução

A biblioteca **Hugging Face Transformers** é uma das mais populares do mundo para trabalhar com **modelos de linguagem (LLMs)** como BERT, GPT, DistilBERT e outros.

Ela permite que você use **modelos pré-treinados** com poucas linhas de código para tarefas como:

1. **Análise de sentimentos**
2. **Geração de texto**
3. **Pergunta e resposta**
4. **Tradução automática**

Nesta aula, vamos:
- Entender o que é a Hugging Face
- Usar o `pipeline` para testar modelos prontos
- Aplicar análise de sentimentos em frases reais
- Testar outras tarefas como geração de texto, QA e tradução
- Entender como funciona a execução local dos modelos

---

## 📌 1. O que é a Hugging Face?

É uma empresa que criou um repositório de **modelos de machine learning open-source** e uma biblioteca poderosa para integrar esses modelos no seu código Python com simplicidade.

> **🔹 Instalação**
```bash
pip install transformers
```

---

## 📌 2. Como funciona a `pipeline` da Hugging Face?

Quando você chama a função `pipeline`, ela:

1. **Verifica localmente** se o modelo necessário já foi baixado;
2. Se ainda não tiver, **baixa o modelo automaticamente** do repositório da Hugging Face (via internet);
3. **Armazena em cache** no seu computador (por padrão, na pasta `~/.cache/huggingface`);
4. Utiliza o modelo **localmente**, sem necessidade de nova conexão com a internet após o download inicial.

Ou seja, **o modelo é executado localmente**, sem enviar dados para servidores externos. Após o primeiro uso, não é necessário estar conectado à internet para utilizá-lo novamente (exceto para modelos que exigem dependências externas específicas).

---

## 📌 3. Usando o pipeline para análise de sentimentos

A função `pipeline` permite testar tarefas complexas com apenas uma linha de código.

### 🔹 Exemplo prático
```python
from transformers import pipeline

# Carregando o pipeline para análise de sentimentos
analisador = pipeline("sentiment-analysis")

# Frase de exemplo
resultado = analisador("Esse curso está incrível, estou aprendendo muito!")
print(resultado)
```

📝 **Saída esperada:**
```
[{'label': 'POSITIVE', 'score': 0.9998}]
```

### 🔍 Entendendo a saída
- **label**: a classificação feita pelo modelo (ex: POSITIVE ou NEGATIVE)
- **score**: a confiança do modelo nessa classificação (quanto mais próximo de 1, mais confiante ele está)

Você pode testar com frases negativas também:
```python
print(analisador("Não gostei da aula de hoje."))
```

📝 **Saída:**
```
[{'label': 'NEGATIVE', 'score': 0.9985}]
```

---

## 📌 4. Explorando outros tipos de pipeline

### 🔹 Geração de texto
Gera uma continuação a partir de uma frase inicial.
```python
from transformers import pipeline

gerador = pipeline("text-generation")
resposta = gerador("Aprender Python com IA é", max_length=30)
print(resposta[0]['generated_text'])
```

📝 **Saída exemplo:**
```
Aprender Python com IA é uma das habilidades mais procuradas no mercado de tecnologia atual.
```

### 🔹 Pergunta e resposta
Recebe uma pergunta e um contexto para buscar a resposta.
```python
qa = pipeline("question-answering")
resposta = qa({
    "question": "Quem criou o Python?",
    "context": "Python foi criado por Guido van Rossum e lançado em 1991."
})
print(resposta['answer'])
```

📝 **Saída esperada:**
```
Guido van Rossum
```

### 🔹 Tradução automática
Traduz frases de um idioma para outro.
```python
tradutor = pipeline("translation_en_to_fr")
print(tradutor("Hello, how are you?"))
```

📝 **Saída esperada:**
```
[{'translation_text': 'Bonjour, comment ça va ?'}]
```

---

## 🏆 Conclusão

- **Transformers** da Hugging Face trazem acesso fácil a modelos de IA avançados
- Usar o `pipeline` é a forma mais simples de começar com tarefas como análise de sentimentos, geração de texto e mais
- Os modelos são executados localmente após o primeiro download, sem necessidade de enviar dados para a nuvem
- Você não precisa de GPU ou conhecimento profundo em redes neurais para começar

Na próxima aula, podemos expandir esses conceitos para criar aplicações com **entrada de usuário**, ou até integrar esses recursos com **Streamlit** para criar uma interface interativa.

