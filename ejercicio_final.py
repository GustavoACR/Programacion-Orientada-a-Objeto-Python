# from textblob import TextBlob

# class AnalizadorDeSentimintos:
#     def analizar_sentimiento(self, texto):
#         analisis = TextBlob(texto)
#         if analisis.sentiment.polarity > 0:
#             return "Positivo"
#         elif analisis.sentiment.polarity == 0:
#             return "Neutral"
#         else:
#             return "Negativo"
        
# analizador = AnalizadorDeSentimintos()

# resultado = analizador.analizar_sentimiento("Hello i hate all this")
# print(resultado)

import openai 

openai.api_key = "api-key"
system_rol = ''' has de cuenta que eres un analizador de sentimientos.
yo te paso sentimientos y tu analizas el sentimiento de los mensajes y me das una respuesta
 con al menos 3 caracteres y como maximo 4 caracteres SOLO RESPUESTAS NUMERICAS, donde -1
 es negatividad maxima, 0 es neutral y 1 es positividad maxima. (puedes responder
 solo con ints y floats)'''
 
mensajes = [{"role": "system", "content": system_rol}]

class AnalizadorDeSentimintos:
    def analizar_sentimientos(self, polaridad):
        if polaridad > -0.7 and polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo" + "\x1b[0;37m"
        elif polaridad > -0.3 and polaridad <= -0.1:
            return "\x1b[1;31m" + "Algo negativo" + "\x1b[0;37m"
        elif polaridad >= -0.1 and polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[0;37m"
        elif polaridad > 0.1 and polaridad <= 0.4:
            return "\x1b[1;32m" + "Algo positivo" + "\x1b[0;37m"
        elif polaridad > 0.4 and polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo" + "\x1b[0;37m"
        elif polaridad > 0.9:
            return "\x1b[1;32m" + "Muy positivo" + "\x1b[0;37m"
        else:
            return "\x1b[1;31m" + "Muy negativo" + "\x1b[0;37m"
        
analyzer = AnalizadorDeSentimintos()

while True:
    user_prompt = input("\x1b[1;33m" + "\nDi algo: " + "\x1b[0;37m")
    mensajes.append({"role": "user", "content": user_prompt})

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 100
    )
    
    respuesta = completion.choices[0].message.content
    mensajes.append({"role": "assistant", "content": respuesta})

    sentimiento = analyzer.analizar_sentimientos(float(respuesta))
    print(sentimiento)
    
