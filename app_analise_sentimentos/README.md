## 🎬 **Versão Inicial do Curso: A Evolução Natural do Desenvolvimento**
Essa parte do curso foi a primeira que desenvolvi e surgiu de forma **100% natural, sem um roteiro fixo**. Eu sabia o que queria fazer e fui implementando de maneira dinâmica, corrigindo erros no processo e seguindo em frente. Essa abordagem reflete a realidade do desenvolvimento de software, onde nem sempre tudo funciona de primeira.

Quis trazer essa experiência para você, aluno, pois já estive nessa posição. Apenas seguir um roteiro onde tudo dá certo na primeira tentativa pode ser frustrante e pouco realista. Aqui, você verá **tentativas, erros e correções**, assim como acontece no dia a dia de um desenvolvedor.

Desenvolvemos um **aplicativo básico**, composto por **backend e frontend**, que recebe comentários e avaliações e os envia para uma API do ChatCompletion, que avalia o sentimento e decide se o comentário deve ser aprovado ou não. Conforme avançamos, a aplicação evolui:

✅ Passamos a **armazenar os dados em um banco NoSQL (MongoDB)**.  
✅ Adicionamos **uma arquitetura de eventos utilizando o Kafka**.  
➡️ Poderíamos usar outra fila, mas escolhi o Kafka por ser mais desafiador. **Se você dominar o básico do Kafka, será capaz de trabalhar com qualquer outra tecnologia de mensageria.**

No final, temos uma **aplicação com 6 containers**:

1️⃣ Backend Python  
2️⃣ Frontend com Streamlit  
3️⃣ Banco de dados MongoDB  
4️⃣ Kafka  
5️⃣ Zookeeper  
6️⃣ Kowl (ferramenta de visualização do Kafka)  

Essa stack pode ser **facilmente iniciada em qualquer ambiente com suporte ao Docker** e está **pronta para ser migrada para a cloud**, podendo ser adaptada para Kubernetes ou outro orquestrador de containers.

---

## 🔥 **Projeto Dividido em Fases**
1️⃣ **Criação do aplicativo**: Backend em Python e frontend com Streamlit.  
2️⃣ **Containerização**: Empacotamos a aplicação para rodar via Docker.  
3️⃣ **Banco de dados**: Integramos o MongoDB para armazenar os dados.  
4️⃣ **Arquitetura orientada a eventos**: Introduzimos o Kafka para comunicação assíncrona.  

Esse curso foi projetado para **ser dinâmico e prático**, simulando situações reais e permitindo que você aprenda **não apenas conceitos, mas como resolver problemas na prática**. 🚀

