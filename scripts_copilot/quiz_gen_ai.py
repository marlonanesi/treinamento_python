import tkinter as tk
import openai
from config import API_KEY

# Configurar a chave da API OpenAI
openai.api_key = API_KEY

def gerar_pergunta():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente de quiz."},
            {"role": "user", "content": "Por favor, me forneça uma pergunta de Verdadeiro ou Falso sobre Python."}
        ]
    )
    pergunta = response.choices[0].message['content']
    pergunta_text.config(state=tk.NORMAL)
    pergunta_text.delete(1.0, tk.END)
    pergunta_text.insert(tk.END, pergunta)
    pergunta_text.config(state=tk.DISABLED)

def verificar_resposta(resposta_usuario):
    pergunta = pergunta_text.get(1.0, tk.END).strip()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente de quiz."},
            {"role": "user", "content": f"Qual é a resposta correta para a pergunta: '{pergunta}'? Por favor, forneça a resposta e uma explicação."}
        ]
    )
    resposta_correta = response.choices[0].message['content']
    resultado_text.config(state=tk.NORMAL)
    resultado_text.delete(1.0, tk.END)
    if resposta_usuario in resposta_correta:
        resultado_text.insert(tk.END, "✅ Resposta correta!", "correta")
    else:
        resultado_text.insert(tk.END, "❌ Resposta errada!", "errada")
    resultado_text.config(state=tk.DISABLED)
    
    explicacao_text.config(state=tk.NORMAL)
    explicacao_text.delete(1.0, tk.END)
    explicacao_text.insert(tk.END, resposta_correta)
    explicacao_text.config(state=tk.DISABLED)

# Configuração da interface gráfica com Tkinter
root = tk.Tk()
root.title("Quiz Inteligente de Python")
root.geometry("500x350")  # Define o tamanho da janela para 500x350 pixels

pergunta_text = tk.Text(root, wrap=tk.WORD, height=5, width=60)
pergunta_text.pack(pady=10)
pergunta_text.config(state=tk.DISABLED)

resultado_text = tk.Text(root, wrap=tk.WORD, height=2, width=60)
resultado_text.pack(pady=10)
resultado_text.tag_config("correta", foreground="green")
resultado_text.tag_config("errada", foreground="red")
resultado_text.config(state=tk.DISABLED)

explicacao_text = tk.Text(root, wrap=tk.WORD, height=5, width=60)
explicacao_text.pack(pady=10)
explicacao_text.config(state=tk.DISABLED)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn_gerar = tk.Button(btn_frame, text="Gerar Pergunta", command=gerar_pergunta)
btn_gerar.pack(side=tk.LEFT, padx=10)

btn_verdadeiro = tk.Button(btn_frame, text="Verdadeiro", command=lambda: verificar_resposta("Verdadeiro"))
btn_verdadeiro.pack(side=tk.LEFT, padx=10)

btn_falso = tk.Button(btn_frame, text="Falso", command=lambda: verificar_resposta("Falso"))
btn_falso.pack(side=tk.LEFT, padx=10)

root.mainloop()