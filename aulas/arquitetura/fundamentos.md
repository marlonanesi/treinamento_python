# 🏗️ Aula: Fundamentos de Arquitetura de Software

## 📌 Introdução

A arquitetura de software é a base estrutural que define **como um sistema será organizado, escalado, mantido e evoluído**. Mais do que escolher tecnologias, arquitetar um sistema é tomar decisões estratégicas sobre **acoplamento, responsabilidade, modularidade, comunicação e resiliência**.

Nesta aula, veremos os fundamentos essenciais, práticas recomendadas e erros comuns, além de destacar a importância do rito de **Solution Review**, uma etapa crítica no ciclo de vida de uma solução.

---

## 🧱 Fundamentos da Arquitetura

### 1. **Modularização e Reutilização**
- Dividir o sistema em **módulos coesos e independentes** facilita manutenção, testes e evolução.
- Módulos reutilizáveis reduzem retrabalho e aceleram novos projetos.

### 2. **Desacoplamento**
- O **baixo acoplamento** entre módulos permite evoluir partes do sistema sem afetar outras.
- Favorece **resiliência, escalabilidade e testabilidade**.
- Ferramentas como eventos, filas e interfaces bem definidas ajudam nesse processo.

### 3. **Separação de responsabilidades**
- Cada módulo ou serviço deve ter uma responsabilidade bem definida.
- Seguir princípios como **SRP (Single Responsibility Principle)** evita "monólitos dentro do micro".

### 4. **Documentação e Visibilidade**
- Diagramas, DSLs ou DSLs visuais (ex: C4 Model, Mermaid.js) ajudam todos os perfis a entender a estrutura.
- A arquitetura não deve morar apenas na cabeça de uma pessoa.

---

## ⚠️ Erros comuns no início de projetos

- Ignorar **requisitos não-funcionais** (ex: escalabilidade, observabilidade, segurança)
- Acoplar demais o sistema a um banco de dados específico ou a um framework
- Tentar resolver todos os problemas com uma única arquitetura (ex: tudo em microserviços)
- Superestimar o time e escolher tecnologias complexas demais
- Criar sistemas sem mecanismos claros de **observabilidade (logs, métricas, tracing)**

---

## 🧠 Perguntas importantes para discutir desde o início

1. Quais são os **requisitos não funcionais** mais críticos?
2. O sistema precisa ser **escalável horizontalmente**?
3. Existem **limitações de domínio, latência ou volume**?
4. Como será feito o **controle de acesso e segurança**?
5. O que deve ser **desacoplado desde o começo**?
6. Quais pontos já podem ser **externalizados ou plugáveis**?
7. Como os módulos se comunicarão? (**sincronia x assincronia**)
8. Qual será a estratégia de **deploy e rollback**?

---

## 🧩 Rito: Solution Review

O **Solution Review** é um momento estruturado onde a solução é apresentada para revisão crítica por diferentes perfis:

- Arquitetos
- Líderes técnicos
- Devs seniores
- Pessoas de segurança, infraestrutura, dados e produto

### Objetivos do rito:
- Validar a coerência da arquitetura com os requisitos do negócio
- Antecipar riscos técnicos e operacionais
- Identificar pontos de acoplamento desnecessários
- Enxergar oportunidades de simplificação e reutilização
- Trazer alinhamento multidisciplinar sobre a visão da solução

### Como conduzir:
- Apresentar a **visão geral**, pontos técnicos críticos e decisões já tomadas
- Mostrar **diagrama de componentes e fluxos principais**
- Conduzir o review com base em **perguntas provocativas**, não apenas validações
- Documentar os pontos levantados e definir **ações ou validações futuras**

---

## ✅ Conclusão

"Uma boa arquitetura não é a mais bonita no papel, mas a que **melhor resolve os problemas certos com o menor custo de mudança possível**. Comece simples, desacople o que for possível desde o início, e mantenha um canal aberto para evolução contínua."
Marlon Brehmer Anesi

**Arquitetar é alinhar tecnologia com estratégia e resultados.**

