import logging
from django.shortcuts import render

# Create your views here.

logger = logging.getLogger(__name__)


def timetable_landing(request):
    logger.info(request)
    feature_list = (
        {'icon': 'img/glasses2.svg', 'description': ('Перегляд розкладу '
         'групи (дізнайся, яка зараз пара)'), 'class': 'feature-block'},
        {'icon': 'img/edit45.svg', 'description': ('Редагування розкладу '
         '(доступне командирам груп)'), 'class': 'feature-block'},
        {'icon': 'img/school84.svg', 'description': ('Перегляд розкладу'
         ' викладача'), 'class': 'feature-block'},
        {'icon': 'img/checkmark2.svg', 'description': ('Перегляд графіку '
         'екзаменів та практики'), 'class': 'feature-block'},
        {'icon': 'img/sun127.svg', 'description': 'Канікули',
         'class': 'feature-block'},
        )
    return render(request, 'landing/promo.html',
                  {'feature_list': feature_list})


def timetable_about(request):
    return render(request, 'landing/about.html')
