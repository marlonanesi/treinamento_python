# 🎯 Quiz Inteligente com FastAPI + Jinja2

Desenvolva uma aplicação web profissional de Quiz usando **FastAPI**, **Jinja2** e **OpenAI API** com interface moderna e responsiva.

## 📋 Estrutura do Projeto

```
quiz_gen_ai_2.0/
├── main.py              # Aplicação FastAPI
├── config.py            # Configurações e API Key
├── templates/
│   └── index.html       # Template Jinja2
└── static/
    └── style.css        # Estilos CSS
```

## 🚀 Especificações Técnicas

### **Backend (main.py)**
- **Framework**: FastAPI com Jinja2Templates
- **Rotas**:
  - `GET /` → Renderiza página inicial
  - `POST /gerar-pergunta` → Gera pergunta via OpenAI
  - `POST /verificar-resposta` → Valida resposta e retorna explicação
- **OpenAI Integration**: Modelo `gpt-4.1-mini` para perguntas de Python
- **CORS**: Habilitado para requisições AJAX

### **Frontend (index.html)**
- **Template Engine**: Jinja2
- **Design**: Interface moderna com gradientes e animações
- **Responsividade**: Mobile-first design
- **Interatividade**: AJAX para comunicação assíncrona
- **UX**: Loading states e feedback visual

### **Funcionalidades**
1. **Geração de Perguntas**: Verdadeiro/Falso sobre Python
2. **Validação Inteligente**: IA verifica resposta e explica
3. **Feedback Visual**: Cores e ícones para respostas corretas/incorretas
4. **Interface Responsiva**: Funciona em desktop e mobile

## 🎨 Identidade Visual

### **Paleta de Cores**
- **Primary**: `#667eea` (Azul moderno)
- **Secondary**: `#764ba2` (Roxo elegante)
- **Success**: `#10b981` (Verde sucesso)
- **Error**: `#ef4444` (Vermelho erro)
- **Background**: `#f8fafc` (Cinza claro)

### **Tipografia**
- **Font**: Inter (Google Fonts)
- **Títulos**: Bold, tamanhos hierárquicos
- **Texto**: Regular, boa legibilidade

### **Componentes**
- **Botões**: Gradientes com hover effects
- **Cards**: Sombras suaves e bordas arredondadas
- **Loading**: Spinner animado
- **Feedback**: Alertas coloridos com ícones

## 🔧 Implementação

### **Configuração (config.py)**
```python
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')
```

### **Rotas FastAPI**
- **Página inicial**: Renderiza template com Jinja2
- **API endpoints**: Retornam JSON para AJAX
- **Error handling**: Tratamento de erros da OpenAI

### **Template Jinja2**
- **Layout responsivo**: CSS Grid e Flexbox
- **JavaScript**: Fetch API para requisições
- **Estados visuais**: Loading, success, error
- **Animações**: Transições suaves

## 📱 Funcionalidades da Interface

### **Fluxo do Usuário**
1. **Página inicial** → Botão "Gerar Pergunta"
2. **Loading state** → Spinner durante geração
3. **Pergunta exibida** → Botões Verdadeiro/Falso
4. **Resposta enviada** → Loading durante validação
5. **Resultado mostrado** → Feedback colorido + explicação

### **Estados Visuais**
- **Idle**: Botão de gerar pergunta disponível
- **Loading**: Spinner e botões desabilitados
- **Question**: Pergunta exibida com botões de resposta
- **Result**: Feedback visual com explicação

### **Responsividade**
- **Desktop**: Layout em duas colunas
- **Tablet**: Layout adaptado
- **Mobile**: Stack vertical otimizado

## 🎯 Requisitos de Implementação

### **Backend Requirements**
- FastAPI com templates Jinja2
- OpenAI client configurado
- CORS middleware
- Error handling robusto
- Validação de dados

### **Frontend Requirements**
- HTML semântico e acessível
- CSS moderno com variáveis
- JavaScript vanilla (sem frameworks)
- Fetch API para requisições
- Loading states e feedback visual

### **Integração OpenAI**
- **Prompt para perguntas**: Gerar questões V/F sobre Python
- **Prompt para validação**: Verificar resposta e explicar
- **Error handling**: Fallback para falhas da API
- **Rate limiting**: Controle de requisições