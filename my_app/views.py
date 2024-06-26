from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import QuestionAnswer


# Create your views here.
def info_main(request):
    return render(request, 'info_main.html')


def info_art(request, painting_slug):
    if painting_slug == 'women-1':
        data = {
            'art_dict': {
                'Автор:': 'Тикунова Ольга',
                'Описание картины:': '''Картина портрет женщины «На рассвете» написана масляными красками на холсте.
                                    натянутом на подрамник. Красивый линии лица, загадка в глазах, прозрачные мысли.''',
                'Стоимость картины:': '30 000₽',
                'Об авторе:': '''Ольга пишет реалистичную живопись, особенно пейзажи.
                    Картины Ольги нашли свой дом не только в городах России, но и в Канаде, Германии и Китае.'''},
            'images': ['../static/images/women1.png'],
            'title': ['Картина женщины 1']}
        return render(request, 'art.html', context=data)

    if painting_slug == 'men-1':
        data = {
            'art_dict': {
                'Автор:': 'Феоктистов Вячеслав',
                'Описание картины:': '''Картина маслом на холсте с изображением городского мужчины, следы от работы,
                                    силуэт доброго человека, задумчивость в глазах.''',
                'Стоимость картины:': '30 000₽',
                'Об авторе:': '''Вечеслав является членом творческого Союза художников России и Союза художников Подмосковья.
                                Более 20 лет пишет маслом стильные и красивые картины.'''
            },
            'images': ['men1.png'],
            'title': ['Картина мужчины 1']}
        return render(request, 'art.html', context=data)

    if painting_slug == 'men-2':
        data = {
            'art_dict': {
                'Автор:': 'Алехнович Геннадий',
                'Описание картины:': '''Картина маслом на холсте с изображением мужчины, следы мудрости возраста,
                                    свет на уставшем лице.''',
                'Стоимость картины:': '30 000₽',
                'Об авторе:': '''Характерны два направления цветочная живопись и фигуратив в жанре ню.
                                Стремление в живописи к легкости, индивидуальности, неповторимости, современности.
                                Член Союза Художников России.'''
            }, 'images': ['{% static \'images/men2.png\' %}'],
            'title': ['Картина мужчины 2']}
        return render(request, 'art.html', context=data)

    else:
        return render(request, 'page_404.html', status=404)


def question_answer(request):
    if request.method == 'POST':
        question_answer_value = request.POST.get('question_answer')
        QuestionAnswer.objects.create(question=question_answer_value)
        return HttpResponse(f'''<h2>Ваш вопрос задан.</h2>
                            <a href = ""><button>Вернуться назад</button></a>''')

    if request.method == 'GET':
        result = QuestionAnswer.objects.all()
        data = {
            'question_answer': result
        }
        return render(request, 'question_answer.html', data, status=200)



