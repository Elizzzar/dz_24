from django.shortcuts import render
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def get_jsonplaceholder_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        return response.json()
    return []

def pagination(request, page=1):
    data = get_jsonplaceholder_data()

    items_per_page = 10 
    paginator = Paginator(data, items_per_page)

    try:
        data_page = paginator.page(page)
    except PageNotAnInteger:
        data_page = paginator.page(1)
    except EmptyPage:
        data_page = paginator.page(paginator.num_pages)

    return render(request, "pagination.html", {"data": data_page})
