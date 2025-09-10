import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

# Importações principais do LangChain
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# --- 1. CONFIGURAÇÃO INICIAL ---

load_dotenv()


if not os.getenv("GROQ_API_KEY") or not os.getenv("TAVILY_API_KEY"):
    print("ERRO: Chaves de API não encontradas. Verifique se o arquivo .env existe e está correto.")
    exit()

# --- 2. DEFINIÇÃO DAS FERRAMENTAS ---
search_tool = TavilySearch(max_results=5)
tools = [search_tool]

# --- 3. DEFINIÇÃO DO CÉREBRO (LLM) ---
# Usando o modelo Llama 3.3 que se provou estável
llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0)

# --- 4. CRIAÇÃO DO PROMPT ---
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
        Você é um assistente especialista em futebol de altíssimo nível.
        Sua função é responder perguntas sobre futebol usando dados atualizados da internet.
        Seja direto, informativo e use as informações que encontrar para formular suas respostas.
        Ao dar probabilidades ou estatísticas, sempre mencione que são baseadas nos dados mais recentes que você encontrou na web.
        Você tem acesso a uma ferramenta de busca chamada 'tavily_search_results_json'.
        Use-a sempre que precisar de informações atuais sobre jogos, jogadores, times, notícias ou estatísticas.
        Responda sempre em português do Brasil.
        """),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# --- 5. CRIAÇÃO DO AGENTE ---
agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- 6. LOOP DE INTERAÇÃO COM O USUÁRIO ---
print("--- Chatbot de Futebol IA (usando Groq e Mixtral) ---")
print("Olá! Faça sua pergunta sobre futebol. (Digite 'sair' para encerrar)")

while True:
    user_input = input("\nVocê: ")
    if user_input.lower() == 'sair':
        print("Até a próxima!")
        break
    
    response = agent_executor.invoke({"input": user_input})
    
    print(f"\nIA: {response['output']}")