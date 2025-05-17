import base64
import streamlit as st

st.set_page_config(
    page_title="servidor",
    page_icon="https://cdn-icons-png.flaticon.com/128/6071/6071905.png",
    layout="wide"
)

# Inyectar CSS personalizado
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-image: url("https://static.vecteezy.com/system/resources/previews/013/882/390/non_2x/vertical-panorama-banner-cybersecurity-information-privacy-data-protection-virus-and-spyware-photo.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;

        /* Capa oscura encima de la imagen */
        background-color: rgba(0, 0, 0, 0.6); /* negro con opacidad */
        background-blend-mode: darken;
    }
    </style>
    """,
    unsafe_allow_html=True
)


with st.sidebar:
    st.image("icono.png", width=200)
    st.header(":blue[Integrantes]",divider="gray")
    st.write("• Andrés Felipe Ramírez Mackenzie ")
    st.write("• Keiner Zuñiga Romero ")


st.header("Bienvenidos",divider="blue")
st.write("Este laboratorio pertenece a la categoría HACKING-TIME, se realizan en parejas compitiendo uno contra otro para demostrar quien tiene de momento mejores capacidades para desenvolverse en el mundo de la seguridad informática. Si resultas ser el vencedor Felicidades!!, sino recuerda, la práctica hace al maestro y seguir entrenando y estudiando te harán cada vez mejor.")


st.subheader("📄 Documentación")

# Ruta del PDF local
pdf_path = "documento.pdf"

# Leer el archivo PDF y convertirlo a base64
with open(pdf_path, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode("utf-8")

# Crear el HTML para incrustar el PDF
pdf_display = f"""
<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="700px" type="application/pdf"></iframe>
"""

# Botón para mostrar el PDF
if st.button("📖 Ver documentación"):
    st.markdown(pdf_display, unsafe_allow_html=True)


st.subheader("Configuracion del entorno",divider="blue")
with st.expander("ver capturas del procedimiento👇"):
    
    st.subheader("Buscar el firewall de windows")
    st.image("image/Firewall.png")
    st.write("""
        Buscamos en el buscador de windows firewall, ingresamos al que diga firewall de windows defender y le damos a la opción de Activar o desactivar el firewall de windows defender.
        """)
    
    st.subheader("Desactivar Firewall")
    st.image("image/Desactivar_Fireware.png")
    st.write("""
        luego desactivamos el firewall de windows defender como se ve en la imagen, tanto en la red privada como en la publica, para que no haya problemas de conexión entre las maquinas virtuales. 
        """)
    
    st.subheader("Activar el escritorio remoto")
    st.image("image/Activar_Escritorio_Remoto.png")
    st.write("""
        Activamos la opción de escritorio remoto en las configuraciones de Windows Server, esto se hace para poder acceder de manera remota a la máquina.
        """)
    
    st.subheader("Preparación de los archivos")

    st.image("image/creacion_de_carpeta.png", caption="Creación de la carpeta")
    
    # Crear 3 columnas
    col1, col2 = st.columns(2)
    # Insertar imágenes en las columnas
    with col1:
        st.image("image/usuarios_guardados.png", caption="Usuarios guardados")
        st.image("image/creacion_de_txt.png", caption="Creación del archivo .txt")

    with col2:
        st.image("image/contraseñas_guardadas.png", caption="Contraseñas guardadas")
        st.image("image/creacion_carta.png", caption="Creación de la carta")


    # Descripción final
    st.write("""
    Preparamos los archivos necesarios para la vulneración, creamos una carpeta en el Disco Local (C:) llamada como el nombre del usuario. Luego dentro de la carpeta creamos dos archivos .txt llamado usuarios.txt donde guardamos 5 usuarios donde solo uno es el verdadero, otro archivo llamado contraseñas.txt donde guardamos las contraseñas 30 contraseñas donde solo una es la verdadera y por último una carpeta llamada carta y dentro creamos otro archivo .txt que se llama carta.txt con un mensaje para el ganador.
    """)
    
    st.subheader("Analisis de red")
    st.image("image/nmap.png")
    st.write("""
        Verificamos con nmap si el puerto 3389 está abierto, para poder realizar la vulneración al escritorio remoto.Para esto utilizamos el comando nmap -p 3389 -sV -Pn <IP>, donde <IP> es la dirección IP de la máquina a la que queremos acceder.
        """)
    
    st.subheader("Obtención de la IP del rival")
    st.image("image/ping.png")
    st.write("""
        Utilizamos el comando ping para obtener la dirección IP de la máquina de nuestro compañero. Esto nos permitirá realizar un escaneo más específico y encontrar posibles vulnerabilidades. Basandonos en el nombre de la máquina de nuestro compañero.
        """)
    

st.subheader("Acceso al escritorio remoto del compañero", divider="blue")
st.video("https://youtu.be/CWl2e_ClSmo")

st.markdown("""
### 📹 Descripción del video

En este video se realiza la **vulneración al escritorio remoto** de nuestro compañero, en base a las credenciales *filtradas*. 

🔹 Se configura un **DNS dinámico** para acceder a su **IP pública**.  
🔹 Previamente, se había obtenido dicha IP mediante un **análisis de red**.  
🔹 Posteriormente, se lanza un ataque al escritorio remoto, probando las contraseñas filtradas del usuario.

Tras múltiples intentos, se logra el acceso exitoso al escritorio remoto, lo que permite visualizar la **información almacenada**, como las fotos y una carta personal.
""")

st.subheader("Configuracion del entorno - Revancha",divider="blue")
with st.expander("ver capturas del procedimiento👇"):
    
    st.subheader("Abrir el editor de registro")
    st.image("image/comando_para_abrir_el_editor_de_registro.png")
    st.write("""
        con el comando win+R abrimos un cuadro de dialogo, donde escribimos regedit y le damos enter, para abrir el editor de registro de windows.
        """)
    
    st.subheader("Abrir el editor de registro")
    st.image("image/ruta_para_cambiar_el_puerto.png")
    st.write("""
        En la linea subrayada en azul copiamos la siguiente ruta HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp
        """)
    
    st.subheader("Busqueda del archivo PortNumber")
    st.image("image/busqueda_de_portnumber.png")
    st.write("""
        Buscamos el archivo PortNumber, que es el que contiene el puerto por defecto del escritorio remoto, que es el 3389.
        """)
    
    st.subheader("Modificacion del archivo PortNumber")
    st.image("image/cambiar_puerto.png")
    st.write("""
        Cambiamos el valor del puerto por defecto 3389 a cualquier otro que este entre los rangos de 1024 – 65535, para que no haya problemas de conexión entre las maquinas virtuales nuevamente.
        """)
    
    
    
    