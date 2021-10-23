import aiml
import unidecode


def remove_diacritic(text):
    return unidecode.unidecode(text)


k = aiml.Kernel()
k.learn("przywitania.aiml")
k.learn("pizza.aiml")
k.learn("pozegnania.aiml")
while True:
    input_bytes = input("> ")
    input_text = remove_diacritic(input_bytes)
    if input_text == "koniec":
        exit()
    print(k.respond(input_text))
