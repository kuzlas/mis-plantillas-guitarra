import streamlit as st

# Configuración visual de la página
st.set_page_config(page_title="Kuzlas Luthier App", page_icon="🎸", layout="centered")

st.title("🎸 Directorio de Plantillas de Guitarra Jazz")
st.markdown("---")
st.write("Bienvenido **Kuzlas**. Selecciona un modelo para obtener el plano técnico a escala real.")

# Diccionario de planos (Nombre: Enlace al PDF)
planos_jazz = {
    "Gibson L-5 CES (Archtop 17\")": "https://www.electricherald.com/wp-content/uploads/2016/06/Gibson-L5-Blueprints.pdf",
    "Gibson ES-335 (Semi-hollow)": "https://www.electricherald.com/wp-content/uploads/2016/06/Gibson-ES335-Blueprints.pdf",
    "Gibson ES-175 (Jazz Standard)": "https://www.electricherald.com/wp-content/uploads/2016/06/Gibson-ES175-Blueprints.pdf",
    "D'Angelico New Yorker": "https://www.electricherald.com/wp-content/uploads/2016/06/DAngelico-New-Yorker-Blueprints.pdf",
    "Benedetto Archtop (Modern Jazz)": "https://www.electricherald.com/wp-content/uploads/2016/01/Benedetto-Archtop-Blueprints.pdf"
}

# Interfaz de selección
modelo_elegido = st.selectbox("Selecciona el modelo de Jazz:", list(planos_jazz.keys()))
papel = st.radio("Tamaño de impresión recomendado:", ["A4 (Mosaico necesario)", "A3 / Plotter (Recomendado)"])

st.info(f"Has seleccionado: **{modelo_elegido}**")

# Botón de descarga
url_plano = planos_jazz[modelo_elegido]

if st.button(f"Abrir Plano de {modelo_elegido}"):
    st.success("✅ Plano localizado con éxito.")
    st.markdown(f"### [📥 CLIC AQUÍ PARA DESCARGAR EL PDF]({url_plano})")
    
    st.warning("""
    **Instrucciones para impresión 1:1:**
    1. Abre el PDF con Adobe Acrobat o un lector oficial.
    2. En los ajustes de impresión, selecciona **'Escala personalizada: 100%'** o **'Tamaño Real'**.
    3. NO selecciones 'Ajustar al área de impresión', o las medidas de la guitarra serán incorrectas.
    """)

st.markdown("---")
st.caption("App creada por Gemini para Kuzlas - 2024")
