import streamlit as st
from PIL import Image
import os

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
# Deve ser a primeira chamada do Streamlit
st.set_page_config(
    page_title="Sacrominis | Estatuária de Legado",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed" # Começa fechado para focar na arte
)

# --- 2. ESTILIZAÇÃO VISUAL (CSS CUSTOMIZADO) ---
# Aqui garantimos que o app Streamlit tenha a cara do ateliê Sacrominis (Espartano, Solene, Dourado)
custom_css = """
<style>
    /* Fundo escuro e fonte serifada para dar tom solene */
    .stApp {
        background-color: #0b0c10;
        color: #FFFFF0;
        font-family: 'Georgia', serif;
    }
    
    /* Títulos em Dourado (#DAA520) */
    h1, h2, h3 {
        color: #DAA520 !important;
        text-align: center;
        font-weight: normal;
        letter-spacing: 2px;
    }
    
    /* Linha divisória customizada */
    hr {
        border-color: #DAA520;
        opacity: 0.3;
    }
    
    /* Box do Manifesto (Bordas douradas como solicitado nos seus projetos anteriores) */
    .manifesto-box {
        border: 1px solid #DAA520;
        padding: 30px;
        border-radius: 5px;
        background-color: rgba(218, 165, 32, 0.05);
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Ajuste de imagens para parecerem quadros */
    [data-testid="stImage"] img {
        border: 2px solid #DAA520;
        border-radius: 3px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.5);
    }
    
    /* Texto centralizado para citações */
    .quote-text {
        font-style: italic;
        color: #c0c0c0;
        text-align: center;
        font-size: 1.2rem;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- 3. FUNÇÕES AUXILIARES ---
def carregar_imagem(nome_arquivo):
    """Tenta carregar a imagem, retorna None se não encontrar para evitar que o app quebre."""
    try:
        if os.path.exists(nome_arquivo):
            return Image.open(nome_arquivo)
        return None
    except Exception as e:
        return None

# --- 4. ESTRUTURA DO APLICATIVO ---

# CABEÇALHO / HERO SECTION
logo_img = carregar_imagem("logo_completa.PNG")
if logo_img:
    # Cria três colunas para centralizar a logo (a do meio é mais larga)
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])
    with col_centro:
        st.image(logo_img, use_container_width=True)
else:
    # Fallback: Se a logo não for encontrada, exibe o texto
    st.markdown("<h1>SACROMINIS</h1>", unsafe_allow_html=True)

st.markdown("<p class='quote-text'>ESTATUÁRIA DE LEGADO TÁTICO E SACRO</p>", unsafe_allow_html=True)
st.markdown("<p class='quote-text'>\"Onde a Inteligência Arquiteta o Legado e a Mão Forja a Honra\"</p>", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# SEÇÃO 1: O NÚCLEO INEGOCIÁVEL (MANIFESTO)
col_vazia1, col_manifesto, col_vazia2 = st.columns([1, 4, 1])
with col_manifesto:
    st.markdown("""
    <div class="manifesto-box">
        <h3 style='margin-top:0;'>A Crença Central</h3>
        <p>A verdadeira honra e devoção não podem ser produzidas em massa; elas exigem o sacrifício do tempo e a união do rigor intelectual com a maestria manual para forjar um legado físico.</p>
        <br>
        <p><b>O Inimigo Combatido:</b> A banalização do legado — a cultura das "lembrancinhas" feitas às pressas, a produção em massa sem alma.</p>
        <p><b>A Promessa:</b> Transformar resina bruta em relicários e tributos que ancoram a fé e a honra.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# SEÇÃO 2: O ACERVO (PORTFÓLIO VISUAL)
st.markdown("<h2>O ACERVO</h2>", unsafe_allow_html=True)

# Abas para separar os nichos
tab_sacro, tab_tatico = st.tabs(["✝️ Santos Católicos", "⚔️ Corporações Policiais"])

with tab_sacro:
    st.markdown("<p class='quote-text'>Representam fé, reverência, sacrifício e proteção.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    img1 = carregar_imagem("IMG_4664.JPEG")
    if img1:
        with col1:
            st.image(img1, use_container_width=True, caption="Arte Sacra - Devoção em Resina")
    else:
        col1.info("Imagem IMG_4664.JPEG não encontrada no diretório.")

    img2 = carregar_imagem("IMG_4665.PNG")
    if img2:
        with col2:
            st.image(img2, use_container_width=True, caption="Detalhes e Acabamento Manual")
    else:
        col2.info("Imagem IMG_4665.PNG não encontrada no diretório.")

with tab_tatico:
    st.markdown("<p class='quote-text'>Representam honra, dever, legado e proteção.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_tat_1, col_tat_2, col_tat_3 = st.columns(3)
    
    img3 = carregar_imagem("IMG_4672 2.jpg")
    if img3:
        with col_tat_2: # Colocado no meio para destaque
            st.image(img3, use_container_width=True, caption="Tributo Tático - Honra Forjada")
    else:
        col_tat_2.info("Imagem IMG_4672 2.jpg não encontrada no diretório.")

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# SEÇÃO 3: O ARQUITETO DO LEGADO (SOBRE O FUNDADOR)
st.markdown("<h2>O ARQUITETO DO LEGADO</h2>", unsafe_allow_html=True)

col_bio1, col_bio2 = st.columns([2, 3])

with col_bio1:
    # Como não temos uma foto específica do fundador nas imagens anexadas, usamos um placeholder ou deixamos espaço
    st.markdown("""
    <div style="border: 1px solid #DAA520; padding: 50px; text-align: center; height: 100%; display: flex; align-items: center; justify-content: center;">
        <span style="color: #DAA520; font-size: 1.2rem;">"Eu não sou mais um impressor de miniaturas.<br>Eu sou o arquiteto do legado e o artífice da honra."</span>
    </div>
    """, unsafe_allow_html=True)

with col_bio2:
    st.markdown("""
    **Frederico Rabelo** une dois mundos que não admitem covardia ou falsidade: fé e linha de frente. Policial Militar e Cristão, nascido no interior de São Paulo, hoje reside no Distrito Federal.
    
    Com um profundo entendimento sobre hierarquia, dever e reverência, Frederico organiza seu tempo com rigor espartano. Dedica-se ao trabalho policial, aos estudos jurídicos contínuos, à criação de modelagem 3D e à pintura artística de figuras Sacras e Corporações Policiais.
    
    O ateliê da Sacrominis nasceu de uma necessidade singular: encontrar na arte a âncora para equilibrar a mente em um mundo sedento por atenção. Hoje, no silêncio do ateliê, ele forja os relicários da Sacrominis.
    """)

st.markdown("<br><br>", unsafe_allow_html=True)

# SEÇÃO 4: RODAPÉ E CONTATO
st.markdown("""
<div style='text-align: center; padding: 20px; background-color: #050505; border-top: 1px solid #DAA520;'>
    <h4 style='color: #DAA520;'>A Barreira Intransponível (Rigor Moral)</h4>
    <p style='font-size: 0.9rem; color: #a0a0a0; max-width: 800px; margin: 0 auto;'>
        "A Sacrominis recusa absolutamente qualquer obra ou contrato, por mais lucrativo que seja, que vá contra a nobreza da Polícia Militar ou que vilipendie a fé católica."
    </p>
    <br>
    <p style='color: #FFFFF0;'>Para requerer uma obra ou obter o Certificado de Autenticidade, entre em contato.</p>
    <a href="mailto:contato@sacrominis.com" style='color: #DAA520; text-decoration: none; border: 1px solid #DAA520; padding: 10px 20px; border-radius: 3px; display: inline-block; margin-top: 10px;'>Solicitar Contato</a>
</div>
""", unsafe_allow_html=True)
