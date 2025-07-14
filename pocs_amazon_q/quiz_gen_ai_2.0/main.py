from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
from config import API_KEY

app = FastAPI(title="Quiz Inteligente", version="2.0")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = API_KEY

class RespostaModel(BaseModel):
    pergunta: str
    resposta: str

# 1. O decorador @app.get("/") define a rota raiz ("/") para requisições GET
# 2. A função home recebe um objeto Request que contém informações sobre a requisição HTTP
# 3. templates.TemplateResponse renderiza o arquivo index.html localizado no diretório templates/
# 4. O dicionário {"request": request} passa o objeto request como contexto para o template
# 5. O Jinja2 usa esse contexto para renderizar o HTML dinâmico na página
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/gerar-pergunta")
async def gerar_pergunta():
    try:
        
        response = openai.ChatCompletion.create(
            model="gpt-4.1-mini",
            messages=[{
                "role": "user",
                "content": "Gere uma pergunta de Verdadeiro ou Falso sobre Python. Seja específico e educativo. Retorne apenas a pergunta."
            }]
        )
        # Esta linha extrai o texto da resposta gerada pela API do OpenAI
        # response.choices[0] - pega a primeira resposta retornada (geralmente só há uma)
        # .message.content - acessa o conteúdo da mensagem dentro da resposta
        # .strip() - remove espaços em branco extras no início e fim do texto
        pergunta = response.choices[0].message.content.strip()
        return {"pergunta": pergunta}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao gerar pergunta")

@app.post("/verificar-resposta")
async def verificar_resposta(dados: RespostaModel):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4.1-mini",
            messages=[{
                "role": "user",
                "content": f"Pergunta: {dados.pergunta}\nResposta do usuário: {dados.resposta}\n\nA resposta está correta? Responda apenas 'Verdadeiro' ou 'Falso' e depois explique em uma frase curta."
            }]
        )
        resultado = response.choices[0].message.content.strip()
        
        if "Verdadeiro" in resultado.split('\n')[0]:
            correto = True
        else:
            correto = False
            
        explicacao = resultado.split('\n', 1)[1] if '\n' in resultado else resultado
        
        return {
            "correto": correto,
            "explicacao": explicacao
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao verificar resposta")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)