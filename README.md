# RestoraDjango
Заголовок проекта: Restora - Онлайн-сервис для заказа и доставки блюд из ресторана.

Описание проекта: Restora - это удобный веб-сайт, который позволяет пользователям заказывать блюда из ресторана и получать их доставку. Мы предлагаем широкий выбор меню, чтобы каждый мог найти что-то по своему вкусу. Наш сервис обеспечивает удобную и легкую систему заказа, а также быструю доставку, чтобы пользователи могли наслаждаться вкусными блюдами прямо у себя дома или в офисе.

Установка и использование:

Существующая виртуальная среда
Если ваш проект уже находится в существующей виртуальной среде Python, сначала установите django, запустив

$ pip install django
А затем запустите django-admin команду для запуска нового проекта:

$ django-admin startproject  <project_name>

После этого просто установите локальные зависимости, запустите миграцию и запустите сервер.

Начиная
Сначала клонируйте репозиторий из Github и переключитесь в новый каталог:

$ git clone git@github.com/USERNAME/{{ project_name }}.git
$ cd {{ project_name }}
Активируйте virtualenv для своего проекта.

Затем просто примените миграции:

$ python manage.py migrate
Теперь вы можете запустить сервер разработки:

$ python manage.py runserver
Откройте веб-браузер и перейдите по адресу http://localhost:3000/restora/home, чтобы получить доступ к веб-сайту Restora.
Зайдите на главной странице в меню или выберите необходимую категорию блюд. 
Выберите блюда из представленного меню.
Добавьте выбранные блюда в корзину и оформите заказ.
Укажите адрес доставки.
Проверьте информацию о заказе и подтвердите его.
Ожидайте доставку и наслаждайтесь вкусными блюдами из ресторана.