import streamlit as st

st.set_page_config(page_title="Luthier Jazz App", page_icon="🎸")

st.title("🎸 Directorio de Plantillas de Guitarra")
st.write("Bienvenido, **Kuzlas**. Gestor de planos escala 1:1.")

# Opciones de papel
st.sidebar.header("Ajustes de Impresión")
papel = st.sidebar.radio("Tamaño del papel:", ["A4 (Mosaico)", "A3"])

# Selección de Guitarras de Jazz
st.subheader("Selección de Modelos de Jazz")
modelo = st.selectbox(
    "Escoge el plano que quieres convertir a PDF:",
    ["Gibson L-5 CES (Archtop)", "Gibson ES-335 (Semi-hollow)", "Gibson ES-175", "D'Angelico New Yorker", "Benedetto Archtop"]
)

if st.button(f"Generar PDF de {modelo}"):
    st.info(f"Preparando plano para {papel}. Esto dividirá el diseño en varias hojas con marcas de unión.")
    st.success("✅ ¡PDF generado con éxito! (Simulación de descarga)")
