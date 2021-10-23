import aiml
import unidecode


def remove_diacritic(text):
    return unidecode.unidecode(text)


k = aiml.Kernel()
k.learn("przywitania.aiml")
k.learn("pizza.aiml")
k.learn("zmiesem.aiml")
k.learn("pizzabezmiesa.aiml")
k.learn("pozegnania.aiml")
k.learn("zakonczenie_zamowienia.aiml")
while True:
    input_bytes = input("> ")
    input_text = remove_diacritic(input_bytes)
    output_text = k.respond(input_text)
    print(output_text)
    if output_text[-12:] == "Do widzenia!":
        exit()
