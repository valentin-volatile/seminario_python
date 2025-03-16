import random

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# lista de tuples que tiene pregunta, respuestas posibles e índice de la respuesta correcta (sin repetición)
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

score = 0.0

# El usuario deberá contestar 3 preguntas
for question in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question[0])
    
    for i, answer in enumerate(question[1]):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        
        # Se verifica que la respuesta sea válida
        user_answer = user_answer.strip() #ignoramos trailing o leading spaces
        if(not user_answer.isnumeric() or int(user_answer) > len(question[1])):
            print("Respuesta no válida")
            exit(1)
        
        # Se verifica si la respuesta es correcta
        if int(user_answer)-1 == question[2]:
            print("¡Correcto!")
            score += 1
            break
        else:
            score -= 0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(question[1][question[2]])

    # Se imprime un blanco al final de la pregunta
    print()

print("Puntaje:", score)
