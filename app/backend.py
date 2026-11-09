

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")
chat = ChatGroq(
    model="llama-3.3-70b-versatile"
)

class Titulo(BaseModel):
    titulo: list[str] = Field(description="lista de titulos")

class Temas(BaseModel):
    temas: list[str] = Field(description="listas de temas")

prompt_titulos = ChatPromptTemplate.from_messages(
    [
        ("system","""
        Você é um especialista em criação de títulos para blogs e SEO.

        Sua única função é gerar títulos criativos, claros e atrativos com base no tema informado pelo usuário.

        Regras:
        - Não repita títulos.
        - Use linguagem natural.
        - Crie títulos que despertem interesse sem usar clickbait exagerado.
        - Priorize a palavra-chave principal.
        - Escreva em português do Brasil.
        - Não faça explicações ou comentários.

        Retorne apenas uma lista com os títulos."""),
        ("human","Listes 5 titulos sobre: {temas}")
    ]
)

prompt_temas = ChatPromptTemplate.from_messages(
    [
        ("system","""
        Você é um especialista em criação de temas para blogs e SEO.

        Sua única função é gerar temas criativos, claros e atrativos com base no tema informado pelo usuário.

        Regras:
        - Não repita temas.
        - Use linguagem natural.
        - Crie temas que despertem interesse sem usar clickbait exagerado.
        - Priorize a palavra-chave principal.
        - Escreva em português do Brasil.
        - Não faça explicações ou comentários.

        Retorne apenas uma lista com os temas."""),
        ("human","Listes 5 temas sobre: {temas}")
    ]
)

prompt_blog = ChatPromptTemplate.from_messages(
     [
        (
            "system",
            """
            Você é um especialista em artigo, redação técnica e SEO.

            Sua única função é escrever um artigo completo em Markdown.

            Regras:
            - Escolha apenas 1 dos títulos fornecidos pelo usuário.
            - Utilize todos os temas fornecidos como seções do artigo.
            - Crie um conteúdo detalhado, claro e bem organizado.
            - Explique os conceitos de forma simples.
            - Sempre que necessário, adicione exemplos de código.
            - Utilize títulos e subtítulos (H1, H2 e H3).
            - Inclua listas quando fizer sentido.
            - Finalize com uma conclusão.
            - Não invente informações.
            - Não escreva comentários fora do artigo.
            - Retorne apenas o artigo em Markdown.
            """
        ),
        (
            "human",
             """
            Títulos disponíveis:
            {titulos}

            Temas:
            {temas}
            """
        )
    ]
)

runnable = RunnableParallel({
    "titulos": prompt_titulos | chat | StrOutputParser(),
    "temas": prompt_temas | chat | StrOutputParser()
})

chain = runnable | prompt_blog | chat | StrOutputParser()
chain_blog_direct = prompt_blog | chat | StrOutputParser()


def gerar_titulos_e_temas(assunto: str) -> dict:
    return runnable.invoke({"temas": assunto})


def gerar_artigo(assunto: str) -> str:
    return chain.invoke({"temas": assunto})


def gerar_artigo_stream(assunto: str):
    return chain.stream({"temas": assunto})


def gerar_artigo_customizado_stream(titulos: str, temas: str):
    return chain_blog_direct.stream({"titulos": titulos, "temas": temas})


if __name__ == "__main__":
    print(gerar_artigo("langchain"))
