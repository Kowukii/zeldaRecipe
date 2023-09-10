from django.urls import path
from api.views import *
from api.bank import bank
from api.image import image
urlpatterns = [
    path('index/', index, name='index'),
    path('info/', get_info, name='info_demo'),
    path('brief/<int:uid>', brief, name='brief'),
    path('fruit/', bank.FruitView.as_view()),
    path('fish/', bank.FishView.as_view()),
    path('mushroom/', bank.MushroomView.as_view()),
    path('vegetable/', bank.VegetableView.as_view()),
    path('meat/', bank.MeatView.as_view()),
    path('crab/', bank.CrabView.as_view()),
    path('nut/', bank.NutView.as_view()),
    path('enemy/', bank.EnemyView.as_view()),
    path('relish/', bank.RelishView.as_view()),
    path('special/', bank.SpecialView.as_view()),
    path('insect/', bank.InsectView.as_view()),
    path('bad/', bank.BadView.as_view()),
    path('image/', DataSubmitView.as_view({
        'post': 'create'
    })),
    path('recipe/', RecipeCheckView.as_view()),
]