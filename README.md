# ✍️ Agente Criador de Conteúdo para Blog (Blog-IA)

Um sistema inteligente para criação de artigos de blog otimizados para SEO, desenvolvido com **Streamlit**, **LangChain** e o modelo **Llama 3.3 70B** via API do **Groq**.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F05032?style=for-the-badge&logo=groq&logoColor=white)

---

## 🚀 Funcionalidades

- **⚡ Geração Direta (Automática):** Informe um assunto e receba um artigo completo gerado em tempo real via streaming.
- **🛠️ Geração Personalizada (Em Etapas):**
  1. **Ideação:** Geração de sugestões de títulos e subtemas pela IA.
  2. **Revisão:** Edição e personalização livre de títulos e seções pelo usuário.
  3. **Escrita:** Criação do artigo completo adaptado exatamente às suas escolhas.
- **📊 Métricas do Conteúdo:** Cálculo de total de palavras, caracteres e estimativa de tempo de leitura.
- **📥 Exportação:** Download fácil do artigo final no formato Markdown (`.md`).
- **🎨 UI Moderna:** Interface customizada e responsiva desenvolvida em Streamlit.

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3.12+](https://www.python.org/)** — Linguagem base do projeto.
- **[Streamlit](https://streamlit.io/)** — Framework para a interface web interativa.
- **[LangChain](https://www.langchain.com/)** — Orquestração de prompts, cadeias e chamadas ao LLM.
- **[ChatGroq (Llama 3.3 70B Versatile)](https://groq.com/)** — Modelo de linguagem para geração rápida e de altíssima qualidade.
- **[Pydantic](https://docs.pydantic.dev/)** — Validação de estruturas de dados.
- **[python-dotenv](https://github.com/theskumar/python-dotenv)** — Gerenciamento de variáveis de ambiente.

---

## 📋 Pré-requisitos

- Python 3.12 ou superior instalado.
- Uma chave de API da **Groq** ([obtenha gratuitamente no GroqCloud](https://console.groq.com/)).

---

## 🔧 Configuração e Instalação

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

Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:

```env
GROQ_API_KEY=sua_chave_groq_aqui
```

---

## 💻 Como Executar a Aplicação

Para iniciar o servidor web do Streamlit:

```bash
streamlit run frontend.py
```

A aplicação abrirá automaticamente no seu navegador padrão no endereço `http://localhost:8501`.

---

## 📂 Estrutura do Projeto

```
blog-ia/
├── backend.py        # Lógica do LangChain, prompts e integração com o ChatGroq
├── frontend.py       # Interface de usuário desenvolvida em Streamlit
├── main.py           # Script de entrada secundário
├── imagem/           # Assets visuais (favicon, logotipo)
├── .env.example      # Modelo de variáveis de ambiente
├── pyproject.toml    # Configuração do projeto e dependências
└── README.md         # Documentação do projeto
```

---

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE).
