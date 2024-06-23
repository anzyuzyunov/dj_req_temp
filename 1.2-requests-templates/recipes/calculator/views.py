from django.shortcuts import render
from django.shortcuts import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
def helo(request):
    return HttpResponse('Привет, страница пустая')

def recipe(request, dish: str):
    ## Если есть условие с передачей количества персон не работает "Такого рецепта нет"
    servings = int(request.GET.get('servings', 1))
    context = {'recipe': {ingr: quantity * servings for (ingr, quantity) in DATA.get(dish).items()}}

    return render(request,'calculator/index.html',context)
    # context = {'recipe': DATA.get(dish)
    #
    # }
    # return render(request,'calculator/index.html',context)




# def recipe(request,dish:str):
#
#     context = {}
#     servings = int(request.GET.get('servings', 1))
#     recep = DATA.get(dish)
#     final_dish = {}
#     for dishs, caunt in recep.items():
#         final_dish[dishs] = caunt * servings
#     context.setdefault('recipe', final_dish)
#     return render(request,'calculator/index.html',context)
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
