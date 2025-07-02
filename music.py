

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# streamlit run your_script.py
# python -m streamlit run music.py

import streamlit as st
import pandas as pd

# Cargar archivo
df = pd.read_csv("artistas.csv")

# Corregir nombre de columna con espacio extra
df.rename(columns={"artista _musical": "artista_musical"}, inplace=True)

# Selector de géneros múltiples
generos_disponibles = sorted(set(g for sub in df['género_musical'].dropna().str.split('|') for g in sub))
generos_filtrados = st.multiselect("Escoge uno o más géneros", generos_disponibles)

# Filtrado estricto por todos los géneros seleccionados
if generos_filtrados:
    df_filtrado = df[df['género_musical'].apply(lambda x: all(g in x.split('|') for g in generos_filtrados if isinstance(x, str)))]
else:
    df_filtrado = df

# Mostrar resultados
for _, row in df_filtrado.iterrows():
    st.subheader(row['artista_musical'])

    if pd.notna(row['url_imagen']):
        st.image(row['url_imagen'], use_container_width=True)

    st.markdown(f"**Biografía:** {row['biografía']}")
    st.markdown(f"**Géneros:** {row['género_musical']}")
    st.markdown(f"**Audiencia mensual en Spotify:** {row['audiencia_Spotify']}")

    # Canción más escuchada
    st.markdown(f"🎵 **Canción más escuchada:** {row['canción_más_escuchada']}")
    st.markdown(f"▶️ **Reproducciones:** {row['reproducciones']}")

    # Enlace a Spotify o YouTube
    if pd.notna(row['url_video']):
        if "youtube" in row['url_video']:
            st.video(row['url_video'])
        else:
            st.markdown(f"[🔗 Escuchar en Spotify]({row['url_video']})")

    # Opcional: redes sociales
    if pd.notna(row['redes_social']):
        st.markdown(f"📱 **Redes sociales:** {row['redes_social']}")

    if pd.notna(row['Link_información']):
        st.markdown(f"[ℹ️ Más información]({row['Link_información']})")

    st.markdown("---")
    
