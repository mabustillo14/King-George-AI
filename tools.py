import mutagen

from ai_audio_model import transcribir_audio
from ai_text_model import hacer_evaluacion #, medir_KPI

def duracion_audio(audio_path):
    audio = mutagen.File(audio_path)
    duracion = audio.info.length
    return duracion


def ask_chatbot(context, question, audio):
    transcripcion = transcribir_audio(audio)
    resultado = transcripcion
    KPI = duracion_audio(audio)
    resultado = hacer_evaluacion(context,question, transcripcion)
    #KPI = medir_KPI(duracion, transcripcion)
    return [KPI, resultado]
