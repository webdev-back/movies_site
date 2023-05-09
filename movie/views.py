from django.shortcuts import render
from .models import Movie, Review
from django.shortcuts import get_object_or_404, redirect
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    context = {
        'searchTerm': searchTerm,
        'movies': movies,
    }
    return render(request, 'movie/index.html', context)


def signup(request):
    email = request.GET.get('email')
    return render(request, 'movie/signup.html', {'email': email})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    context = {
        'movie': movie,
        'reviews': reviews,
    }
    return render(request, 'movie/detail.html', context)


@login_required
def createreview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'GET':
        context = {
            'form': ReviewForm(),
            'movie': movie
        }
        return render(request, 'movie/createreview.html', context)
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('detail', newReview.movie.id)
        except ValueError:
            context = {
                'form': ReviewForm(),
                'error': 'bad data passed in',
            }
            return render(request, 'movie/createreview.html', context)


@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)

    if request.method == 'GET':
        form = ReviewForm(instance=review)
        context = {
            'form': form,
            'review': review,
        }
        return render(request, 'movie/updatereview.html', context)
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.movie.id)
        except ValueError:
            context = {
                'review': review,
                'form': form,
                'error': 'Bad data in form'
            }
            return render(request, 'movie/updatereview.html', context)


@login_required
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail', review.movie.id)
