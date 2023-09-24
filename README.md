# King-George-AI

**Legal Insight AI** es un programa de análisis de contratos basado en inteligencia artificial (IA). Simplifica la comprensión legal, toma decisiones informadas y optimiza tu flujo de trabajo. 

Este proyecto es parte del Coding Challenge de [Makers Fellowship](https://www.makers.build/) 2023.


# <br>Tecnologías ⚙️
Este proyecto se ha desarrollado utilizando Python 3.0, Gradio, Firebase y ChatGPT de OpenAI.
- **Gradio 🖌:** Una biblioteca de interfaz de usuario (UI) de Python que facilita la creación de interfaces de usuario interactivas 
- **ChatGPT 🤖:** Api de Inteligencia Artificial que proporciona modelos de lenguaje y capacidades de procesamiento de texto avanzadas.
- **Whisper 🤖:** Api de Inteligencia Artificial que proporciona procesamiento de lenguaje natural (NLP) y desarrollo de servicios de voz interactivos


# <br>¿Cómo usar el programa? 💻
Para poder **inicializar el programa** desde la consola debes seguir los siguientes pasos:

0) Instala las dependencias: `pip3 install -r requirements.txt`
1) Ejecuta desde la terminal el programa **`app.py`**  
2) Copia la URL y pega en tu navegador. Y ya puedes utilizar la interfaz gráfica (GUI).
<br>

Para **hacer una consulta desde la GUI** debes seguir los siguientes pasos:

1) **Carga el contrato** que deseas analizar.
2) **Selecciona las categorías** que deseas analizar.
3) **Opcional:** Haz una pregunta puntual.
4) Haz clic en **"Analizar"**.
5) Espera los resultados.
6) Explora las conclusiones y **obten insights**.

Si hiciste bien los pasos, deberias obtener un resultado similar al siguiente:

![captura de pantalla de la ejecución del programa Legal Insight AI](img/captura.JPG)

# <br>Nuestra API 📩

**Puedes consumir nuestro servicio también vía API**.
<br>El endpoint es `run/predict` donde puedes hacer peticiones POST con tu data.
<br>Para ver la implementación recurrir a `call_api.py`

# <br>Variables de Entorno 🔑
Para utilizar el programa, es necesario generar tus propias claves de API. Sigue estos pasos para configurar las claves API necesarias:

1) Crea un archivo llamado **.env** en la raíz de tu proyecto

2) Dentro del archivo .env, agrega las credenciales de tu base de datos de Firebase.
```
# FIREBASE DATABASE
DATABASE_URL = "URL base de datos de Firebase"

FIREBASE_CREDENTIALS = "Biblioteca .JSON con las credenciales"
```
3) Dentro del archivo .env, agrega las credenciales de tu cuenta de OpenAI.
```
# OPEN AI CREDENTIAL
OPENAI_KEY = "Agrega tu OpenAI Api Key"
```

# <br>Convención de commits 🎯
Se utilizó el [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):
una convención de reglas para crear un historial de commits explícito; lo que facilita la escritura de herramientas automatizadas encima. 

# <br> Contacto 🌟
Ante consultas, me puedes consultar por mi perfil de [Linkedin](https://www.linkedin.com/in/mario-bustillo/).
