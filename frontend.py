import os
from PIL import Image
import streamlit as st
import backend

FAVICON_PATH = os.path.join("imagem", "farvicon.png")
LOGOTIPO_PATH = os.path.join("imagem", "logotipo.png")

page_icon = FAVICON_PATH if os.path.exists(FAVICON_PATH) else "✍️"

st.set_page_config(
    page_title="Gerador de Artigos com IA",
    page_icon=page_icon,
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }
    
    .header-container {
        background: linear-gradient(135deg, #1e1e2f 0%, #2d2b55 100%);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        color: #ffffff;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .header-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        background: linear-gradient(90deg, #60a5fa, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .header-subtitle {
        font-size: 1.1rem;
        color: #cbd5e1;
    }

    .metric-card {
        background-color: #1e293b;
        border-radius: 12px;
        padding: 1rem 1.5rem;
        text-align: center;
        border: 1px solid #334155;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: bold;
        color: #38bdf8;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="header-container">
        <div class="header-title">Agente Criador de Conteúdo para Blog</div>
        <div class="header-subtitle">
            Crie artigos completos, otimizados para SEO e com exemplos práticos usando a potência do Llama 3.3 e LangChain.
        </div>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    if os.path.exists(LOGOTIPO_PATH):
        st.image(LOGOTIPO_PATH, width=150)
    st.title("Configurações")
    
    modo_geracao = st.radio(
        "Modo de Geração:",
        ["Geração Direta (Automática)", "Geração Personalizada (Em Etapas)"],
        help="Escolha entre gerar tudo com um clique ou personalizar títulos e temas antes da escrita."
    )
    
    st.divider()
    
    st.markdown("### Sugestões de Temas")
    sugestoes = [
        "LangChain e Agentes IA",
        "Python 3.12 e Novidades",
        "Boas Práticas de Clean Code",
        "Engenharia de Prompt para Devs",
        "Arquitetura Microserviços com FastAPI"
    ]
    
    tema_selecionado_sidebar = None
    for item in sugestoes:
        if st.button(f"📌 {item}", use_container_width=True):
            st.session_state["tema_input"] = item

    st.divider()
    st.caption("")

if "tema_input" not in st.session_state:
    st.session_state["tema_input"] = ""

if "titulos_gerados" not in st.session_state:
    st.session_state["titulos_gerados"] = ""

if "temas_gerados" not in st.session_state:
    st.session_state["temas_gerados"] = ""

if "artigo_final" not in st.session_state:
    st.session_state["artigo_final"] = ""


if modo_geracao == "Geração Direta (Automática)":
    st.subheader("Gerar Artigo Completo")
    
    tema_usuario = st.text_input(
        "Sobre qual assunto você deseja que o artigo seja escrito?",
        value=st.session_state["tema_input"],
        placeholder="Ex: Como construir um sistema de RAG com LangChain",
        key="input_direto"
    )
    
    col_btn, _ = st.columns([1, 3])
    with col_btn:
        btn_gerar = st.button(" Criar Artigo Agora", type="primary", use_container_width=True)

    if btn_gerar:
        if not tema_usuario.strip():
            st.warning("⚠️ Por favor, informe um assunto para o artigo.")
        else:
            with st.spinner("Analisando o tema, criando títulos, planejando seções e redigindo o artigo..."):
                try:
                    container_resposta = st.empty()
                    texto_acumulado = ""
                    
                    stream = backend.gerar_artigo_stream(tema_usuario)
                    for chunk in stream:
                        texto_acumulado += chunk
                        container_resposta.markdown(texto_acumulado + "▌")
                    
                    container_resposta.markdown(texto_acumulado)
                    st.session_state["artigo_final"] = texto_acumulado
                    st.success("🎉 Artigo gerado com sucesso!")
                except Exception as e:
                    st.error(f"❌ Ocorreu um erro ao gerar o artigo: {str(e)}")


else:
    st.subheader(" Geração Personalizada em Etapas")
    st.write("Ideal para quem prefere analisar e ajustar as sugestões de títulos e subtemas antes de gerar o artigo.")
    
    st.markdown("#### 1️⃣ Passo 1: Definir Assunto e Gerar Ideias")
    
    col_input, col_btn_ideias = st.columns([3, 1])
    with col_input:
        tema_usuario = st.text_input(
            "Assunto principal:",
            value=st.session_state["tema_input"],
            placeholder="Ex: Inteligência Artificial na Educação",
            key="input_etapas",
            label_visibility="collapsed"
        )
    with col_btn_ideias:
        btn_ideias = st.button("Gerar Títulos e Temas", use_container_width=True)

    if btn_ideias:
        if not tema_usuario.strip():
            st.warning("⚠️ Por favor, informe um assunto.")
        else:
            with st.spinner("🔎 Gerando opções de títulos e lista de temas..."):
                try:
                    resultado = backend.gerar_titulos_e_temas(tema_usuario)
                    st.session_state["titulos_gerados"] = resultado.get("titulos", "")
                    st.session_state["temas_gerados"] = resultado.get("temas", "")
                    st.success("✅ Ideias geradas! Ajuste os campos abaixo se desejar.")
                except Exception as e:
                    st.error(f"❌ Erro ao gerar ideias: {str(e)}")

    st.divider()

    st.markdown("#### 2️⃣ Passo 2: Revisar Títulos e Subtemas")
    
    col_titulos, col_temas = st.columns(2)
    with col_titulos:
        titulos_editados = st.text_area(
            "Títulos Sugeridos (a IA escolherá o melhor):",
            value=st.session_state["titulos_gerados"],
            height=200,
            help="Você pode editar ou adicionar seus próprios títulos."
        )
    with col_temas:
        temas_editados = st.text_area(
            "Subtemas/Seções do Artigo:",
            value=st.session_state["temas_gerados"],
            height=200,
            help="Esses tópicos serão transformados nas seções do seu artigo."
        )

    st.divider()

    st.markdown("#### 3️⃣ Passo 3: Escrever o Artigo Final")
    btn_gerar_custom = st.button("Escrever Artigo Customizado", type="primary", use_container_width=True)

    if btn_gerar_custom:
        if not titulos_editados.strip() or not temas_editados.strip():
            st.warning("⚠️ Forneça os títulos e temas no Passo 2 antes de gerar.")
        else:
            with st.spinner("Escrevendo o artigo baseado nas suas preferências..."):
                try:
                    container_resposta = st.empty()
                    texto_acumulado = ""
                    
                    stream = backend.gerar_artigo_customizado_stream(titulos_editados, temas_editados)
                    for chunk in stream:
                        texto_acumulado += chunk
                        container_resposta.markdown(texto_acumulado + "▌")
                    
                    container_resposta.markdown(texto_acumulado)
                    st.session_state["artigo_final"] = texto_acumulado
                    st.success("🎉 Artigo customizado gerado com sucesso!")
                except Exception as e:
                    st.error(f"❌ Erro ao gerar o artigo: {str(e)}")


if st.session_state["artigo_final"]:
    st.divider()
    st.subheader("Métricas e Exportação do Conteúdo")
    
    artigo_txt = st.session_state["artigo_final"]
    palavras = len(artigo_txt.split())
    caracteres = len(artigo_txt)
    tempo_leitura = max(1, round(palavras / 200))
    
    col_m1, col_m2, col_m3, col_down = st.columns([1, 1, 1, 2])
    
    with col_m1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{palavras}</div>
                <div class="metric-label">Palavras</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_m2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{caracteres}</div>
                <div class="metric-label">Caracteres</div>
            </div>
        """, unsafe_allow_html=True)

    with col_m3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">~{tempo_leitura} min</div>
                <div class="metric-label">Leitura</div>
            </div>
        """, unsafe_allow_html=True)

    with col_down:
        st.write("💾 **Baixar o artigo gerado:**")
        st.download_button(
            label="📥 Baixar como Markdown (.md)",
            data=artigo_txt,
            file_name="artigo_blog.md",
            mime="text/markdown",
            use_container_width=True
        )
