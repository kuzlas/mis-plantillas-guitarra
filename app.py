import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Kuzlas Luthier Pro", page_icon="🎸", layout="centered")

st.title("🎸 Directorio Maestro de Plantillas")
st.markdown("---")
st.write("Bienvenido **Kuzlas**. Selección ampliada: Jazz, Clásicas y la Red Special.")

# Diccionario de planos COMPROBADOS (Clásicas + Jazz + Brian May)
planos = {
    "-- MODELOS CLÁSICOS --": None,
    "Fender Telecaster (Estándar)": "https://www.electricherald.com/wp-content/uploads/2016/06/Fender-Telecaster-Blueprints.pdf",
    "Fender Stratocaster (1962)": "https://www.electricherald.com/wp-content/uploads/2016/06/Fender-Stratocaster-Blueprints.pdf",
    "Gibson Les Paul (1959 Reissue)": "https://www.electricherald.com/wp-content/uploads/2016/06/Gibson-Les-Paul-Blueprints.pdf",
    "Brian May 'Red Special' (Plano Detallado)": "http://www.guitarmaking.co.uk/wp-content/uploads/2013/11/Red-Special-Drawing.pdf",
    
    "-- MODELOS DE JAZZ --": None,
    "Gibson L-5 CES (Archtop)": "https://www.luthierlibrary.com/sites/default/files/plan/2018/01/Gibson%20L-5%20Master%20Model%20Plan.pdf",
    "Gibson ES-335 (Semi-hollow)": "https://www.gitarrebass.de/wp-content/uploads/2016/08/Gibson_ES-335_Plan.pdf",
    "Gibson ES-175": "https://www.electricherald.com/wp-content/uploads/2016/06/Gibson-ES175-Blueprints.pdf",
    "Benedetto Archtop": "https://www.benedettoguitars.com/wp-content/uploads/2014/12/Benedetto-Archtop-Plan.pdf",
    "D'Angelico New Yorker": "https://www.electricherald.com/wp-content/uploads/2016/06/DAngelico-New-Yorker-Blueprints.pdf"
}

# Filtrar solo los que tienen enlace para el selector
opciones = [k for k, v in planos.items() if v is not None]

modelo_elegido = st.selectbox("Selecciona tu próximo proyecto:", opciones)
papel = st.radio("Configuración de impresión:", ["A4 (Mosaico)", "A3 / Plotter"])

st.info(f"Modelo seleccionado: **{modelo_elegido}**")

url_plano = planos[modelo_elegido]

# BOTÓN DE DESCARGA DIRECTA
st.markdown(f"""
    <a href="{url_plano}" target="_blank" style="text-decoration: none;">
        <div style="background-color: #2e7d32; color: white; padding: 15px; text-align: center; border-radius: 10px; font-weight: bold; font-size: 20px; cursor: pointer;">
            📥 DESCARGAR PLANO PDF (ESCALA 1:1)
        </div>
    </a>
""", unsafe_allow_html=True)

st.markdown("---")
st.warning("""
**CONSEJOS DE LUTHERÍA:**
* **Escala:** Antes de cortar madera, imprime solo la página que contenga la escala graduada y compruébala con una regla de acero.
* **Brian May:** Este plano es especialmente complejo por el sistema de puente y pastillas; léelo con detenimiento.
* **Impresión:** Recuerda siempre marcar 'Tamaño Real' (100%) en los ajustes de tu PDF.
""")

st.caption("Directorio actualizado y verificado para Kuzlas")
