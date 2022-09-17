#----------------trivia----------

#añadiendo costantes p
NEGRO = '\033[30m'
ROJO = '\033[31m'
VERDE = '\033[32m'
AMARILLO = '\033[33m'
AZUL = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
BLANCO = '\033[37m'
RESET = '\033[39m'
espacio = "......................................................"
#imports de librerias
import random
import time

print(VERDE + "Bienvenido a mi trivia sobre el senior de los anillos\n" +
      RESET)
print(VERDE + "pondremos a prueba tus conocimientos\n" + RESET)
print(espacio)
name = input(MAGENTA + "\n ingresa tu nombre \n" + RESET)

print(
    VERDE + "\n Hola", name,
    "responde las siguiente preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"
    + RESET)
puntajeInicial = random.randint(0, 11)

comodinAcierto = random.randint(2, 6)
castigoError = random.randint(1, 4)
#lista para acumular puntos
ptsResCor = []
ptsResInc = []
ptsCastigo = []
ptsComodin = []
otros = []
#listas para guardar resultados finales
PuntosJugada = []
respCorrectas = []
resFalsas = []

print(MAGENTA + name, ", tienes ", comodinAcierto,
      " puntos al iniciar la trivia" + RESET)
print(
    AMARILLO +
    "las respuestas correctas suman 10 puntos \nlas respuestas incorrecas resta 5 puntos \notras respuestas restan 1 punto  "
    + RESET)

print(AZUL + "", comodinAcierto,
      " puntos mas por cada respuesta correcta" + RESET)
print(ROJO + "", castigoError,
      " puntos menos por cada respuesta incorrecta" + RESET)
print(espacio)
for x in range(5, 0, -1):
    print(x)
    time.sleep(1)

seguir = True
intentos = 1
print(espacio)
while seguir == True:
    correcto = 0
    falso = 0
    print("intento numero:", intentos)

    #pregunta 01 ------------------------------------------

    ptsResCor.append(puntajeInicial)
    print(
        AZUL +
        "\n 1: ¿como se llama el hobbit que llevo el anillo unico a la  montania del destino, para poder destruirlo? \n"
        + RESET)

    print(CYAN + "\n a: Samsagaz Gamyi \n" + RESET)

    print(CYAN + "\n b: Peregrin Tuk \n" + RESET)

    print(CYAN + "\n c: Meriadoc  Brandigamo \n" + RESET)

    #respuesta correcta
    print(CYAN + "\n d: Frodo Bolsón \n" + RESET)

    respuesta_1 = input("\n Tu respuesta: ").lower()

    while respuesta_1 not in ("a", "b", "c", "d"):
        ptsCastigo.append(castigoError)
        otros.append(1)
        #puntaje =puntaje- 1 - castigoError
        print(ROJO + "pierdes ", castigoError,
              " puntos, como castigo por errror" + RESET)
        print(
            ROJO + "pierdes ", 1,
            " punto, como castigo por digitar una respuesta no establecida" +
            RESET)
        #print(MAGENTA+"puntaje actual = ",puntaje," "+RESET )
        respuesta_1 = input(
            ROJO +
            "\n Debes responder a, b, c, o d. Ingresa nuevamente tu respuesta  "
            + RESET).lower()

    if respuesta_1 == "d":
        ptsResCor.append(10)
        ptsComodin.append(comodinAcierto)
        print(MAGENTA + "Respuesta correcta " + RESET)
        #puntaje = puntaje + 10 + comodinAcierto
        print(CYAN + "ganas", 10,
              " puntos, por responder correctamente" + RESET)
        print(CYAN + "ganas", comodinAcierto,
              " puntos, por el comodin de acierto" + RESET)
        correcto += 1

    else:
        print(ROJO + "respuesta incorrecta" + RESET)
        ptsResInc.append(5)
        ptsCastigo.append(castigoError)
        print(ROJO + "Pierdes", 5,
              " puntos, por responder incorrectamente" + RESET)
        print(ROJO + "Pierdes", castigoError,
              " puntos, como castigo por error" + RESET)
        falso += 1

    time.sleep(3)
    print(espacio)
    #pregunta 02--------------------------------------------------------
    print(
        AZUL +
        "\n 2: ¿cual es el nombre del ENT que salva la vida de pippin y merry  de un orco? \n"
        + RESET)
    #respuesta correcta
    print(CYAN + "\n a: barbol \n" + RESET)

    print(CYAN + "\n b: gandalf \n" + RESET)

    print(CYAN + "\n c: saruman \n" + RESET)

    print(CYAN + "\n d: gollum \n" + RESET)

    respuesta_2 = input("\n Tu respuesta: ").lower()

    while respuesta_2 not in ("a", "b", "c", "d", "x"):
        ptsCastigo.append(castigoError)
        otros.append(1)
        #puntaje =puntaje- 1 - castigoError
        print(ROJO + "pierdes ", castigoError,
              " puntos, como castigo por errror" + RESET)
        print(
            ROJO + "pierdes ", 1,
            " punto, como castigo por digitar una respuesta no establecida" +
            RESET)
        #puntaje = puntaje - 1- castigoError
        #print(MAGENTA+"puntaje actual = ",puntaje,""+RESET)
        respuesta_2 = input(
            ROJO +
            "\n Debes responder a, b, c, o d. Ingresa nuevamente tu respuesta  "
            + RESET).lower()

    if respuesta_2 == "b":
        print(ROJO + "incorrecto " + RESET)
        print(
            AMARILLO + name,
            ", Gandalf es un  maia enviados a la Tierra Media para ayudar  en la lucha contra el «señor oscuro» Sauron"
            + RESET)
        ptsResInc.append(5)
        ptsCastigo.append(castigoError)
        print(ROJO + "Pierdes", 5,
              " puntos, por responder incorrectamente" + RESET)
        print(ROJO + "Pierdes", castigoError,
              " puntos, como castigo por error" + RESET)
        falso += 1
    elif respuesta_2 == "c":
        print(ROJO + "incorrecto " + RESET)
        print(
            AMARILLO + name,
            ", Saruman es el líder de los Istari, magos enviados a la Tierra Media con la intención de vencer a Sauron"
            + RESET)
        ptsResInc.append(5)
        ptsCastigo.append(castigoError)
        print(ROJO + "Pierdes", 5,
              " puntos, por responder incorrectamente" + RESET)
        print(ROJO + "Pierdes", castigoError,
              " puntos, como castigo por error" + RESET)
        falso += 1
    elif respuesta_2 == "d":
        print(ROJO + "incorrecto " + RESET)
        print(
            AMARILLO + name,
            ", gollum fue un hobbit que vivió cerca de 589 años gracias al poder del Anillo Único, que lo desfiguro física y mentalmente"
            + RESET)
        ptsResInc.append(5)
        ptsCastigo.append(castigoError)
        print(ROJO + "Pierdes", 5,
              " puntos, por responder incorrectamente" + RESET)
        print(ROJO + "Pierdes", castigoError,
              " puntos, como castigo por error" + RESET)
        falso += 1
    elif respuesta_2 == "x":
        print(AZUL + "Encontraste la respuesta secreta" + RESET)
        ptsComodin.append(50)
        print(MAGENTA + "ganas", 50,
              " puntos, por encontrar la respuesta secreta" + RESET)
        correcto += 1
    else:
        print(MAGENTA + "muy bien ", name, ", respuesta correcta" + RESET)
        ptsResCor.append(10)
        ptsComodin.append(comodinAcierto)
        print(CYAN + "ganas", 10,
              " puntos, por responder correctamente" + RESET)
        print(CYAN + "ganas", comodinAcierto,
              " puntos, por el comodin de acierto" + RESET)
        correcto += 1

    time.sleep(3)
    print(espacio)
    #pregunta 03 --------------------------------------------------------
    print(AZUL +
          "\n3: Cuantos integrantes Conformaban la comunidad del anillo?\n" +
          RESET)

    #respiesta incorrecta
    print(CYAN + "\n a: 5 \n" + RESET)

    #respuesta menos indicada
    print(CYAN + "\n b: 10 \n" + RESET)

    #respuesta indicada
    print(CYAN + "\n c: 9 \n" + RESET)

    #respuesta disparatada
    print(CYAN + "\n d: 18 \n" + RESET)

    respuesta_3 = input("\n Tu respuesta: ").lower()

    while respuesta_3 not in ("a", "b", "c", "d"):
        ptsCastigo.append(castigoError)
        otros.append(1)
        print(ROJO + "pierdes ", castigoError,
              " puntos, como castigo por errror" + RESET)
        print(
            ROJO + "pierdes ", 1,
            " punto, como castigo por digitar una respuesta no establecida" +
            RESET)

        #puntaje = puntaje - 1- castigoError
        #print(MAGENTA+"puntaje actual = ",puntaje,""+RESET)
        respuesta_3 = input(
            ROJO +
            "\n Debes responder a, b, c, o d. Ingresa nuevamente tu respuesta  \n"
            + RESET).lower()

    if respuesta_3 == "a":
        print(ROJO + name,
              ", tu respuesta es incorrecto, se te restaran 5 puntos " + RESET)
        ptsResInc.append(5)
        ptsCastigo.append(castigoError)
        print(ROJO + "Pierdes", 5,
              " puntos por responder incorrectamente" + RESET)
        print(ROJO + "Pierdes", castigoError,
              " puntos como castigo por error" + RESET)
        falso += 1
    elif respuesta_3 == "b":

        print(ROJO + "respuesta menos indicada", name,
              ", casi aciertas! se te sumaran 5 puntos" + RESET)
        ptsResCor.append(5)
        ptsCastigo.append(castigoError)
        print(AMARILLO + "ganas", 5, " puntos de consuelo" + RESET)
        print(ROJO + "Pierdes", castigoError,
              " puntos, como castigo por error" + RESET)

        falso += 1
    elif respuesta_3 == "d":
        print(ROJO + "respuesta incorrecta, ", name,
              " tu respuesta es muy disparatada\n" + RESET)
        #puntaje /=2
        ptsResInc.append(20)
        ptsCastigo.append(castigoError)
        print(ROJO + "Pierdes", 20,
              " puntos, por responder incorrectamente" + RESET)
        print(ROJO + "Pierdes", castigoError,
              " puntos, como castigo por error" + RESET)
        falso += 1
    else:
        print(AZUL + "muy bien ", name, ", respuesta correcta!" + RESET)
        ptsResCor.append(20)
        ptsComodin.append(comodinAcierto)

        print(CYAN + "ganas", 20,
              " puntos, por responder correctamente" + RESET)
        print(CYAN + "ganas", comodinAcierto,
              " puntos, por el comodin de acierto" + RESET)
        correcto += 1
#pregunta 04 ------------------------------------------
    time.sleep(2)
    print(espacio)
    print(
        AZUL +
        "\n 4: completa la siguiente frase  \n"
        + RESET)
    print(CYAN+"'Tres Anillos para los Reyes Elfos bajo el cielo. Siete para los Señores Enanos en palacios de piedra. Nueve para los Hombres Mortales condenados a morir. Uno ...............'\n"+RESET)

    print(CYAN + "\n a: para el maestro Karin \n" + RESET)

    print(CYAN + "\n b: para la caperocita roja \n" + RESET)
#respuesta correcta
    print(CYAN + "\n c: para el Señor Oscuro.Sauron \n" + RESET)

    
    print(CYAN + "\n d: para la novia \n" + RESET)

    respuesta_4 = input("\n Tu respuesta: ").lower()

    while respuesta_4 not in ("a", "b", "c", "d"):
        ptsCastigo.append(castigoError)
        otros.append(1)
        #puntaje =puntaje- 1 - castigoError
        print(ROJO + "pierdes ", castigoError,
              " puntos, como castigo por errror" + RESET)
        print(
            ROJO + "pierdes ", 1,
            " punto, como castigo por digitar una respuesta no establecida" +
            RESET)
        #print(MAGENTA+"puntaje actual = ",puntaje," "+RESET )
        respuesta_1 = input(
            ROJO +
            "\n Debes responder a, b, c, o d. Ingresa nuevamente tu respuesta  "
            + RESET).lower()

    if respuesta_4 == "c":
        ptsResCor.append(10)
        ptsComodin.append(comodinAcierto)
        print(MAGENTA + "Respuesta correcta " + RESET)
        #puntaje = puntaje + 10 + comodinAcierto
        print(CYAN + "ganas", 10,
              " puntos, por responder correctamente" + RESET)
        print(CYAN + "ganas", comodinAcierto,
              " puntos, por el comodin de acierto" + RESET)
        correcto += 1

    else:
        print(ROJO + "respuesta incorrecta" + RESET)
        ptsResInc.append(5)
        ptsCastigo.append(castigoError)
        print(ROJO + "Pierdes", 5,
              " puntos, por responder incorrectamente" + RESET)
        print(ROJO + "Pierdes", castigoError,
              " puntos, como castigo por error" + RESET)
        falso += 1

    time.sleep(3)
    print(espacio)
  
    for x in range(random.randint(3, 6), 0, -1):
        print(x)
        time.sleep(1)

    ##sumando puntos
    print(AZUL + espacio + RESET)
  
    sumaResCor = sum(ptsResCor)
    print(AZUL + "suma de puntos de respuestas correctas" + RESET)
    print(sumaResCor)

    
    sumaResIncc = sum(ptsResInc)
    print(ROJO + "Suma de puntos de Respuestas incorrectas" + RESET)
    print(sumaResIncc)

    sumaComodin = sum(ptsComodin)
    print(CYAN + "suma puntos comodin" + RESET)
    print(sumaComodin)

    sumaCastigo = sum(ptsCastigo)
    print(AMARILLO + "Suma puntos castigos" + RESET)
    print(sumaCastigo)
  
    SumaOtros = sum(otros)
    print(ROJO + "suma puntaje por responde otra alternativa" + RESET)
    print(SumaOtros)
  
    print(espacio)
  
    puntajeTotal = (sumaResCor + sumaComodin - sumaResIncc - sumaCastigo -
                    SumaOtros)
    print(VERDE + name, ", gracias por jugar,  alcanzaste acumular ",
          puntajeTotal, " puntos" + RESET)
    print(CYAN + "N° de respuestas correctas =", correcto, "" + RESET)
    print(ROJO + "N° de respuestas FALSAS =", falso, "" + RESET)

    print(espacio)

    PuntosJugada.append(puntajeTotal)
    respCorrectas.append(correcto)
    resFalsas.append(falso)

    ptsResCor = []
    ptsResInc = []
    ptsComodin = []
    ptsCastigo = []
    otros = []

    time.sleep(4)

    intentos += 1
    
    time.sleep(2)
    print(ROJO + "¿quieres seguir jugando?" + RESET)
    time.sleep(2)
    print(
        ROJO +
        "ingresa 'si' si quieres seguir jugando\n u otra letra para salir\n" +
        RESET)
    respuesta = input(MAGENTA + "tu respuesta" + RESET).lower()
    if respuesta != "si":
        seguir = False
        print(AZUL + "gracias por jugar\n" + RESET)
        for x in range(0, len(PuntosJugada), 1):
            print(CYAN + "puntaje intento N°", x + 1, "=", PuntosJugada[x],
                  " \n" + RESET)
            time.sleep(1)

            print(CYAN + "Respuestas Correctas intento N°", x + 1, "=",
                  respCorrectas[x], " \n" + RESET)
            print(ROJO + "Respuestas Incorrectas intento N°", x + 1, "=",
                  resFalsas[x], " \n" + RESET)
            time.sleep(1)
            print(espacio)
    print(espacio)