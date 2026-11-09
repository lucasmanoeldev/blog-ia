# Agente Criador de Conteúdo para Blog (Blog-IA)

Um sistema inteligente para criação de artigos de blog otimizados para SEO, desenvolvido com **Streamlit**, **LangChain** e o modelo **Llama 3.3 70B** via API do **Groq**.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F05032?style=for-the-badge&logo=groq&logoColor=white)

---

## Funcionalidades

- **Geração Direta (Automática):** Informe um assunto e receba um artigo completo gerado em tempo real via streaming.
- **Geração Personalizada (Em Etapas):**
  1. **Ideação:** Geração de sugestões de títulos e subtemas pela IA.
  2. **Revisão:** Edição e personalização livre de títulos e seções pelo usuário.
  3. **Escrita:** Criação do artigo completo adaptado exatamente às suas escolhas.
- **Métricas do Conteúdo:** Cálculo de total de palavras, caracteres e estimativa de tempo de leitura.
- **Exportação:** Download fácil do artigo final no formato Markdown (`.md`).
- **UI Moderna:** Interface customizada e responsiva desenvolvida em Streamlit.

---

## Tecnologias Utilizadas

- **[Python 3.12+](https://www.python.org/)** — Linguagem base do projeto.
- **[Streamlit](https://streamlit.io/)** — Framework para a interface web interativa.
- **[LangChain](https://www.langchain.com/)** — Orquestração de prompts, cadeias e chamadas ao LLM.
- **[ChatGroq (Llama 3.3 70B Versatile)](https://groq.com/)** — Modelo de linguagem para geração rápida e de altíssima qualidade.
- **[Pydantic](https://docs.pydantic.dev/)** — Validação de estruturas de dados.
- **[python-dotenv](https://github.com/theskumar/python-dotenv)** — Gerenciamento de variáveis de ambiente.

---

## Pré-requisitos

- Python 3.12 ou superior instalado.
- Uma chave de API da **Groq** ([obtenha gratuitamente no GroqCloud](https://console.groq.com/)).

---

## Configuração e Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/lucasmanoeldev/blog-ia.git
cd blog-ia
```

### 2. Configurar o Ambiente Virtual e Instalar Dependências

Se você utiliza o **uv**:
```bash
uv sync
```

Ou via **pip** e ambiente virtual padrão:
```bash
python -m venv .venv
# No Windows:
.venv\Scripts\activate
# No Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Configurar as Variáveis de Ambiente

Copie `.env.example` para `.env` na raiz do projeto e preencha sua chave:

```env
GROQ_API_KEY=sua_chave_groq_aqui
```

---

## Como Executar a Aplicação

Para iniciar o servidor web do Streamlit:

```bash
uv run streamlit run frontend.py
```

Se instalou com pip, use `streamlit run frontend.py` com o ambiente virtual ativado.

No Streamlit Community Cloud, mantenha `frontend.py` como arquivo principal e configure `GROQ_API_KEY` nos secrets da aplicação.

A aplicação abrirá automaticamente no seu navegador padrão no endereço `http://localhost:8501`.

---
## Imagem
<img width="1910" height="944" alt="image" src="https://github.com/user-attachments/assets/dea6f79b-0a0d-48df-a8e3-a1be1915666b" />

## Estrutura do Projeto

```text
blog-ia/
├── app/
│   ├── __init__.py
│   ├── backend.py       # Prompts, cadeias LangChain e integração com a Groq
│   └── frontend.py      # Interface Streamlit
├── assets/
│   ├── favicon.png
│   └── logotipo.png
├── frontend.py          # Entrada da aplicação e compatibilidade com deploys
├── .env.example         # Exemplo de configuração local
├── .python-version
├── pyproject.toml       # Dependências compartilhadas
├── requirements.txt     # Instalação alternativa com pip
├── uv.lock              # Versões resolvidas pelo uv
└── README.md
```

O frontend chama as funções do backend no mesmo processo Python. Não é necessário iniciar um servidor de API separado. Execute os comandos a partir da raiz do repositório.


---

## Licença

O repositório ainda não contém um arquivo de licença.


## Outros projetos

Veja o [catálogo de projetos públicos](docs/PROJETOS.md), organizado por área.
