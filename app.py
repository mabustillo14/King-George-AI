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

# Inputs
context = gr.Textbox(label="1) Carga el link de la webpage de la compañía")
question = gr.Textbox(label="2) Carga la pregunta")
audio = gr.Audio(label="3) Graba tu respuesta", source="microphone", type="filepath")

# Outputs
KPI = gr.Textbox(label="Algunas métricas importantes de tu respuesta")
resultado = gr.Textbox(label="Recomendaciones")

gui = gr.Interface(
    fn=check_inputs, 
    inputs=[context, question, audio], 
    outputs=[KPI, resultado],
    description = description,
    theme=gr.themes.Soft()
)

gui.launch()