import gradio as gr
from tools import ask_chatbot

def check_inputs(context, question, audio):
    if(audio != None and context !="" and question !="" ):
        respuesta = ask_chatbot(context, question, audio)
        return respuesta[0], respuesta[1]
    else:
        return "!Ups, hubo un Error! - Nos hacen falta información para poder ayudarte", None


# Descripción del Header
description = """
<center><h1><b>King George.ai 👑 </b></h1>
<center><h2><b>Análisis inteligente para Call Centers 🗣️💡 </b></h2>
Simplemente carga respuestas a ciertas preguntas clave y obtén conclusiones detalladas de tu rendimiento.
</center>
"""

# Descripción del Footer
article = """
<br>
<b>¿Por qué elegirnos?</b>
<br><b>King George AI  👑</b>, tu aliado inteligente para mejorar tus habilidades comunicativas 💯. <br>Hacemos análisis de tus respuestas ante preguntas de clientes 🔍 y te damos feedback para mejorar tu potencial 🙌.
<br>Descubre el poder de la inteligencia artificial aplicada a potenciar los Call Centers.🤖💡
"""


# Inputs
context = gr.Textbox(label="1) Dame información de la compañía a quien das soporte 🔗")
question = gr.Textbox(label="2) Ingresa la pregunta del cliente ❓")
audio = gr.Audio(label="3) Graba tu respuesta (máximo 1 minuto) 🎵", source="microphone", type="filepath")

# Outputs
KPI = gr.Textbox(label="Métricas importantes de tu respuesta 🔔")
resultado = gr.Textbox(label="Feedback 💡")

gui = gr.Interface(
    fn=check_inputs, 
    inputs=[context, question, audio], 
    outputs=[KPI, resultado],
    description = description,
    article = article,
    theme=gr.themes.Soft()
)

gui.launch()