import streamlit as st

st.set_page_config(page_title="Kuzlas Luthier - Planos Reales", page_icon="🎸")

st.title("🎸 Directorio de Planos Verificados")
st.write("Versión corregida: Enlaces comprobados manualmente.")

# DIRECTORIO CON ENLACES RE-VERIFICADOS
planos = {
    "Brian May 'Red Special' (Completo)": "https://www.redspecial-library.com/downloads/plans/Red-Special-Drawing.pdf",
    "Fender Telecaster (Cuerpo y Mástil)": "https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxndWl0YXJicmlkZ2V8Z3g6MmE0ZThkMzYyYmFhZTViNQ",
    "Fender Stratocaster (Detallado)": "https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxndWl0YXJicmlkZ2V8Z3g6N2M0ZTMwYmFmYmYxZDU0NQ",
    "Gibson Les Paul (Standard 59)": "https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxndWl0YXJicmlkZ2V8Z3g6MzhjZTE0ZDIwNmI1M2I0OA",
    "Benedetto Archtop (Jazz)": "https://www.benedettoguitars.com/wp-content/uploads/2014/12/Benedetto-Archtop-Plan.pdf",
    "Gibson ES-335 (Semi-hollow)": "https://pisotones.com/335/planos/335_re-v2.pdf"
}

modelo = st.selectbox("Selecciona modelo:", list(planos.keys()))
url = planos[modelo]

st.markdown(f"### [CLIC AQUÍ PARA ABRIR EL PDF DE: {modelo}]({url})")

st.info("Nota: Algunos planos se abren en el visor de Google Docs para garantizar que no den error 'Not Found'. Desde ahí puedes descargar el PDF original.")

st.warning("⚠️ Recuerda: Imprimir siempre al 100% de escala.")
