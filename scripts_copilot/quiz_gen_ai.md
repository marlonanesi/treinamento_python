Gere um código Python que implementa um jogo de Quiz usando Tkinter e a API ChatCompletion da OpenAI. 

📌 **Detalhes do código:**
- Importar a chave da OpenAI do arquivo `config.py` com `from config import API_KEY`.
- Importar as bibliotecas `tkinter` e `openai`.
- Configurar a chave da API OpenAI com `openai.api_key = API_KEY`.

📌 **Funções necessárias:**
1. **`gerar_pergunta()`**:
   - Deve chamar a API `ChatCompletion` com o modelo `"gpt-3.5-turbo"`.
   - Deve enviar uma mensagem para a IA pedindo uma pergunta de **Verdadeiro ou Falso sobre Python**.
   - A pergunta gerada deve ser exibida em um `Label` chamado `pergunta_label`.

2. **`verificar_resposta(resposta_usuario)`**:
   - Deve obter o texto da pergunta exibida em `pergunta_label`.
   - Deve chamar a API `ChatCompletion` perguntando **qual é a resposta correta e uma explicação**.
   - Se a resposta do usuário estiver correta, exibir "✅ Resposta correta!" em um `Label` chamado `resultado_label`.
   - Se a resposta estiver errada, exibir "❌ Resposta errada!" no mesmo `Label`.
   - Exibir a explicação retornada pela IA em um `Label` chamado `explicacao_label`.

📌 **Interface gráfica com Tkinter:**
- Criar um `Tk()` chamado `root` com título **"Quiz Inteligente de Python"**.
- Criar um `Label` chamado `pergunta_label` com um texto inicial **"Clique abaixo para gerar uma pergunta!"**.
- Criar um botão `btn_gerar` que chama `gerar_pergunta()`.
- Criar dois botões: 
  - `btn_verdadeiro`, que chama `verificar_resposta("Verdadeiro")`.
  - `btn_falso`, que chama `verificar_resposta("Falso")`.
- Criar um `Label` chamado `resultado_label` para mostrar se a resposta está correta ou não.
- Criar um `Label` chamado `explicacao_label` para mostrar a explicação da IA.
- Iniciar o loop principal com `root.mainloop()`.
