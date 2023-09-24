import os
from dotenv import load_dotenv
import openai




# Cargar variables de entorno
load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY', '')

# Asignar la API Key
openai.api_key = OPENAI_KEY

def mychatbot(messages):
    # Chatbot que hace consultas "query" a una base de conocimiento "contract_knowledge"

    # Enviar solicitud a la api OpenAI con el modelo "GPT-3.5-turbo"
    res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = messages
    )

    # Del diccionario extraer la informacion correspondiente al id "content"
    conclusion = res['choices'][0]['message']['content']
    
    return conclusion


def hacer_evaluacion(base_knowledge, question, transcripcion):

    prompt = f"""
    Dada la siguiente pregunta realizada por un cliente: {question}. Para la siguiente transcripcion de la respuesta que le dio Call Center: {transcripcion}
    Da RECOMENDACIONES para mejorar el contenido y la manera de responder a esa respuesta a esa pregunta.
    Apoya tu respuesta en los siguientes aspectos:
    - RED FLAGS, GREEN FLAGS
    - Si el TONO y VOCABULARIO es el adecuado para responder la pregunta, 
    - Si es precioso el contenido y responde a la pregunta
    Dame las recomendaciones en un texto NO SUPERIOR a 150 caracteres. Da CONSEJOS para mejorar como formular la respuesta a esta pregunta.
    Aplica saltos de linea para separar cada parrafo y emojis para resaltar cada uno de las solicitudes.

    Si la respuesta no responde totalmente a la pregunta, extrae informacion de la base de conocimiento y haz un parrafo con información que se debe mencionar ante dicha pregunta.
    """


    # Dialogo con ChatGPT
    messages = [
        {"role": "system", "content": "Eres un asistente útil experto en proceso de onboarding y evaluacion de personal de un Call Center."},
        {"role": "user", "content": "Responda mis consultas de acuerdo con el contexto dado. Si no se tiene una respuesta clara o sin información se debe indicar. \nLa base de conocimiento se considera la información proporcionada del siguiente enlace a la pagina web de la compañía: {}".format(str(base_knowledge))},
        #{"role": "user", "content": "Responda mis consultas de acuerdo con el contexto dado. Si no se tiene una respuesta clara o sin información se debe indicar."},
        {"role": "assistant", "content": "¡Ok, seguro!"},
        #{"role": "system", "content": "Aplica markdown para resaltar cada uno de las solicitudes y emojis para mejorar el UX de la experiencia"},
        #{'role': 'assistant', 'content': base_knowledge},
        {"role": "user", "content": prompt}
    ]

    #base_knowledge = "Truora es una empresa tecnológica que se especializa en soluciones de verificación de antecedentes y autenticación digital. Fundada en Colombia en 2016, la empresa se ha convertido en un líder en el campo de la seguridad y la confiabilidad de datos en América Latina. Su objetivo principal es proporcionar herramientas y servicios que permitan a las empresas y organizaciones tomar decisiones más informadas al evaluar la integridad y la autenticidad de las personas y las transacciones en línea."
    #base_knowledge = "Obtene tu contexto de https://www.truora.com/es/"



    # Output
    respuesta = mychatbot(messages)


    return respuesta

def medir_KPI(duracion, transcripcion):

    prompt = f"""
    Debes realizar un analisis de rendimiento de respuestas de call centers ante preguntas de clientes.
    Para la siguiente transcripcion de la respuesta que dio el Call Center: {transcripcion} cuya duración del audio es {duracion} segundos.
    Dame las siguientes MÉTRICAS:
    - La claridad de las palabras con un porcentaje, donde 0% cuando no se entiende nada y 100% cuando se entiende su totalidad.
    - La velocidad de palabras por minuto, indicar si es muy lento o muy rapido y dar un consejo para mejorar la velocidad y se comprenda mejor.
    - INSIGHTS POSITIVOS Y NEGATIVOS, cada uno con FEEDBACK POSITIVO Y NEGATIVO.
    Dame las metricas mencionadas en un texto NO SUPERIOR A 150 caracteres. 
    Aplica saltos de linea para separar cada parrafo y emojis y resaltar cada uno de las solicitudes. 
    """

    # Dialogo con ChatGPT
    messages = [
        {"role": "system", "content": "Eres un asistente útil experto en proceso de onboarding y evaluacion de personal de un Call Center."},
        {"role": "user", "content": "Responda mis consultas de acuerdo con el contexto dado. Si no se tiene una respuesta clara o sin información se debe indicar."},
        {"role": "assistant", "content": "¡Ok, seguro!"},
        #{"role": "system", "content": "Aplica markdown para resaltar cada uno de las solicitudes y emojis para mejorar el UX de la experiencia"},
        {"role": "user", "content": prompt}
    ]

    # Output
    respuesta = mychatbot(messages)

    return respuesta

