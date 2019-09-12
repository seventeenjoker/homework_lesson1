def ask_user():
    user_answer = ''
    while user_answer != 'хорошо':
        try:
            user_answer = input('Как дела?')
        except KeyboardInterrupt:
            print('Пока!')
            break

def positive_thinking(questions_answers):
    checker = True
    while checker:
        question = input('Давай поговорим!')
        if questions_answers.get(question):
            print(questions_answers[question])
        elif question == 'хватит.':
            print('Пока :)')
            checker = False
        else:
            print('Я не расслышал :()')

questions_answers = {
    'Как дела?': 'Отлично!',
    'Как настроение?': 'Отлично!',
    'Что делаешь?': 'Программирую!'
}

ask_user()
positive_thinking(questions_answers)