from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class CategoriesFood(models.Model):
    name = models.CharField('Название', max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
class Employees(models.Model):
    firstName = models.CharField('Имя', max_length=20)
    lastName = models.CharField('Фамилия', max_length=20)
    phoneNumberRegex = RegexValidator(regex = r"^(\+375|80)-(29|25|44|33)-(\d{3})(\d{2})(\d{2})$")
    phone = models.CharField('Телефон',
        validators=[phoneNumberRegex],
        max_length=15,
        unique=True
    )
    employeesPosition = models.CharField('Должность', max_length=20)
    category = models.ForeignKey('CategoriesFood',  on_delete=models.SET_DEFAULT, verbose_name='Категория', null=True, default=None)   #если категория удалится можно вызвать ф-ию по замене категории
    
    def __str__(self):
        if self.category is None:
            category_name = 'Без категории'
        else:
            category_name = str(self.category)
        return f'{self.lastName} {self.firstName} ({category_name})'
        # inf = ''
        # inf += f'{self.lastName} '
        # inf += self.firstName
        # return inf
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
    
class Dishes(models.Model):
    name = models.CharField('Название блюда', max_length=100)
    image = models.ImageField('Изображение', upload_to='uploads')
    price = models.DecimalField('Стоимость', max_digits=10, decimal_places=2)
    cookingTime = models.IntegerField('Приготовление в минутах')
    category = models.ForeignKey('CategoriesFood',  on_delete=models.SET_NULL, verbose_name='Категория', null=True, default='Без категории')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
    
class Products(models.Model):
    name = models.CharField('Название', max_length=100)
    amount = models.PositiveIntegerField('Количество')
    UNIT_STATUS = (('KG', 'кг'),
                      ('G', 'гр'),
                      ('SHT', 'шт'))
    unit = models.CharField('Единица измерения', max_length=5, choices=UNIT_STATUS, default='KG')    #единица измерения
    pricePerUnit = models.FloatField('Цена за единицу')
    expiration = models.CharField('Годность в месяцах', max_length=20)   #срок годности
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
class Ingredients(models.Model):
    amount = models.IntegerField()
    UNIT_STATUS = (('KG', 'кг'),
                      ('G', 'гр'),
                      ('SHT', 'шт'), 
                      ('STL', 'ст.л.'),
                      ('CHL', 'ч.л.'),)
    unit = models.CharField('Единица измерения', max_length=5, choices=UNIT_STATUS, default='KG')    #единица измерения
    product =  models.ForeignKey('Products', on_delete=models.SET_DEFAULT, verbose_name='Продукты', default=None)
    dishe = models.ForeignKey('Dishes', on_delete=models.SET_DEFAULT, verbose_name='Блюдо', default=None)
   
    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

class Order(models.Model):
    id = models.AutoField('Номер заказа', primary_key=True)  #номер заказа
    #Обратите внимание, что использование явного поля id может потребовать дополнительной работы при создании и обновлении записей, 
    # поскольку Django обычно автоматически создает и управляет полем id для каждой модели. Также имейте в виду, что если вы явно 
    # определяете поле id, Django не будет автоматически создавать его значение при сохранении новой записи, поэтому вам может 
    # потребоваться явно установить его значение перед сохранением.
    
    #number = models.IntegerField()  #id
    date =  models.DateTimeField('Дата заказа', blank=True)
    adress = models.CharField('Адрес', max_length=70)
    price = models.FloatField('Цена')
    payment_STATUS = (('cash', 'наличные'),
                      ('card', 'картой'),)
    payment = models.CharField('Оплата', max_length=10, choices=payment_STATUS, default='card')  #boll choise
    delivery_STATUS = (('C', 'самовывоз'),
                       ('D', 'доставка'),
                       ('T', 'в ресторане'),)
    delivery = models.CharField('Доставка', max_length=1, choices=delivery_STATUS, default='D')  
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
class OrderItem(models.Model):
    quantity  = models.PositiveIntegerField('Количество')     #положительные целочисленные значения (больше или равно нулю). Оно ограничивает вводимые значения таким образом, что они не могут быть отрицательными.
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Заказ', null=True)
    dish = models.ForeignKey('Dishes', on_delete=models.SET_DEFAULT, verbose_name='Блюдо', null=True, default=None)
   
    def get_order_id(self):
        return self.order.id  #Мы также добавили метод get_order_id, который возвращает значение поля id связанной записи Order.

    def __str__(self):
        numberOrder = self.get_order_id()
        inf = f'Заказ №{numberOrder}'
        return inf
    
    class Meta:
        verbose_name = 'Состав заказа'
        verbose_name_plural = 'Состав заказа' 
        
class Tables(models.Model):
    number = models.PositiveIntegerField('Номер', unique=True)
    numberOfSeats = models.PositiveIntegerField('Число мест')
    availability_STATUS = (('A', 'Доступен'), 
                           ('B', 'Забронирован'),)
    availability = models.CharField('Доступность', max_length=1, choices=availability_STATUS, default='A')
    
    def __str__(self):
        return str(self.number)
    
    class Meta:
        verbose_name = 'Столик'
        verbose_name_plural = 'Столики' 
    
class Availabilitys(models.Model):
    beginning = models.DateTimeField('Начало брони')
    end = models.DateTimeField('Окончание брони')
    table = models.ForeignKey('Tables', on_delete=models.SET_DEFAULT, null=True, verbose_name='Столик', default=None)
    
    def __str__(self):
        return str(self.table.number)
    
    class Meta:
        verbose_name = 'Занятость'
        verbose_name_plural = 'Занятость' 

class Supply(models.Model):    #поставка
    provider = models.CharField('Поставщик', max_length=20)
    dateOfDelivery = models.DateTimeField('Дата поставки')
    dateOfExpiry = models.DateTimeField('Дата окончания срока годности')
    quantity = models.PositiveIntegerField('Количество')
    UNIT_STATUS = (('KG', 'кг'),
                      ('G', 'гр'),
                      ('SHT', 'шт'),
                      ('L', 'л.'),)
    unit = models.CharField('Единица измерения', max_length=5, choices=UNIT_STATUS, default='KG')    #единица измерения
    total = models.FloatField('Сумма')
    product =  models.ForeignKey('Products', on_delete=models.SET_NULL, null=True, verbose_name='Продукты', default=1)
    STATUS = (('B', 'Испорчен'),
              ('G', 'Годен'),)
    status = models.CharField('Статус', max_length=1, choices=STATUS, default= 'G') 
    
    def __str__(self):
        return self.provider
    
    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'

class Users(models.Model):
    name = models.CharField('Имя', max_length=20)
    phoneNumberRegex = RegexValidator(regex = r"^(\+375|80)-(29|25|44|33)-(\d{3})(\d{2})(\d{2})$")
    phone = models.CharField('Телефон', 
        validators=[phoneNumberRegex],
        max_length=15,
        unique=True
    )
    email = models.EmailField(blank=False)
    dateOfBirthday = models.DateField('Дата рождения', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
class Administrators(models.Model):
    user = models.ForeignKey('Users', on_delete=models.SET_DEFAULT, verbose_name='Пользователи', null=True, default=None)
    email = models.EmailField(editable=True, default='')
    level = models.CharField('Уровень доступа', max_length=10)
    
    def get_user_email(self):
        self.email = self.user.email  #Мы также добавили метод get_order_id, который возвращает значение поля id связанной записи Order.
        return self.email
    
    def __str__(self):
        userEmail = self.get_user_email()
        inf = f'{self.user.name} {userEmail}'
        return inf

    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'
        
    # class Meta:
    #     ordering = ["-my_field_name"]


    # # def get_absolute_url(self):

    # #      return reverse('model-detail-view', args=[str(self.id)])

    # def __str__(self):
    
    #     return self.field_name
    
 