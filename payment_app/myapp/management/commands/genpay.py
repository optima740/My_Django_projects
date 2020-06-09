from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from rest_framework.generics import get_object_or_404

from ...models import *
import random
class Command(BaseCommand):
    # Задаём текст помощи, который будет
    # отображён при выполнении команды
    # python manage.py genpay --help
    help = u'Generate pays. Создание моделей Pay со случайным содержанием полей'

    def add_arguments(self, parser):
        # Указываем сколько и каких аргументов принимает команда.
        # В данном случае, nargs='+' - минимум один аргумент, либо список.
        parser.add_argument('-u', '--user_id', nargs='+', type=int,
                            help=u'Для какого пользователя(либо список user_id через пробел)')
        # Вторым аргументом передаем число
        parser.add_argument('-n', '--number', type=int, help=u'Количество создаваемых Pay')

    def handle(self, *args, **options):
        # Получаем аргументы:
        user_id = options['user_id']
        number_pays = options['number']
        # user_id - возможно список, по этому итерируемся сначала по нему.
        for user in user_id:
            of_user = get_object_or_404(Customer.objects.all(), pk=user)
            # Создаем число платежей = number_pays
            for i in range(number_pays):
                # случайная генерация строки для поля Pay
                payment_summ = random.randint(0, 100000)
                # Непосредственно, создание модели типа Car, с указанными полями
                Pay.objects.create(author=of_user, payment_summ=payment_summ)

        self.stdout.write('Successfully created {0} pays!'.format(number_pays))
        #self.stdout.write('Current list pays: {}'.format(list(Pay.objects.all())))
