dic = {
    "Ivan": {"Altura": 45, "Peso": "Gordo", "Belleza": ["Poca", "Mucha"]},
    "Omar": "Tonto",
}

manual = {
    "Tipología": {
        "Monumental": {
            "Monumento Político": ["Palacio", "Sede Gubernamental"],
            "Monumento Publico": ["Arco", "Fontana"],
            "Pregunta": "Qué tipo de monumento es?",
        }
    },
    "Complejidad": None,
}
print(manual["Ivan"])
json_structure = {
    "Monumental": {
        "Monumento político": ["palacio", "sede gubernamental"],
        "Monumento público": ["Arco", "fontana"],
        "Monumento religioso": ["iglesia", "convento"],
    },
    "Paisajística": {
        "Paisaje": ["urbano-arquitectónico"],
        "Paisaje natural": [],
        "Paisaje fluvial": [],
    },
    "Tipológica": {
        "Edificio singular": ["rascacielos", "edificio icónico"],
        "Elemento urbano": ["escalinate", "fuente", "verja"],
        "Infraestructura": ["túnel", "puente", "carretera"],
        "Inmueble": ["edificio normal", "residencial"],
        "Jardines": [],
        "Patrimonio industrial": [],
    },
    "Arte y educación": {
        "Escultura": [],
        "Pintura": [],
        "Arte moderno": [],
        "Educación": ["elemento educativo", "cartela"],
    },
    "Inmaterial": {
        "Escena": [],
        "Espectáculos": [],
        "Eventos": [],
        "Personal": ["selfie", "animales"],
    },
}
