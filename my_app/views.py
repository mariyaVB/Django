from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def info_main(request):
    return HttpResponse('<h1>Каталог живописи</h1>\n'
                        '<h2><a href=http://127.0.0.1:8000/painting/progulka_s_zontom_po_allee>Прогулка с зонтом по аллее</a></h2>\n'
                        '<h2><a href=http://127.0.0.1:8000/painting/na_rassvete>На рассвете</a></h2>')


def info_art(request, painting_slug):
    if painting_slug == 'progulka_s_zontom_po_allee':
        return HttpResponse("<h2>Феоктистов Вячеслав</h2>\n"
                            "<h3>Картина маслом на холсте с изображением городской аллеи осенью, следы огней машин,"
                            "силуэт девушки с зонтом вдали, осенние листья клёнов. Свет фонарей на мокром асфальте."
                            "Романтическое настроение</h3>\n"
                            "<h3>21 000₽</h3>\n"
                            "<h2>Об авторе:\n"
                            "<h3>Вечеслав является членом творческого Союза художников России и Союза художников Подмосковья."
                            "Более 20 лет пишет маслом стильные и красивые картины."
                            "<img src=https://zvetnoe.ru/upload/catalog/2019/12/WD-0012.jpg></img>")

    if painting_slug == 'na_rassvete':
        return HttpResponse("<h2>Тикунова Ольга</h2>\n"
                            "<h3>Картина морской пейзаж «На рассвете» написана масляными красками на холсте,"
                            "натянутом на подрамник. Красивый морской пейзаж,утреннее море, прозрачные волны. </h3>\n"
                            "<h3>13 000₽</h3>\n"
                            "<h2>Об авторе:\n"
                            "<h3>Ольга пишет реалистичную живопись, особенно пейзажи. "
                            "Картины Ольги нашли свой дом не только в городах России, но и в Канаде, Германии и Китае."
                            "<img src=https://narisyu.cdnbro.com/posts/70937736-rassvet-risunok-akvareliu-34.jpg></img>")

    else:
        return HttpResponseNotFound('<img src=https://crocos.kz/files/404_4x%20(1).jpg></img>')






