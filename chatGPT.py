import openai


def titulo():
    print("*-------------------------------- BIENVENIDO A TU PROPIO ASISTENTE PERSONAL -----------------------------*")
    print('*    REGLAS:                                                                                             *')
    print('*\t- Puedes preguntar o pedir lo que quieras, mientras no sea algo ofensivo o de indole sexual.     *')
    print('*\t- No puedes pedirme datos personales.                                                            *')
    print('*\t- Solo tengo información del internet hasta 2021.                                                *')
    print('*--------------------------------------------------------------------------------------------------------*')


def chat_gpt():
    openai.api_key = 'aca va tu api key que la sacas de tu cuenta de openai'
    titulo()
    while True:
        my_prompt = input("\nchat me: ")

        if my_prompt == 'exit':
            break

        completion = openai.Completion.create(
            engine='text-davinci-003',
            prompt=my_prompt,
            max_tokens=4000
        )

        print(completion.choices[0].text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chat_gpt()
