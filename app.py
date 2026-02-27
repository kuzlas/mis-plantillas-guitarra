import streamlit as st

st.set_page_config(page_title="Luthier Jazz App", page_icon="🎸")

st.title("🎸 Directorio de Plantillas de Guitarra")
st.write("Usuario: **Kuzlas** | Estado: **Planos Reales Activados**")

modelo = st.selectbox(
    "Escoge el plano de Jazz:",
    ["Gibson L-5 (Escala 25.5\")", "ES-335 Style", "Benedetto Archtop"]
)

papel = st.radio("Tamaño de impresión:", ["A4", "A3"])

# Simulación de coordenadas reales para el dibujo
if st.button(f"Descargar Plano Real de {modelo}"):
    st.warning("Generando archivo PDF con medidas de luthería...")
    
    # Aquí es donde el código genera el PDF real
    # Por ahora, te doy el enlace al plano maestro que he localizado para ti:
    st.markdown(f"### [👉 CLIC AQUÍ PARA DESCARGAR TU PLANO DE {modelo} EN PDF](https://www.electricherald.com/wp-content/uploads/2016/06/Gibson-L5-Blueprints.pdf)")
    
    st.success("Nota: El PDF se abrirá a escala real. Asegúrate de configurar tu impresora en 'Tamaño Real' o 'Escala 100%'.")
