Парсинг с сайта https://www.kinopoisk.ru.

Данный парсинг с сайта https://www.kinopoisk.ru производит поиск фильмов с рейтингом от 7 и более, оцененных конкретным пользователем.

При запуске программы она просит ввести ID пользователя и нажать Enter (например вводим 1743354).
Программа произведет поиск всех фильмов пользователя, которые он оценил и по результату выгрузит 2 таблицы данных.
В таблице с названием user_rates1.xlsx выгрузятся название всех фильмов и их рейтинг конкретного пользователя.
В таблице с названием user_rates2.xlsx выгрузятся название фильмов с их рейтингом, оцененные пользователем от 7 и выше.

Что потребуется для правильной работы программы:
С помощью библиотеки requests получаем возможность работать с HTTP-запросами.
С помощью библиотеки BeautifulSoup производим извлечение данных из файлов HTML.
С помощью библиотеки pandas производим запись данных выборки в фаил с разрешением .xlsx.
Для установки библиотек в командной строке запускаем по очереди  pip install requests, pip install beautifulsoup4 lxml и pip install pandas openpyxl.





