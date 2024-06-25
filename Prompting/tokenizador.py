# Primero, vamos a calcular el número de tokens en el texto dado utilizando una herramienta de tokenización.
# Usaremos la biblioteca transformers de Hugging Face para esto.

from transformers import GPT2Tokenizer

# El modelo GPT-4 usa una tokenización similar a la de GPT-3.
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

text = """
{ "P1": "Iglesia", "P2": [ "Arco", "Columna", "Cornisa", "Escultura", "Fachada", "Persona", "Puerta", "Ventana","Elemento vegetal", "Edificio" ], "P3": "No", "P4": "10", "P5": [ "Piedra", "Ladrillo", "Metal", "Teja" ], "P6": "Sí", "P7":"Sí", "P8": "Medio" }

"""

# Tokenizamos el texto
tokens = tokenizer.encode(text)

# Contamos el número de tokens
num_tokens = len(tokens)
print(num_tokens)
