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
    
    #messages=[
    #        {"role": "system", "content": "Eres un asistente útil experto en proceso de onboarding y evaluacion de personal de un Call Center."},
    #        {"role": "user", "content": "Responda mis consultas de acuerdo con el contexto dado. Si no se tiene una respuesta clara o sin información se debe indicar. \nLa base de conocimiento se considera la información del siguiente enlace a la pagina web de la compañía: {}".format(str(base_knowledge))},
    #        {"role": "assistant", "content": "¡Ok, seguro!"},
    #        #{"role": "system", "content": "Aplica markdown para resaltar cada uno de las solicitudes y emojis para mejorar el UX de la experiencia"},
    #        {"role": "user", "content": prompt}
    #    ]
    messages = messages
    )

    # Del diccionario extraer la informacion correspondiente al id "content"
    conclusion = res['choices'][0]['message']['content']
    
    return conclusion



def hacer_evaluacion(base_knowledge, question, transcripcion):

    #base_knowledge = "Truora es una empresa tecnológica que se especializa en soluciones de verificación de antecedentes y autenticación digital. Fundada en Colombia en 2016, la empresa se ha convertido en un líder en el campo de la seguridad y la confiabilidad de datos en América Latina. Su objetivo principal es proporcionar herramientas y servicios que permitan a las empresas y organizaciones tomar decisiones más informadas al evaluar la integridad y la autenticidad de las personas y las transacciones en línea."
    #base_knowledge = "Obtene tu contexto de https://www.truora.com/es/"
    #Contexto
    prompt = "Dada la siguiente pregunta: " + question 
    prompt = "El call center dio la siguiente respuesta: " + transcripcion
    prompt += "Se proporciona la transcripcion de la respuesta del call center. Determina  Red Flags, Green Fags, si el tono y vocabulario es el adecuado para responder la pregunta, si es precioso no el contenido y responde a la pregunta. "
    
    # Solicitud
    prompt += "Dame las observaciones mencionadas en un texto no superior a 150 caracteres. Aplica saltos de linea para separar cada parrafo y emojis para mejorar el UX de la experiencia y resaltar cada uno de las solicitudes"
    prompt += "Añade un parrafo de hasta 200 caracteres que incluya la infomación y manera correcta de reponder a esa pregunta"

    # Messages a ChatGPT
    messages = [
        {"role": "system", "content": "Eres un asistente útil experto en proceso de onboarding y evaluacion de personal de un Call Center."},
        {"role": "user", "content": "Responda mis consultas de acuerdo con el contexto dado. Si no se tiene una respuesta clara o sin información se debe indicar. \nLa base de conocimiento se considera la información del siguiente enlace a la pagina web de la compañía: {}".format(str(base_knowledge))},
        {"role": "assistant", "content": "¡Ok, seguro!"},
        #{"role": "system", "content": "Aplica markdown para resaltar cada uno de las solicitudes y emojis para mejorar el UX de la experiencia"},
        {"role": "user", "content": prompt}
    ]

    # Output
    respuesta = mychatbot(messages)


    return respuesta