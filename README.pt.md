# RAG com Python, LangChain e Bancos de Dados Vetoriais

Este projeto demonstra um pipeline de Retrieval-Augmented Generation (RAG) usando Python, LangChain e OpenAI. Ele pode carregar documentos PDF, criar embeddings vetoriais e armazená-los em um banco de dados vetorial como ChromaDB ou Pinecone para recuperação eficiente e resposta a perguntas. O projeto inclui notebooks Jupyter para desenvolvimento e uma aplicação Streamlit para uma interface de usuário interativa.

## Funcionalidades

-   **Carregamento de Documentos**: Carrega e processa texto de arquivos PDF locais.
-   **Divisão de Texto**: Divide documentos em pedaços menores e gerenciáveis, adequados para embedding.
-   **Embeddings Vetoriais**: Gera embeddings vetoriais usando os modelos da OpenAI.
-   **Armazenamento Vetorial**:
    -   [ChromaDB](https://www.trychroma.com/) para armazenamento vetorial local e persistente.
    -   [Pinecone](https://www.pinecone.io/) para um banco de dados vetorial escalável e baseado em nuvem.
-   **Interface Conversacional**: Faça perguntas sobre os documentos carregados através de uma aplicação web Streamlit.
-   **Estimativa de Custo**: Fornece um custo estimado para gerar os embeddings antes do processamento.

## Estrutura do Projeto

```
.
├── .env                  # Variáveis de ambiente (chaves de API)
├── main.ipynb            # Notebook Jupyter para o fluxo de trabalho com ChromaDB
├── pinecone.ipynb        # Notebook Jupyter para gerenciamento do Pinecone
├── streamlit_app.py      # A aplicação web Streamlit
├── requirements.txt      # Dependências Python
├── pdfs/                 # Diretório para seus documentos PDF
└── chroma_db/            # Armazenamento local para ChromaDB
```

## Configuração

Siga estes passos para configurar e executar o projeto localmente.

1.  **Clonar o Repositório**
    ```sh
    git clone <url-do-repositorio>
    cd <nome-do-repositorio>
    ```

2.  **Criar e Ativar um Ambiente Virtual**
    ```sh
    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instalar Dependências**
    Instale os pacotes necessários a partir do arquivo `requirements.txt`.
    ```sh
    pip install -r requirements.txt
    ```

4.  **Variáveis de Ambiente**
    Crie um arquivo `.env` no diretório raiz e adicione suas chaves de API. Este arquivo é ignorado pelo Git.
    ```
    # .env
    OPENAI_API_KEY="sua_chave_de_api_openai"
    PINECONE_API_KEY="sua_chave_de_api_pinecone"
    ```

5.  **Adicionar Documentos**
    Coloque os arquivos PDF que você deseja processar dentro do diretório `pdfs/`.

## Uso

Você pode interagir com este projeto usando os notebooks Jupyter ou a aplicação web Streamlit.

### 1. Notebooks Jupyter

-   **[main.ipynb](main.ipynb)**: Use este notebook para percorrer o processo de carregamento de documentos, dividi-los em pedaços e armazenar os embeddings em uma instância local do ChromaDB.
-   **[pinecone.ipynb](pinecone.ipynb)**: Este notebook demonstra como criar, gerenciar e consultar um índice Pinecone para seus embeddings vetoriais.

### 2. Aplicação Streamlit

Para uma experiência interativa, execute a aplicação Streamlit. Isso permite que você carregue um documento e faça perguntas sobre o conteúdo dele.

1.  Inicie a aplicação a partir do seu terminal:
    ```sh
    streamlit run streamlit_app.py
    ```
2.  Abra seu navegador na URL local fornecida pelo Streamlit.
3.  Carregue um documento PDF e comece a fazer perguntas.