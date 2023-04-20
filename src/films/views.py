from django.shortcuts import render
from django.views.generic import ListView

from .models import Film, UserFilmRelation
from .forms import FilmAddForm


def home(request):
    if request.method == 'POST':
        film_name = request.POST.get("film-name")
        if film_name:
            try:
                film = Film.objects.get(name=film_name)
            except Exception as e:
                print(e)
                pass
            else:
                if film:
                    try:
                        relation = UserFilmRelation.objects.select_related('user').select_related('film').get(film=film, user=request.user)
                        if relation.in_bookmarks == True:
                            relation.in_bookmarks = False
                        else:
                            relation.in_bookmarks = True
                        relation.save()
                    except Exception as e:
                        relation = UserFilmRelation.objects.create(
                            user=request.user,
                            film=film,
                            in_bookmarks=False)
                        relation.save()
        else:
            print("film name not exist")
        films = Film.objects.select_related('data').prefetch_related('viewers').all()
        data = {
            'films': films
        }
        return render(request, 'films/home.html', data)
    else:
        films = Film.objects.select_related('data').prefetch_related('viewers').all()
        data = {
            'films': films
        }
        return render(request, 'films/home.html', data)
    

def search(request):    
    if request.method == 'GET':
        films = Film.objects.select_related('data').filter(name__icontains=request.GET.get("search"))
        
        data = {
            'films': films
        }
        return render(request, 'films/home.html', data)
    
class Search(ListView):
    template_name = 'films/home.html'
    context_object_name = "films"
    
    def get_queryset(self):
        return Film.objects.select_related('data').filter(name__icontains=self.request.GET.get("search"))
    

def add_film(request):
    if request.method == "POST":
        form = FilmAddForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.added_by = request.user
            form.save(commit=True)
        else:
            form = FilmAddForm()
            return render(request, 'films/add_film.html', {'form': form})
    elif request.method == 'GET':
        form = FilmAddForm()
        return render(request, 'films/add_film.html', {'form': form})
        