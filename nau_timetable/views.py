import logging
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

logger = logging.getLogger(__name__)

def timetable_landing(request):
	logger.info(request)
	return render(request, 'landing/promo.html')

def timetable_about(request):
	return render(request, 'landing/about.html')

