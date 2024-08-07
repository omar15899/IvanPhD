# Primero, vamos a calcular el número de tokens en el texto dado utilizando una herramienta de tokenización.
# Usaremos la biblioteca transformers de Hugging Face para esto.

from transformers import GPT2Tokenizer

# El modelo GPT-4 usa una tokenización similar a la de GPT-3.
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

text = r"""
Contexto: Estoy llevando a cabo un estudio acerca de la percepción del paisaje histórico de Madrid mediante fotos de mis amigos y necesito que analices esta imagen. Eres un experto en análisis de fotografías de tipo paisajístico y cultural. Sabiendo que la imagen ha sido tomada en Madrid y siguiendo tu criterio más objetivo, capaz y profesional, necesito que respondas a las siguientes preguntas: 

{ P1 "Cuál es la característica principal (solo elegir la más representativa) con la que categorizarías a la imagen": 

[ "Palacio", 
"Edificio gubernamental", 
"Fuente pública", 
"Arco de triunfo", 
"Puerta monumental", 
"Iglesia", 
"Varios edificios", 
"Río", 
"Parque", 
"Edificio residencial", 
"Edificio singular", 
"Rascacielos", 
"Escalinata", 
"Verja", 
"Túnel", 
"Puente", 
"Carretera", 
"Escultura", 
"Pintura", 
"Arte moderno", 
"Cartela informativa", 
"Selfie", 
"Retrato a personas", 
"Animales", 
"Espectáculo/evento", 
"Comida/bebida”,
“Tienda/grandes almacenes” ], 

P2 "¿Qué monumentos de Madrid reconoces en la foto? Además del elemento principal de la foto, dime qué otros monumentos aparecen, basándote solo en la información visual de la fotografía y no en otra información externa como ubicaciones cercanas. No menciones monumentos si no estás completamente seguro de cuáles son. Si no hay ningún monumento reconocible di “sin datos” ":

P3 "Siglos de los monumentos que aparecen en la foto en base a tu conocimiento de los mismos (es decir, puedes emplear otra información no visual)": 

[ anterior al 15, 
16, 
17, 
18, 
19, 
20, 
21 ], 

P4 "Atribuye un estilo arquitectónico/artístico al elemento principal y al resto de monumentos que aparecen en la foto. Si sólo aparecen elementos": 

[ "Renacentista", 
"Herreriano", 
"Barroco", 
"Neoclasicismo", 
"Arquitectura del siglo XIX", 
"Arquitectura del siglo XX", 
"Arquitectura del siglo XXI", 
"Sin datos"  ], 

P5 "¿Qué elementos de la siguiente lista aparecen en la foto (pueden ser varios)? Menciona solo los que se perciben visualmente y no mejores la respuesta usando otro tipo de información no visual. Menciona solamente los elementos que se perciben claramente y no menciones elementos si no estás completamente seguro de que están presentes": 

[ "Agua", 
"Animales", 
"Fuente pública", 
"Arco de triunfo", 
"Puerta monumental", 
"Iglesia", 
"Edificio", 
"Escultura", 
"Infraestructura", 
"Mobiliario interior", 
"Persona", 
"Elemento vegetal", 
"Vehículo", 
"Mobiliario urbano" 
"Río", 
"Parque",
"Escalinata", 
"Pintura", 
"Espectáculo/evento", 
"Comida/bebida”,
“Tienda/grandes almacenes” ], 

P6 "¿Cuántos elementos de la lista anterior aparecen?": 

[ "0", 
"1", 
"2", 
"3", 
"4", 
"5", 
"6", 
"7", 
"8", 
"9", 
"10", 
"11", 
"12", 
"13", 
"14", 
"15", 
"16", 
"17", 
"18" ],

P7 "¿Qué materiales de la siguiente lista aparecen en la foto?": 

[ "Piedra", 
"Ladrillo", 
"Metal", 
"Cristal", 
"Madera", 
"Teja", 
"Asfalto" ], 

P8 "¿Es una foto tomada en el exterior?": 

[ "Sí", 
"No" ], 

P9 "Si es una foto tomada en el exterior, ¿está tomada durante el día? Si es una foto tomada en interior puedes decir "sin datos": 

[ "Sí", 
"No", 
"Sin datos" ], 

P10 "Indica cuál es el rango de cada fotografía de entre las siguientes opciones": 

[ "Panorámica", 
"Detalle" ] } 

La respuesta ha de darse en el mismo formato JSON, pero los keys tienen que ser P1,P2,…,PN. Sólo responde en este formato.

"""

# Tokenizamos el texto
tokens = tokenizer.encode(text)

# Contamos el número de tokens
num_tokens = len(tokens)
print(num_tokens)
