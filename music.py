# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# streamlit run your_script.py
# python -m streamlit run music.py
#Instalamos las librerías necesarias
import streamlit as st #Para ejecutar la página
import pandas as pd #Para acceder a nuestra csv en Visual Studio Code
from streamlit_option_menu import option_menu #Para generar el menú de opciones ubicado al lado izquierdo de la página
import random #Para la elección de un artista aleatorio (será explicado en el apartado utilizado)

# Cargar archivo
df = pd.read_csv("artistas.csv")

# Corregir nombre de columna con espacio extra
df.rename(columns={"artista _musical": "artista_musical"}, inplace=True)

# st.sidebar.image("nombre del logo", use_container_width=True)
# En este apartado, la libería "option_menu" es primordial
# Con "with st.sidebar" creamos el menu de opciones que contiene las 5 pestañas de la página
with st.sidebar:
    # Mostrar logo encima del menú. 
    st.image("logo_ori.png", use_container_width=True)

    # Menú de navegación generado con listas
    selected = option_menu(
        menu_title=None,  
        options=["Inicio", 'Descubre', 'Tendencias', 'Géneros', 'Aportes'], #Lista de pestañas
        icons=['house', 'search', 'fire', 'music-note-list', 'envelope'], #Lista de iconos correspondientes a cada pestaña
        default_index=0
    )
# Con la función "if" condicionamos que si escoge "Inicio" estaremos en la primera pestaña    
if selected == "Inicio":
    st.image("logo.png", width=700)
    # La función st.markdown permite establecer ciertos parámetros en texto sen Streamlit
    # el atributo style se utiliza para agregar estilos CSS.
    # <h1 style='text-align: justifty: para alinear el texto. Esto varia de acuerdo a la preferencia
    # font-size: 20px;'>: para el tamaño de la letra
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    st.markdown("""
    <div style='text-align: justify; font-size: 20px;'>
    <p>¡Bienvenido a un viaje sonoro por Ecos del Perú! Esta página es un homenaje vibrante a la música peruana en toda su diversidad, desde las montañas hasta la selva y las ciudades costeras. Aquí encontrarás una exploración profunda de un aproximado de más de diez géneros que han marcado la identidad del país: desde la energía contagiante del rock y la cumbia, hasta la fuerza ancestral de la música andina y la modernidad del urbano y el hip hop.</p>
    <p>Pero no solo hablamos de estilos, también celebramos a quienes los hacen posibles. Navega por las historias de leyendas consagradas y descubre a talentos emergentes que están transformando la escena nacional. Encontrarás perfiles de artistas, sus trayectorias, y el impacto social que han generado a través de la música. Esta es más que una página, es una ventana abierta a los sonidos que nos definen como país.</p>
    </div>
    """, unsafe_allow_html=True)
    # Subtitulo 
    st.header('🎼 Géneros Musicales Peruanos')
    # expansor de St. permite insertar un contenedor de varios elementos que pueda expandirse o contraerse
    # Contiene varios elementos y que el usuario puede expandir o contraer. Al contraerlo, solo se ve la etiqueta proporcionada
    with st.expander('Rock'): #Usamos "with" para añadir elementos al contenedor devuelto
        st.markdown("<div style='text-align: justify; font-size: 15px;'><p>El rock peruano surgió en los años 60, influenciado por el beat británico y el rock psicodélico estadounidense, pero pronto empezó a dialogar con la realidad local. Enfrentó censura, golpes militares y desinterés comercial, lo que no impidió su desarrollo en circuitos alternativos. Con el tiempo, incorporó elementos andinos, criollos y urbanos, dando paso a una identidad sonora única. Desde bandas pioneras como Los Saicos hasta propuestas contemporáneas, el rock en Perú ha sido vehículo de rebeldía, crítica social y expresión cultural.</div>", unsafe_allow_html=True) 
        st.image('rock_peruano.jpg', width=700)

    with st.expander('Chicha'):
        st.markdown("<div style='text-align: justify; font-size: 15px;'><p>La chicha nació en los años 70 como una fusión entre la cumbia colombiana, el rock psicodélico y los ritmos andinos traídos por los migrantes del interior a Lima. Surgió en un contexto de cambio social, dando voz a sectores populares marginados. A pesar del estigma que enfrentó por décadas, evolucionó con fuerza, integrando teclados eléctricos, guitarras distorsionadas y letras urbanas. Hoy, es un símbolo de identidad cultural y resistencia.</div>", unsafe_allow_html=True) 
        st.image('chicha.jpg', width=700)

    with st.expander('Salsa'):
        st.markdown("<div style='text-align: justify; font-size: 15px;'><p>La salsa en el Perú se popularizó en los años 70, influenciada por el boom salsero de Nueva York y el Caribe, y rápidamente fue adoptada por barrios populares limeños. En medio de contextos de migración y efervescencia urbana, se convirtió en una forma de expresión colectiva, con letras que hablaban de amor, lucha y cotidianidad. Aunque enfrentó la hegemonía de otros géneros, la salsa peruana creció con orquestas locales que imprimieron su propio estilo. Hoy, sigue viva en peñas, conciertos y nuevas generaciones de salseros.</div>", unsafe_allow_html=True) 
        st.image('salsa.png', width=700)

    with st.expander('Cumbia'):
        st.markdown("<div style='text-align: justify; font-size: 15px;'><p>La cumbia peruana emergió en los años 60 como una adaptación local de la cumbia colombiana, fusionada con ritmos amazónicos, guitarras eléctricas y sonidos tropicales. Su auge coincidió con procesos de migración interna, convirtiéndose en la banda sonora de una nueva identidad urbana. A pesar del rechazo inicial de ciertos sectores, logró consolidarse como un género masivo y diverso. Con el tiempo, dio origen a subgéneros como la cumbia amazónica y la tecnocumbia.</div>", unsafe_allow_html=True)
        st.image('cumbia.jpg', width=700)

    with st.expander('Hip Hop'):
        st.markdown("<div style='text-align: justify; font-size: 15px;'><p>El hip hop en el Perú nació en los años 90 como una expresión de las juventudes urbanas, influenciado por el movimiento global pero profundamente marcado por la realidad local. Surgió en calles, barrios y plazas, abordando temas como la desigualdad, la discriminación y la resistencia. A través del rap, el breakdance y el graffiti, encontró formas de visibilizar identidades marginadas. Hoy, el hip hop peruano es un movimiento activo y diverso, con voces potentes desde Lima hasta regiones del interior.</div>", unsafe_allow_html=True)
        st.image('hiphop.jpg', width=500)

    with st.expander('Urbano'):
        st.markdown("<div style='text-align: justify; font-size: 15px;'><p>La música urbana en el Perú tomó fuerza en los años 2000, influenciada por el reguetón, el trap y otros ritmos latinos que llegaron desde el Caribe y Estados Unidos. Inicialmente vista como música pasajera, fue adoptada por jóvenes de distintos sectores que encontraron en sus letras una forma de hablar sobre el amor, la fiesta, la lucha diaria y la vida en la ciudad. A lo largo del tiempo, el género se ha fusionado con sonidos locales, creando un estilo propio y ganando espacios en radios, festivales y plataformas digitales.</div>", unsafe_allow_html=True)
        st.image('urbano.png', width=700)

    with st.expander('Andino'):
        st.markdown("<div style='text-align: justify; font-size: 15px;'><p>La música andina en el Perú tiene raíces ancestrales que se remontan a las civilizaciones prehispánicas, con instrumentos como la quena, el charango y el bombo. Durante siglos, ha sido una forma de preservar la memoria, la cosmovisión y las tradiciones de los pueblos originarios. En el siglo XX, se revitalizó con nuevas fusiones y migró a los espacios urbanos, adaptándose sin perder su esencia. Ha enfrentado estigmas sociales, pero hoy es símbolo de orgullo e identidad cultural.</div>", unsafe_allow_html=True)
        st.image('andina.jpg', width=700)

    with st.expander('Pop'):
        st.markdown("<div style='text-align: justify; font-size: 15px;'><p>El pop peruano comenzó a consolidarse en las décadas de 1980 y 1990, influenciado por las corrientes del pop latino y anglosajón, pero adaptado a las sensibilidades locales. Aunque inicialmente tuvo poca visibilidad frente a géneros más populares, logró abrirse paso gracias a artistas que fusionaron melodías accesibles con letras que reflejan vivencias peruanas. En los últimos años, ha ganado fuerza con propuestas frescas y producciones independientes que mezclan pop con sonidos andinos, urbanos y electrónicos.</div>", unsafe_allow_html=True)
        st.image('pop.png', width=700)

    with st.expander('Criollo'):
        st.markdown("<div style='text-align: justify; font-size: 15px;'><p>La música criolla es uno de los pilares de la identidad cultural peruana, con raíces en la costa y una fusión de influencias españolas, africanas e indígenas. Surgió en los barrios populares de Lima como expresión del alma mestiza, a través de géneros como el vals, la marinera y el festejo. Sus letras hablan de amor, nostalgia, barrio y patria, y durante décadas fue la voz sentimental del país. Aunque ha enfrentado cambios generacionales, sigue viva en peñas, guitarras y nuevas interpretaciones.</div>", unsafe_allow_html=True)
        st.image('criolla.jpg', width=700)
# Con la función "elif" condicionamos que si escoge "Descubre" estaremos en la segunda pestaña  
elif selected == "Descubre":
    elección = ['artista_musical', 'biografía', 'Link_información', 'url_imagen', 'género_musical',
                'audiencia_Spotify', 'canción_más_escuchada', 'reproducciones', 'url_video']
    # La función "random" selecciona aleaotoriamanente un artista de la base de datos
    # df[elección]: Accede a un elemento de la lista "elección"
    # .sample(1): Toma una muestra aleatoria de un solo elemento de esa lista
    # .iloc[0]: Accede al primer (y único) valor de esa muestra aleatoria y arroga un artista X
    artista_random = df[elección].sample(1).iloc[0]

    st.subheader("🎤 Artista aleatorio:")
    # Parametros para la selección de imágenes
    st.markdown(f"""<div style="text-align: center;">
        <img src="{artista_random['url_imagen']}" width="500" />
        <p style="font-weight: bold;">{artista_random['artista_musical']}</p></div>""",
        unsafe_allow_html=True)
    # Presentación de los datos arrogados
    # Crear dos columnas para distribuir la información y que se visualice de manera ordenada
    col1, col2 = st.columns([1, 2]) 

    # Columna 1: 5 datos 
    with col1:
        st.markdown(f"**🎶 Nombre:** {artista_random['artista_musical']}")
        st.markdown(f"**🎧 Género:** {artista_random['género_musical']}")
        st.markdown(f"**🌍 Audiencia en Spotify:** {artista_random['audiencia_Spotify']}")
        st.markdown(f"[🔗 Más información]({artista_random['Link_información']})")
        st.markdown(f"[🎬 Ver video]({artista_random['url_video']})")
    # Columna 2: 2 datos
    with col2:
        st.markdown(f"<div style='text-align: justify; font-size: 15px;'><strong>📝 Biografía:</strong> {artista_random['biografía']}</div>",
        unsafe_allow_html=True)
        st.markdown(f"**🔥 Canción más escuchada:** {artista_random['canción_más_escuchada']} ({artista_random['reproducciones']} reproducciones)")

# Con la función "elif" condicionamos que si escoge "Tendencias" estaremos en la tercera pestaña  
elif selected == "Tendencias":
    # Función para convertir valores de audiencia como '3.2M' o '850K' a número real
    def convertir_audiencia(valor):
        if pd.isna(valor): #Si el valor es Nan, se devuelve 0
            return 0
        if isinstance(valor, str): #Si es cadena de texto, se limpia y convierte
            valor = valor.strip()
            if 'M' in valor:
                return float(valor.replace('M', '')) * 1_000_000 #3.2M -> 3,200,000
            elif 'k' in valor:
                return float(valor.replace('k', '')) * 1_000 #850k -> 850,000
            else:
                try:
                    return float(valor)
                except ValueError:
                    return 0
        try:
            return float(valor)  #Si ya es numérico, lo convierte directamente
        except:
            return 0

    # Aplicamos la conversión a la columna de audiencia original
    # Se crea una nueva columna audiencia_convertidas en el DataFrame con los valores numéricos procesados a partir de audiencia_Spotify
    df['audiencia_convertida'] = df['audiencia_Spotify'].apply(convertir_audiencia)

    # Ordenamos los artistas por mayor audiencia y tomamos los 10 más altos
    # Se genera un nuevo DataFrame con los 10 artistas con mayor audiencia en Spotify
    # ordenadnos de forma descendente "ascending=False"
    top_10 = df.sort_values(by='audiencia_convertida', ascending=False).head(10)

    # Se añade una columna con el ranking del 1 al 10
    # Se asignan los puestos del ranking de manera secuencial
    top_10['Ranking'] = range(1, len(top_10) + 1)

    # Reiniciamos el ínidce para mostrar una tabla limpia
    # Se elimina el índice original del DF para evitar confusión en la visualización
    top_10 = top_10.reset_index(drop=True)

    # Encabezado
    st.subheader("🔥 Top Artistas en Tendencia")

# Recorremos cada artista del Top 10 para mostrar su imagen y datos
    for index, row in top_10.iterrows():
        # Dividimos en 2 columnas: imagen | info
        col1, col2 = st.columns([1.2, 3])

        with col1:
            # Mostramos la imagen del artista en un tamaño definido
            st.image(row['url_imagen'], width=160)

        with col2:
            # Nombre del artista con ranking
            st.markdown(f"### {row['Ranking']}. {row['artista_musical']}")
            # Audiencia visual
            st.markdown(f"🎧 Audiencia: {row['audiencia_Spotify']}")
# Con la función "elif" condicionamos que si escoge "Géneros" estaremos en la cuarta pestaña
elif selected == "Géneros":
    st.subheader("🎶 Explora artistas por género musical")

    # Diccionario de imágenes por género
    imagenes_genero = {
        'Andino': 'andina.jpg',
        'Chicha': 'chicha.jpg',
        'Criollo': 'criolla.jpg',
        'Cumbia': 'cumbia.jpg',
        'Electrónica': 'electronica.jpeg',
        'Fusión': 'fusion.jpeg',
        'Hip hop': 'hiphop.jpg',
        'Humor/Viral': 'humor.png',
        'Parodia': 'parodia.jpg',
        'Pop': 'pop.png',
        'Reggae/Funk': 'reggae.jpeg',
        'Rock': 'rock_peruano.jpg',
        'Salsa': 'salsa.png',
        'Tecnocumbia': 'tecnocumbia.jpeg',
        'Urbano': 'urbano.png',
    }
    # Se extraen los nombres de los géneros como una lista para iterar sobre ellos fácilmente
    lista_generos = list(imagenes_genero.keys())

    # Inicializamos el estado del género elegido si aún no existe
    # El estado de sesión se utiliza para guardar qué género ha elegido el usuario
    if "genero_elegido" not in st.session_state:
        st.session_state.genero_elegido = None

    # Si aún no se ha elegido un género, mostrar las imágenes como botones
    if st.session_state.genero_elegido is None:
        st.markdown("Selecciona un género musical:")
        cols = st.columns(4) #Distribuye los géneros en 4 columnas
        for i, genero in enumerate(lista_generos):
            col = cols[i % 4] #Asigna cada género a una columna cíclicamente
            with col:
                st.image(imagenes_genero[genero], use_container_width=True) #Imagen del género
                if st.button(f"{genero}", key=genero): # Botón con el nombre del género
                    st.session_state.genero_elegido = genero #Guarda la elección
                    st.rerun() # Recarga la app para mostrar artistas del género

    # Mostrar artistas si ya se eligió un género
    else:
        genero = st.session_state.genero_elegido
        st.markdown(f"### 🎧 Artistas del género: {genero}")
        #Filtra el DF para mostrar solo artistas que contengan el género elegido
        df_filtrado = df[df['género_musical'].str.contains(genero, case=False, na=False)]
        # Si no se encuentran artistas, se muestra una advertencia
        if df_filtrado.empty:
            st.warning("No se encontraron artistas con ese género.")
        #Si hay artistas, se muestran uno por uno
        else:
            for index, row in df_filtrado.iterrows():
                col1, col2 = st.columns([1.2, 3])
                with col1:
                    st.image(row['url_imagen'], use_container_width=True)
                with col2:
                    st.markdown(f"### {row['artista_musical']}")
                    st.markdown(f"🎧 Audiencia: {row['audiencia_Spotify']}")
                    st.markdown(f"🎵 Género: {row['género_musical']}")

        st.markdown("---")
        # Botón para regresar a la selección de géneros
        if st.button("🔙 Volver a géneros"):
            st.session_state.genero_elegido = None #Reinicia la selección
            st.rerun() #Recarga la app para volver a mostrar los botones por género
# Con la función "elif" condicionamos que si escoge "Aportes" estaremos en la quinta pestaña
elif selected == "Aportes":
    st.title("📬 Aporta un artista a Ecos del Perú")

    st.markdown("¿Conoces un artista peruano que deba estar aquí? ¡Compártenos su información!")
    # st.session_state guarda si el usuario ya ha enviado un aporte durante la sesión actual,
    # evitanso que se vuelva a mostrar el formulario tras el envío
    # Inicializa el estado para controlar si ya se envió un aporte
    if "aporte_enviado" not in st.session_state:
        st.session_state.aporte_enviado = False

    if not st.session_state.aporte_enviado:
        #Sección del formulario
        with st.form("form_aporte"):
            nombre = st.text_input("🎤 Nombre del artista")
            url_imagen = st.text_input("🖼️ URL de la imagen")
            biografia = st.text_area("📖 Biografía del artista")
            audiencia = st.text_input("👥 Audiencia mensual en Spotify (ej: 3.2M o 120K)")
            cancion_mas_escuchada = st.text_input("🎧 Canción más escuchada")
            link_cancion = st.text_input("🔗 Link de la canción en Spotify")
            vistas_cancion = st.text_input("📈 Visualizaciones/reproducciones de la canción")

            submit = st.form_submit_button("Enviar aporte")

        if submit:
            #Validación: nos aseguramos de que todos los campos estén llenos
            if all([
                nombre.strip(),
                url_imagen.strip(),
                biografia.strip(),
                audiencia.strip(),
                cancion_mas_escuchada.strip(),
                link_cancion.strip(),
                vistas_cancion.strip()
            ]):
                nuevo = {
                    "artista_musical": nombre,
                    "url_imagen": url_imagen,
                    "biografía": biografia,
                    "audiencia_Spotify": audiencia,
                    "canción_más_escuchada": cancion_mas_escuchada,
                    "url_video": link_cancion,
                    "reproducciones": vistas_cancion
                }
            # Si la validación es exitosa, se construye un diccionaro con los datos del nuevo artista para agregarlo a un arhcivo .csv
            # aportes.csv almacenará los aportes que se hagan. 
                try:
                    df_aportes = pd.read_csv("aportes.csv")
                except FileNotFoundError:
                    df_aportes = pd.DataFrame(columns=nuevo.keys())
                # En este caso, el archivo no existe al ingresar por primera vez los aportes, entonces se crea un nuevo DF con las mismas
                # columnas que el diccionario "nuevo"
                df_aportes = pd.concat([df_aportes, pd.DataFrame([nuevo])], ignore_index=True)
                df_aportes.to_csv("aportes.csv", index=False)
                #Se actualiza el estado de sesión para indicar que el aporte ya fue enviado y se recarga la pestaña para 
                #mostrar el mensaje de éxito en lugar del formulario 
                st.session_state.aporte_enviado = True
                st.rerun()
            # Si hay campos vacíos, sem muestra un mensaje de error para advertir el usuario
            else:
                st.error("Por favor, completa **todos los campos** antes de enviar el aporte.")
    # Si envió de manera correcta su aporte, se presneta un mensaje de agradecimiento en lugar del formulario
    else:
        st.success("¡Gracias por tu aporte! El artista ha sido registrado correctamente. 🙌")
