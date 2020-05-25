
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from rest_framework.generics import get_object_or_404

from ...models import *
class Command(BaseCommand):
    # Задаём текст помощи, который будет
    # отображён при выполнении команды
    # python manage.py gencars --help
    help = u'Generate cars. Создание моделей Car со случайным содержанием полей'

    def add_arguments(self, parser):
        # Указываем сколько и каких аргументов принимает команда.
        # В данном случае, nargs='+' - минимум один аргумент, либо список.
        parser.add_argument('-e', '--enterprise_id', nargs='+', type=int,
                            help=u'Для какого предприятия(либо список enterprise_id через пробел)')
        # Вторым аргументом передаем число
        parser.add_argument('-n', '--number', type=int, help=u'Количество создаваемых Car')

    def handle(self, *args, **options):
        # Получаем аргументы:
        enterprise_id = options['enterprise_id']
        number_cars = options['number']
        # enterprise_id - возможно список, по этому итерируемся сначала по нему.
        for enterprise in enterprise_id:
            of_enterprise = get_object_or_404(Enterprise.objects.all(), pk=enterprise)
            # Создаем число машинок = number_cars
            for i in range(number_cars):
                brand = get_random_string() # случайная генерация строки для поля Car
                model = get_random_string()
                color = get_random_string()
                # Непосредственно, создание модели типа Car, с указанными полями
                Car.objects.create(brand=brand, model=model, color=color, fuel_util=10, of_enterprise=of_enterprise)

        self.stdout.write('Successfully created {0} cars!'.format(number_cars))
        self.stdout.write('Current list cars: {}'.format(list(Car.objects.all())))
