from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Song, Artist, Genre, Playlist

# Create your views here.
def musicbox_home(request):
    context = {
        'song_count' : Song.objects.all().count(), 
        'artist_count' : Artist.objects.all().count(),
        'genre_count' : Genre.objects.all().count(),
        'playlist_count' : Playlist.objects.all().count(),
    }
    return render(request, "musicbox/musicbox_home.html", context=context)

def kind_list(request, kind):
    if kind=='song':
        contexts = Song.objects.all()
        PAGE_ROW_COUNT = 6
    elif kind=='artist':
        contexts = Artist.objects.all()
        PAGE_ROW_COUNT = 10
    elif kind=='genre':
        contexts = Genre.objects.all()
        PAGE_ROW_COUNT = 10
    elif kind=='playlist':
        contexts = Playlist.objects.all()
        PAGE_ROW_COUNT = 10
    else:
        return redirect("musicbox:musicbox_home")
    
    PAGE_DISPLAY_COUNT = 10
    
    paginator=Paginator(contexts, PAGE_ROW_COUNT)
    pageNum=request.GET.get('pageNum') # 현제 페이지
    
    totalPageCount=paginator.num_pages # 전체 페이지 갯수 
    
    try:
        contexts = paginator.page(pageNum)
    except PageNotAnInteger:
        contexts = paginator.page(1)
        pageNum = 1
    except EmptyPage:
        contexts = paginator.page(paginator.num_pages)
        pageNum = paginator.num_pages
        
    pageNum = int(pageNum)
    
    startPageNum = 1 + PAGE_DISPLAY_COUNT * int((pageNum - 1)/PAGE_DISPLAY_COUNT)
    endPageNum = startPageNum + PAGE_DISPLAY_COUNT-1
    if totalPageCount < endPageNum:
        endPageNum = totalPageCount
        
    bottomPages = range(startPageNum, endPageNum+1)
    
    return render(request, f"musicbox/{kind}_list.html", {
            f'{kind}s':contexts,
            'kind':kind,
            'pageNum':pageNum,
            'bottomPages':bottomPages,
            'totalPageCount':totalPageCount,
            'startPageNum':startPageNum,
            'endPageNum':endPageNum
        }
    )

def kind_detail(request, kind, pk):
    if kind=='song':
        context = get_object_or_404(Song, pk=pk)
    elif kind=='artist':
        context = get_object_or_404(Artist, pk=pk)
    elif kind=='genre':
        context = get_object_or_404(Genre, pk=pk)
    elif kind=='playlist':
        context = get_object_or_404(Playlist, pk=pk)
    else:
        return redirect("musicbox:musicbox_home")

    return render(request, f"musicbox/{kind}_detail.html", {
            f'{kind}':context,
        }
    )