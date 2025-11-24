# RAG com Python, LangChain e Bancos de Dados Vetoriais

Este projeto demonstra um pipeline de Retrieval Augmented Generantion (RAG) usando Python e LangChain. Ele carrega documentos de várias fontes, divide-os em partes gerenciáveis (chunks), cria embeddings vetoriais e os armazena em um banco de dados vetorial como Pinecone ou ChromaDB para recuperação eficiente.

O projeto está estruturado em dois notebooks Jupyter principais:

-   [main.ipynb](main.ipynb): Lida com o carregamento de documentos (PDFs, DOCX, Wikipedia), divisão do texto, cálculo de custo de embedding e interação com um banco de dados vetorial ChromaDB.
-   [pinecone.ipynb](pinecone.ipynb): Gerencia todas as interações com o banco de dados vetorial Pinecone, incluindo criação de índices, inserção de vetores, consultas e exclusão.

## Funcionalidades

-   **Carregamento de Documentos**: Carrega documentos de arquivos PDF locais.
-   **Divisão de Texto**: Divide documentos em pedaços menores, adequados para embedding.
-   **Embeddings Vetoriais**: Cria representações vetoriais de trechos de texto usando os modelos da OpenAI.
-   **Estimativa de Custo**: Calcula o custo estimado para gerar os embeddings.
-   **Armazenamento Vetorial**: Integra-se tanto com o [ChromaDB](https://www.trychroma.com/) quanto com o [Pinecone](https://www.pinecone.io/) para armazenamento e recuperação de vetores.

## Configuração

1.  **Clone o Repositório**
    ```sh
    git clone <url-do-repositorio>
    cd <nome-do-repositorio>
    ```

2.  **Crie e Ative um Ambiente Virtual**
    ```sh
    python -m venv venv
    source venv/bin/activate 
    ```

3.  **Instale as Dependências**
    Instale os pacotes necessários executando as células de `pip install` dentro dos notebooks [main.ipynb](main.ipynb) e [pinecone.ipynb](pinecone.ipynb), ou instale-os a partir do arquivo `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```

4.  **Variáveis de Ambiente**
    Crie um arquivo `.env` na raiz do projeto e adicione suas chaves de API. Este arquivo está incluído no `.gitignore` e não será enviado para o repositório.
    ```
    # .env
    PINECONE_API_KEY="sua_chave_de_api_do_pinecone"
    OPENAI_API_KEY="sua_chave_de_api_da_openai"
    ```

5.  **Adicione os Documentos**
    Coloque seus arquivos PDF dentro do diretório `pdfs/`.

## Uso

1.  **Processar Documentos e Usar o ChromaDB**:
    Abra e execute as células no [main.ipynb](main.ipynb) para carregar os documentos, dividi-los em pedaços e armazenar os embeddings em um banco de dados local do ChromaDB.


2.  **Gerenciar Banco de Dados Vetorial**: Abra e execute as células no [pinecone.ipynb](pinecone.ipynb) para configurar seu índice no Pinecone e (em um passo futuro) carregar os vetores dos documentos.
 
## Demo 
<div align=center >
    

**Pergunda e resposta**

<img width="1632" height="403" alt="screenshot-2025-11-24_08-39-35" src="https://github.com/user-attachments/assets/6c97cd02-cedd-4604-ac70-8fae90d66b8b" />

**Historico do chat**

<img width="1829" height="279" alt="screenshot-2025-11-24_08-43-51" src="https://github.com/user-attachments/assets/b0a56913-6b3b-4f4a-829f-417c8eafce6e" />
</div>


