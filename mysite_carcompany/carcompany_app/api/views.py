from rest_framework import generics, request
from rest_framework.generics import get_object_or_404, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from .serialazers import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # миксин для доступа аутентифицированным пользователям
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from ..models import Car, Enterprise, User, Manager
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
from django.core.files import File

class CarView(LoginRequiredMixin, ListCreateAPIView):
    # представление для списка авто с методами create и get
    serializer_class = CarSerializer
    pagination_class = LimitOffsetPagination
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'UIcars.html'

    def get_queryset(self):
        # переопределяем родительский метод для запроса из БД с фильтром для наших условий
        user_name = self.request.user.username # получаем данные о имени пользователя из request
        list_car = Car.objects.all() # формируем список всех автомобилей
        if user_name != 'admin':
            enterprise = Enterprise.objects.get(manager__username__contains=user_name) # получаем предприятие по пользователю
            list_car = Car.objects.filter(of_enterprise=enterprise) # получаем список авто по конкретному предприятию
            tz = self.get_time_zone() # получаем таймзону из предприятия текущего менеджера
            for car in list_car: # проходимся по всем автомобилям из списка запроса
                car_of_db = Car.objects.get(id=car.id) # получаем из БД  машину по id
                datatime_of_db = car_of_db.date_of_buy # получаем из поля значение даты и времени покупки машины
                datatime_tz = datatime_of_db.replace(tzinfo=tz) # корректировка даты и времени относительно другой tz
                car.date_of_buy = datatime_tz # записываем откорректированное время в список для отображения в шаблоне
        return list_car

    def get_time_zone(self):
        user_name = self.request.user.username
        enterprise = Enterprise.objects.get(manager__username__contains=user_name) # получаем предприятие по пользователю
        tz = pytz.timezone(enterprise.time_zone) # получаем таймзону из предприятия текущего менеджера
        return tz

    def get(self, request):
        # переопределяем родительский метод для получения запроса GET
        queryset = self.get_queryset()
        #serializer = CarSerializer(queryset, many=True)
        paginator = Paginator(queryset, 8)
        page = request.GET.get('page')
        #page = self.paginate_queryset(queryset) # формируем данные для отображения на одной странице
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

    queryset = get_queryset
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

class TripView(LoginRequiredMixin, ListCreateAPIView):
    serializer_class = TripSerialazer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'UITrip.html'

    def get_queryset(self):
        queryset = Trip.objects.all()

        trip = queryset
        #trip = queryset.filter(begin_time__gte=self.request.GET.get('date'))

        #trip = Trip.objects.filter(begin_time=str(self.request.POST.get('date')))
        return trip
    queryset = get_queryset
    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        #time = request.POST.get('date')
        qurey_trip = Trip.objects.filter(end_time__gte=request.POST.get('date'))
        trip = qurey_trip.filter(begin_time__lte=request.POST.get('date'))
        paths = []
        for i in trip:
            paths.append(i.geo_data)
        if len(paths) != 0:
            path_to_file = 'media/' + str(paths[0])
            with open(path_to_file, 'r') as file:
                geodate = [row.strip() for row in file]

        else:
            geodate = 'No date'
        #serializer = TripSerialazer(trip, many=True)


        # with open(Trip.geo_data) as file:
        # str = [row.strip() for row in file]
        # file.closed

        return Response({'result': geodate})

    def get(self, request):
        return Response(locals())

    raise_exception = True

class CarDetailView(LoginRequiredMixin, generics.ListAPIView, ListModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    raise_exception = True  # переопределение поля исключения, в случае не аутентифицированного пользователя
