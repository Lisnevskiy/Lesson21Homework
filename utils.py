def display_greeting():
    print('Здравствуйте! Напишите, что нужно сделать, по такому шаблону:\n')
    print('|Доставить <кол-во> <что> из <откуда> в <куда>|\n')
    print('Или введите слово "стоп" если захотите остановить программу.')


def show_storage_contents(name, storage: dict):
    print(f'\nВ {name} хранится:\n')

    for key, value in storage.items():
        print(f'{value} {key}')

    print('--------------------------------')


def check_user_request(request):
    user_request_list = request.split(' ')

    if len(user_request_list) != 7:
        return 'Слишком короткий запрос!'

    if user_request_list[1].isdigit() is not True:
        return 'Введите <кол-во> цифрами!'

    elif 'склад' not in user_request_list[4] and 'магазин' not in user_request_list[4]:
        return '<откуда> должно иметь значение "склад" или "магазин"!'

    elif 'склад' not in user_request_list[6] and 'магазин' not in user_request_list[6]:
        return '<куда> должно иметь значение "склад" или "магазин"!'

    elif user_request_list[6] == user_request_list[4]:
        return '<откуда> и <куда> имеют одинаковые значения!'

    return True
