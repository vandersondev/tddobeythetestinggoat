from django.http import HttpResponse


def home_page(resquest):
    return HttpResponse('<html><title>To-do lists</title></html>')
