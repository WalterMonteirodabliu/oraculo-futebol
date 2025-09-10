# Oráculo do Futebol

Um chatbot inteligente e especialista em futebol, construído com Agentes de IA, que responde a perguntas complexas buscando informações em tempo real na internet.

[Demonstração do Chatbot]([//s.imgur.com/min/embed.js](https://imgur.com/gallery/py-Wdw0pEE)) 

## Sobre o Projeto

O Oráculo do Futebol é um agente de IA que utiliza o poder de modelos de linguagem de ponta (como Llama 3 ou Mixtral) conectados a ferramentas de busca na web. Ele é capaz de entender perguntas em linguagem natural, pesquisar dados atuais sobre jogos, estatísticas de jogadores, notícias de times e muito mais, para então sintetizar uma resposta completa e coesa.

Este projeto foi criado como um estudo sobre a arquitetura de Agentes de IA com a biblioteca LangChain, contornando a necessidade de APIs de futebol pagas e complexas.

## Funcionalidades

* **Respostas em Tempo Real:** Busca na web para responder sobre eventos recentes.
* **Análise Comparativa:** Compara estatísticas entre jogadores e times.
* **Probabilidades e Previsões:** Sintetiza informações de especialistas para avaliar as chances em jogos futuros.
* **Histórico e Dados:** Responde perguntas sobre campeonatos, resultados passados, etc.
* **Arquitetura Segura:** Mantém as chaves de API seguras usando variáveis de ambiente.

## Tecnologias Utilizadas

* **Python 3.9+**
* **LangChain**: Framework principal para a construção do agente de IA.
* **Groq API**: Fornece acesso a modelos de linguagem de alta velocidade (Llama 3, Mixtral).
* **Tavily Search API**: Ferramenta de busca na web otimizada para Agentes de IA.

## Como Rodar o Projeto

Siga os passos abaixo para configurar e rodar o projeto em sua máquina local.

### Pré-requisitos

* Python 3.9 ou superior
* Uma chave de API da [Groq](https://console.groq.com/keys)
* Uma chave de API da [Tavily AI](https://app.tavily.com/home)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/oraculo-futebol.git](https://github.com/seu-usuario/oraculo-futebol.git)
    cd oraculo-futebol
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Crie um arquivo `requirements.txt`:**
    Este arquivo lista todas as dependências do projeto. Se você ainda não o criou, rode o comando abaixo no seu terminal (com o `venv` ativado) para gerar o arquivo automaticamente:
    ```bash
    pip freeze > requirements.txt
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure as variáveis de ambiente:**
    Crie um arquivo chamado `.env` na raiz do projeto e adicione suas chaves de API, como no exemplo abaixo:
    ```env
    GROQ_API_KEY="COLE_SUA_CHAVE_DA_GROQ_AQUI"
    TAVILY_API_KEY="COLE_SUA_CHAVE_DA_TAVILY_AQUI"
    ```

### Execução

Com tudo configurado, basta rodar o script principal:
```bash
python chatbot_futebol.py
