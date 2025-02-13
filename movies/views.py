from django.shortcuts import render

# Create your views here.
movies = [
    {
        'id': 1, 'name': "whatever", 'price': 500, 'description': "whatever is in it"
    },
]

def index(request):
    template_data = {}
    template_data['title'] = 'movies'
    template_data['movies'] = movies
    return render(request, 'movies/index.html', {'template_data': template_data})