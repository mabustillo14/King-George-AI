import mutagen

from ai_audio_model import transcribir_audio
from ai_text_model import hacer_evaluacion, medir_KPI

def duracion_audio(audio_path):
    audio = mutagen.File(audio_path)
    duracion = audio.info.length
    return duracion


def ask_chatbot(context, question, audio):
    duracion = duracion_audio(audio)
    if(duracion >61):
        return ["**Error** - Ups, tu audio es muy largo y no lo pudimos evaluar. Intenta nuevamente", None]
    #KPI = duracion
    transcripcion = transcribir_audio(audio)
    resultado = hacer_evaluacion(context,question, transcripcion)
    KPI = medir_KPI(duracion, transcripcion)
    return [KPI, resultado]
