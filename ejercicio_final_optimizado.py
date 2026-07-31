import openai 

openai.api_key = "api-key"
system_rol = ''' has de cuenta que eres un analizador de sentimientos.
yo te paso sentimientos y tu analizas el sentimiento de los mensajes y me das una respuesta
 con al menos 3 caracteres y como maximo 4 caracteres SOLO RESPUESTAS NUMERICAS, donde -1
 es negatividad maxima, 0 es neutral y 1 es positividad maxima. (puedes responder
 solo con ints y floats)'''
 
mensajes = [{"role": "system", "content": system_rol}]

class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.nombre)

class AnalizadorDeSentimintos:
    def __init__(self, rangos):
        self.rangos = rangos
        
    def analizar_sentimientos(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        return Sentimiento("Muy negativo", "31")
        
rangos = [
    ((-0.6, -0.3), Sentimiento("negativo", "31")),
    ((-0.3, -0.1), Sentimiento("algo negativo", "31")),
    ((-0.1, 0.1), Sentimiento("neutral", "33")),
    ((0.1, 0.4), Sentimiento("algo positivo", "32")),
    ((0.4, 0.9), Sentimiento("positivo", "32")),
    ((0.9, 1.0), Sentimiento("muy positivo", "32")),
]
        
analyzer = AnalizadorDeSentimintos(rangos)

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
    