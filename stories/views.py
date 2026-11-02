from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Story


def stories_list(request):
    if request.method == 'POST':
        Story.objects.create(
            title=request.POST.get('title'),
            year=request.POST.get('year') or 'ADOPTED IN 2026',
            author=request.POST.get('author'),
            content=request.POST.get('content'),
            image=request.FILES.get('image'),
        )
        messages.success(request, 'Your adoption story has been published successfully!')
        return redirect('stories_list')

    stories = Story.objects.all().order_by('-id')
    return render(request, 'story/stories.html', {
        'stories': stories
    })


def story_details(request, id):
    story = get_object_or_404(Story, id=id)
    return render(request, 'story/story-details.html', {
        'story': story
    })