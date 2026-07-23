from itertools import product

class Materia:
    def __init__(self, nombre, grupo, profe, clases):
        self.nombre = nombre
        self.grupo = grupo
        self.profe = profe
        self.clases = clases



def DatosMaterias():
    T1 = "14:30 - 16:00"
    T2 = "16:00 - 17:30"
    T3 = "17:30 - 19:00"
    T4 = "19:00 - 20:30"
    T5 = "20:30 - 22:00"
    L = "Lunes"
    M = "Martes"
    Mi = "Miércoles"
    J = "Jueves"
    V = "Viernes"

    Electro1 = Materia("Electroacústica", "V1", "FRANCO PEREZ RICARDO ANDRES", {L:T5, Mi:T5, J:T5})
    Electro2 = Materia("Electroacústica", "V2", "FRANCO PEREZ RICARDO ANDRES", {L:T2, Mi:T2, J:T2})
    Electro4 = Materia("Electroacústica", "V4", "SANCHEZ SANCHEZ MARCIAL MARGARITO", {L:T5, Mi:T5, V:T4})
    Electro5 = Materia("Electroacústica", "V5", "CONTRERAS ESTRADA JOAQUIN", {L:T1, Mi:T1, V:T1})
    Electro6 = Materia("Electroacústica", "V6", "DE LA CRUZ CARTAS XUNAXI GUADALUPE", {L:T2, Mi:T2, V:T1})

    Espacio1 = Materia("Espacio", "V1", "QUINTANA ORTEGA EDGAR", {L:T4, M:T4, J:T4})
    Espacio2 = Materia("Espacio", "V2", "QUINTANA ORTEGA EDGAR", {L:T5, M:T5, J:T5})
    Espacio3 = Materia("Espacio", "V3", "BENITO HERNANDEZ JUAN ELOY", {L:T2, M:T2, J:T2})
    Espacio4 = Materia("Espacio", "V4", "BENITO HERNANDEZ JUAN ELOY", {L:T3, M:T3, Mi:T3})
    Espacio5 = Materia("Espacio", "V5", "LEAL ENRIQUEZ ERIK", {L:T4, M:T4, Mi:T4})
    Espacio6 = Materia("Espacio", "V6", "NOVOA COLIN JUAN FRANCISCO", {L:T4, M:T4, Mi:T4})

    Genera1 = Materia("Generación", "V1", "MORA AROSTICO JULIO CESAR", {L:T3, Mi:T3})
    Genera2 = Materia("Generación", "V2", "MORA AROSTICO JULIO CESAR", {L:T4, Mi:T4})
    Genera3 = Materia("Generación", "V3", "MORA AROSTICO JULIO CESAR", {L:T5, Mi:T5})
    Genera4 = Materia("Generación", "V4", "MONTENEGRO SUSTAITA HILARIO G", {J:T3, V:T3})
    Genera5 = Materia("Generación", "V5", "MONTENEGRO SUSTAITA HILARIO G", {J:T4, V:T4})
    Genera6 = Materia("Generación", "V6", "MORA AROSTICO JULIO CESAR", {M:T1, J:T4})

    Huma1 = Materia("Humanidades", "V1", "MEZA PORTILLO ERASTO", {L:T2, M:T2})
    Huma2 = Materia("Humanidades", "V2", "MEZA PORTILLO ERASTO", {L:T3, M:T3})
    Huma3 = Materia("Humanidades", "V3", "MEZA PORTILLO ERASTO", {L:T4, M:T4})
    Huma4 = Materia("Humanidades", "V4", "MEZA PORTILLO ERASTO", {Mi:T2, V:T2})
    Huma5 = Materia("Humanidades", "V5", "MEZA PORTILLO ERASTO", {Mi:T3, V:T3})

    Micro1 = Materia("Microcontroladores", "V1", "GABRIEL BALDERAS EDUARDO", {Mi:T2, J:T2, V:T2})
    Micro2 = Materia("Microcontroladores", "V2", "GABRIEL BALDERAS EDUARDO", {Mi:T3, J:T3, V:T3})
    Micro3 = Materia("Microcontroladores", "V3", "LOPEZ MACEDO RICARDO", {Mi:T4, J:T4, V:T4})
    Micro4 = Materia("Microcontroladores", "V4", "LOPEZ MACEDO RICARDO", {M:T5, J:T5, V:T5})
    Micro5 = Materia("Microcontroladores", "V5", "LOPEZ HERNANDEZ JOSE ANTONIO", {M:T2, J:T2, V:T2})
    Micro6 = Materia("Microcontroladores", "V6", "RAYA BAHENA JUAN MARTIN", {M:T2, J:T2, V:T2})

    Proce1 = Materia("Procesamiento", "V1", "UTRERA GOMEZ CUAUHTEMOC", {M:T5, Mi:T4, V:T4})
    Proce2 = Materia("Procesamiento", "V2", "PEREZ MACIAS CESAR ISRAEL", {M:T4, J:T4, V:T4})
    Proce3 = Materia("Procesamiento", "V3", "PEREZ MACIAS CESAR ISRAEL", {M:T5, J:T5, V:T5})
    Proce4 = Materia("Procesamiento", "V4", "CARDENAS GONZALEZ GERARDO", {L:T2, M:T2, J:T2})
    Proce5 = Materia("Procesamiento", "V5", "CARDENAS GONZALEZ GERARDO", {L:T3, M:T3, J:T3})
    Proce6 = Materia("Procesamiento", "V6", "RODRIGUEZ SALDAÑA DANIEL", {L:T3, M:T3, J:T3})

    Red1 = Materia("Redes", "V1", "CAMACHO GONZALEZ MARCO ANTONIO", {M:T3, J:T3, V:T3})
    Red2 = Materia("Redes", "V2", "NIEVES GODINEZ JULIO CESAR", {M:T1, Mi:T1, V:T1})
    Red3 = Materia("Redes", "V3", "OLEA RAMIREZ JOSE IRENE", {M:T3, Mi:T3, V:T3})
    Red4 = Materia("Redes", "V4", "CAMACHO GONZALEZ MARCO ANTONIO", {L:T4, M:T4, Mi:T4})
    Red5 = Materia("Redes", "V5", "CAMACHO GONZALEZ MARCO ANTONIO", {L:T5, M:T5, Mi:T5})
    Red6 = Materia("Redes", "V6", "DELGADO PÉREZ JULIO", {L:T1, Mi:T1, J:T1})
    

    OpcionesElectro = [Electro1, Electro2, Electro4, Electro5, Electro6]
    OpcionesEspacio = [Espacio1, Espacio2, Espacio3, Espacio4, Espacio5, Espacio6]
    OpcionesGenera = [Genera1, Genera2, Genera3, Genera4, Genera5, Genera6]
    OpcionesHuma = [Huma1, Huma2, Huma3, Huma4, Huma5]
    OpcionesMicro = [Micro1, Micro2, Micro3, Micro4, Micro5, Micro6]
    OpcionesProce = [Proce1, Proce2, Proce3, Proce4, Proce5, Proce6]
    OpcionesRed = [Red1, Red2, Red3, Red4, Red5, Red6]

    return OpcionesElectro, OpcionesEspacio, OpcionesGenera, OpcionesHuma, OpcionesMicro, OpcionesProce, OpcionesRed



def Traslape(Sesion1, Sesion2):
    if Sesion1 == Sesion2:
        return True
    else: 
        return False
    

def MateriasTraslapadas(materia1, materia2):
    for dia in materia1.clases:
        if dia in materia2.clases:
            sesion1 = materia1.clases[dia]
            sesion2 = materia2.clases[dia]

            if Traslape(sesion1, sesion2):
                return True

    return False


def HorarioValido(horario):
    for i in range(len(horario)):
        for j in range(i + 1, len(horario)):
            if MateriasTraslapadas(horario[i], horario[j]):
                return False

    return True



def NombreCorto(materia):
    nombres_cortos = {
        "Electroacústica": "Electro",
        "Espacio": "Espacio",
        "Generación": "Proyectos",
        "Humanidades": "Huma",
        "Microcontroladores": "Micro",
        "Procesamiento": "PDS",
        "Redes": "Redes"
    }

    nombre = nombres_cortos.get(materia.nombre, materia.nombre)
    return nombre + " " + materia.grupo



def MostrarHorarioBonito(horario):
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    bloques = [
        "14:30 - 16:00",
        "16:00 - 17:30",
        "17:30 - 19:00",
        "19:00 - 20:30",
        "20:30 - 22:00"
    ]

    tabla = {}

    for bloque in bloques:
        tabla[bloque] = {}

        for dia in dias:
            tabla[bloque][dia] = ""

    for materia in horario:
        for dia, bloque in materia.clases.items():
            tabla[bloque][dia] = NombreCorto(materia)

    ancho = 16

    print()
    print("Horario semanal")
    print("-" * 95)

    encabezado = "Bloque".ljust(18)

    for dia in dias:
        encabezado += dia.center(ancho)

    print(encabezado)
    print("-" * 95)

    for bloque in bloques:
        fila = bloque.ljust(18)

        for dia in dias:
            fila += tabla[bloque][dia].center(ancho)

        print(fila)

    print("-" * 95)



preferencias = {
    ("Electroacústica", "FRANCO PEREZ RICARDO ANDRES"): 4,
    ("Electroacústica", "SANCHEZ SANCHEZ MARCIAL MARGARITO"): 4,
    ("Electroacústica", "CONTRERAS ESTRADA JOAQUIN"): 4,
    ("Electroacústica", "DE LA CRUZ CARTAS XUNAXI GUADALUPE"): 5,
    ("Espacio", "QUINTANA ORTEGA EDGAR"): 3,
    ("Espacio", "BENITO HERNANDEZ JUAN ELOY"): 4,
    ("Espacio", "LEAL ENRIQUEZ ERIK"): 4,
    ("Espacio", "NOVOA COLIN JUAN FRANCISCO"): 4,
    ("Generación", "MORA AROSTICO JULIO CESAR"): 4,
    ("Generación", "MONTENEGRO SUSTAITA HILARIO G"): 5,
    ("Humanidades", "MEZA PORTILLO ERASTO"): 3,
    ("Microcontroladores", "GABRIEL BALDERAS EDUARDO"): 2,
    ("Microcontroladores", "LOPEZ MACEDO RICARDO"): 2,
    ("Microcontroladores", "LOPEZ HERNANDEZ JOSE ANTONIO"): 4,
    ("Microcontroladores", "RAYA BAHENA JUAN MARTIN"): 4,
    ("Procesamiento", "UTRERA GOMEZ CUAUHTEMOC"): 4,
    ("Procesamiento", "PEREZ MACIAS CESAR ISRAEL"): 4,
    ("Procesamiento", "CARDENAS GONZALEZ GERARDO"): 4,
    ("Procesamiento", "RODRIGUEZ SALDAÑA DANIEL"): 4,
    ("Redes", "CAMACHO GONZALEZ MARCO ANTONIO"): 2,
    ("Redes", "NIEVES GODINEZ JULIO CESAR"): 4,
    ("Redes", "OLEA RAMIREZ JOSE IRENE"): 3,
    ("Redes", "DELGADO PÉREZ JULIO"): 4,
}



def PuntajeHorario(horario):
    puntaje = 0

    for materia in horario:
        clave = (materia.nombre, materia.profe)

        if clave in preferencias:
            puntaje += preferencias[clave]

    return puntaje


opciones = DatosMaterias()

horarios_validos = []

for combinacion in product(*opciones):
    if HorarioValido(combinacion):
        horarios_validos.append(combinacion)

print("Horarios válidos encontrados:", len(horarios_validos))

horarios_validos.sort(key=PuntajeHorario, reverse=True)

for numero, horario in enumerate(horarios_validos[:10], start=1):
    print()
    print("=" * 95)
    print("HORARIO", numero)
    print("Puntaje:", PuntajeHorario(horario))
    print("=" * 95)

    MostrarHorarioBonito(horario)

    print()
    print("Detalle de profesores:")
    print("--------------------")

    for materia in horario:
        print(materia.nombre, materia.grupo, "-", materia.profe)











