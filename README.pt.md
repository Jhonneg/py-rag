# RAG com Python, LangChain e Pinecone

Este projeto demonstra um pipeline de Retrieval Augmented Generation (RAG) usando Python. Ele carrega documentos de várias fontes, os divide em chunks` e os prepara para a vetorização (embedding) e armazenamento em um banco de dados vetorial Pinecone.

O projeto está estruturado em dois notebooks Jupyter principais:
-   [main.ipynb](main.ipynb): Responsável pelo carregamento de documentos (PDFs, DOCX, Wikipedia), divisão do texto em chunks e cálculo do custo de embedding.
-   [pinecone.ipynb](pinecone.ipynb): Gerencia a interação com o banco de dados vetorial Pinecone.

## Funcionalidades

-   Carrega documentos de arquivos PDF e DOCX locais.
-   Busca e carrega dados diretamente da Wikipedia.
-   Divide documentos em chunks (pedaços) gerenciáveis para processamento.
-   Calcula o custo estimado para criar embeddings usando os modelos da OpenAI.
-   Integra-se com o Pinecone para armazenamento e recuperação de vetores.

## Configuração

1.  **Clonar o repositório**
    ```sh
    git clone <url-do-repositorio>
    cd <nome-do-repositorio>
    ```

2.  **Criar e ativar um ambiente virtual**
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3.  **Instalar dependências**
    Os pacotes necessários são instalados diretamente a partir dos notebooks. Execute as células com `pip install` em [main.ipynb](main.ipynb) e [pinecone.ipynb](pinecone.ipynb).

4.  **Variáveis de Ambiente**
    Crie um arquivo `.env` na raiz do projeto e adicione suas chaves de API. Este arquivo é ignorado pelo Git.
    ```
    # .env
    PINECONE_API_KEY="sua_chave_api_do_pinecone"
    OPENAI_API_KEY="sua_chave_api_da_openai" # Necessário para os embeddings
    ```

5.  **Adicionar Documentos**
    Coloque seus arquivos PDF ou DOCX no diretório `pdfs/`.

## Uso

1.  **Processar Documentos**: Abra e execute as células no [main.ipynb](main.ipynb) para carregar e dividir seus documentos. Você pode ver o número de chunks criados e o custo estimado do embedding.

2.  **Gerenciar Banco de Dados Vetorial**: Abra e execute as células no [pinecone.ipynb](pinecone.ipynb) para configurar seu índice no Pinecone e (em um passo futuro) carregar os vetores dos documentos.