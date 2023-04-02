from classes.request import Request
from classes.shop import Shop
from classes.store import Store
from utils import check_user_request, show_storage_contents, display_greeting


def main():
    display_greeting()

    while True:
        show_storage_contents('склад', store.get_items())
        show_storage_contents('магазин', shop.get_items())

        user_input = input('Введите ваш запрос здесь --> ')
        if user_input.lower() in ('стоп', 'stop'):
            break

        # Проверка запроса пользователя на валидность:
        check_user_input = check_user_request(user_input)
        if check_user_input is not True:
            print(check_user_input)
            continue

        user_request = Request(user_input)

        if user_request.from_ == 'склад':
            response = store.remove(user_request.product, user_request.amount)
            if response is not True:
                print(response)
                continue
            else:
                print('Нужное количество есть на складе')
                print(f'Курьер забрал {user_request.amount} {user_request.product} со склада')
                print(f'Курьер везет {user_request.amount} {user_request.product} со склада в магазин')

            response = shop.add(user_request.product, user_request.amount)
            if response is not True:
                print(response)
                store.add(user_request.product, user_request.amount)
                print(f'Курьер вернул {user_request.amount} {user_request.product} на склад')
                continue
            else:
                print(f'Курьер доставил {user_request.amount} {user_request.product} в магазин')

        if user_request.from_ == 'магазин':
            response = shop.remove(user_request.product, user_request.amount)
            if response is not True:
                print(response)
                continue
            else:
                print('Нужное количество есть в магазине')
                print(f'Курьер забрал {user_request.amount} {user_request.product} из магазина')
                print(f'Курьер везет {user_request.amount} {user_request.product} из магазина в склад')

            response = store.add(user_request.product, user_request.amount)
            if response is not True:
                print(response)
                shop.add(user_request.product, user_request.amount)
                print(f'Курьер вернул {user_request.amount} {user_request.product} в магазин')
            else:
                print(f'Курьер доставил {user_request.amount} {user_request.product} в склад')
                print(store.get_free_space())

        print('********************************')


if __name__ == '__main__':
    shop = Shop()
    shop.add('торт', 5)
    shop.add('печенье', 1)
    shop.add('сок', 4)
    shop.add('кола', 2)

    store = Store()
    store.add('халва', 20)
    store.add('мороженное', 20)
    store.add('шоколад', 20)

    main()
