from rest_framework import generics, request
from rest_framework.generics import get_object_or_404, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from .serialazers import CarSerializer, EnterpriseSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # миксин для доступа аутентифицированным пользователям
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from ..models import Car, Enterprise, User, Manager
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *

"""
class CarListView(LoginRequiredMixin,  generics.ListAPIView):
    # визуализатор Llist для модели Car
    serializer_class = CarSerializer
    def get_queryset(self):
        # переопределяем родительский метод для запроса из БД с фильтром для наших условий
        user_name = self.request.user.username
        list_car = Car.objects.all()
        if user_name != 'admin':
            enterprise = Enterprise.objects.get(manager__username__contains=user_name)
            list_car = Car.objects.filter(of_enterprise=enterprise)
        return list_car

    def get(self, request):
        # переопределяем родительский метод для получения запроса GET
        queryset = self.get_queryset()
        serializer = CarSerializer(queryset, many=True)
        return Response({"cars": serializer.data})

    def post(self, request):
        # метод POST для создания новой Car.
        car = request.data.get('new_car') # получаем пользовательские данные из запроса по ключю "car"
        serializer = CarSerializer(data=car)
        # сериалайзер, как воод-вывод для взаимодействия с моделью Car. (создание)
        if serializer.is_valid(raise_exception=True): # проверка валидности данных из запроса с полями модели.
            car_saved = serializer.save()
        return Response({"success": "Car '{}' created successfully".format(car_saved)})

    def put(self, request):
        # метод PUT для обновления полей Car.
        car_id = request.data.get('id', None) # получаем из запроса id автомобиля
        saved = get_object_or_404(Car.objects.all(), pk=car_id) # проверяем есть ли авто с указанным id в БД если есть,
        # то получаем экземпляр записи по id, иначе ошибка 404
        data = request.data.get('car') # обращаемся в данные запроса (JSON cловарь, по ключу 'car'), эти данные будут
        # перезаписаны в БД.
        serializer = CarSerializer(instance=saved, data=data, partial=True) # перезаписываем в экземпляр saved,
        # данные data
        if serializer.is_valid(raise_exception=True):
            car_saved = serializer.save()
        return Response({"success": "Car '{}' updated successfully".format(car_saved)})

    def delete(self, request):
        car_id = request.data.get('id', None)  # получаем из запроса id автомобиля
        car_to_del = get_object_or_404(Car.objects.all(), pk=car_id)
        car_to_del.delete()
        return Response({"message": "Car with id `{}` has been deleted.".format(car_id)}, status=204)
    raise_exception = True  # переопределение поля исключения, в случае не аутентифицированного пользователя
"""
class CarView(LoginRequiredMixin, ListCreateAPIView):
    # представление для списка авто с методами create и get
    serializer_class = CarSerializer
    pagination_class = LimitOffsetPagination
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'UIcars.html'
    def get_queryset(self):
        # переопределяем родительский метод для запроса из БД с фильтром для наших условий
        user_name = self.request.user.username
        list_car = Car.objects.all()
        if user_name != 'admin':
            enterprise = Enterprise.objects.get(manager__username__contains=user_name)
            list_car = Car.objects.filter(of_enterprise=enterprise)
        return list_car
    queryset = get_queryset

    def get(self, request):
        # переопределяем родительский метод для получения запроса GET
        queryset = self.get_queryset()
        serializer = CarSerializer(queryset, many=True)
        paginator = Paginator(queryset, 8)
        page = request.GET.get('page')
        #page = self.paginate_queryset(queryset) # формируем данные для отображения на одной странице
        """
        if page is not None:
            serializer = CarSerializer(page, many=True) # сериализуем данные page
            result = self.get_paginated_response(serializer.data)
            return Response(locals())
        """
        try:
            cars = paginator.page(page)
        except PageNotAnInteger:
            # Если страница не является целым числом, поставим первую страницу
            cars = paginator.page(1)
        except EmptyPage:
            # Если страница больше максимальной, доставить последнюю страницу результатов
            cars = paginator.page(paginator.num_pages)

        return Response({'result': cars})

    def create(self, serializer):
        # переопределяем родительский метод для получения запроса POST
        car = self.request.data  # получаем данные из запроса
        serializer = CarSerializer(data=car)
        # сериалайзер, как воод-вывод для взаимодействия с моделью Car. (создание)
        if serializer.is_valid(raise_exception=True): # проверка валидности данных из запроса с полями модели.
            car_create = serializer.save()
        return Response({"success": "Car '{}' created successfully".format(car_create)})
    raise_exception = True

class EditCarView(LoginRequiredMixin, RetrieveUpdateDestroyAPIView):
    # представление для конкретной машинки по указанному pk в url
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'UIeditCar.html'
    form_class = CarEditForm
    http_method_names = [u'get', u'post', u'put', u'patch', u'delete', u'head', u'options', u'trace']

    def post(self, request, *args, **kwargs):
        # делаем обработчик для POST запросов. Внутри POST запроса извлекаем скрытое поле '_method' по значению
        # которого вызываем соответствующий функционал из текущего класса. Также извлекаем id из тела запроса.
        if request.POST.get('_method') == 'DELETE':
            self.delete(self.request, int(self.request.POST.get('id')))
        elif request.POST.get('_method') == 'PATH':
            self.path(self.request, int(self.request.POST.get('id')))
        return Response(locals())

    def get_queryset(self):
        # переопределяем родительский метод для запроса из БД с фильтром для наших условий
        user_name = self.request.user.username
        list_car = Car.objects.all()
        if user_name != 'admin':
            enterprise = Enterprise.objects.get(manager__username__contains=user_name)
            list_car = Car.objects.filter(of_enterprise=enterprise)
        return list_car

    def get(self,request, pk):
        return Response(locals())

    def delete(self, request, pk):
        # переопределяем родительский метод для удаления.
        car_id = pk  # получаем id автомобиля из url
        car_to_del = get_object_or_404(self.get_queryset(), pk=car_id)
        car_to_del.delete()
        return Response({"message": "Car with id `{}` has been deleted.".format(car_id)}, status=204)


    def path(self, request, pk):
        # метод PUT для обновления полей Car.
        car_id = pk # получаем id автомобиля из url
        #car_id = request.POST.get("id")
        saved = get_object_or_404(self.get_queryset(), pk=car_id) # проверяем есть ли авто с указанным id в БД если есть,
        # то получаем экземпляр записи по id, иначе ошибка 404
        data = request.data  # данные из переданного в запросе словаря.
        serializer = CarSerializer(instance=saved, data=data, partial=True) # перезаписываем в экземпляр saved,
        # данные data
        if serializer.is_valid(raise_exception=True):
            car_saved = serializer.save()
        return Response({"success": "Car '{}' updated successfully".format(car_saved)})

    serializer_class = CarSerializer
    queryset = get_queryset
    raise_exception = True


class EnterpriseView(LoginRequiredMixin, ListCreateAPIView):
    serializer_class = EnterpriseSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'UIenterprise.html'
    #template_name = 'index.html'
    def get_queryset(self):
        # переопределяем родительский метод для запроса из БД с фильтром для наших условий
        user_name = self.request.user.username
        list_enterprise = Enterprise.objects.all()
        if user_name != 'admin':
            #enterprise = Enterprise.objects.get()

            list_enterprise = Enterprise.objects.filter(manager__username__contains=user_name)
        return list_enterprise
    queryset = get_queryset

    def get(self, request):
        # переопределяем родительский метод для получения запроса GET
        queryset = self.get_queryset()
        serializer = EnterpriseSerializer(queryset, many=True)
        return Response({'result': serializer.data})

    raise_exception = True

class CarDetailView(LoginRequiredMixin, generics.ListAPIView, ListModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    raise_exception = True  # переопределение поля исключения, в случае не аутентифицированного пользователя
