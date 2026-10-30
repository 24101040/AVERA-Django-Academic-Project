from django.shortcuts import (
    render,
    get_object_or_404
)

from .models import Child


def child_list(request):
    children = Child.objects.filter(
        is_public=True,
        organization__verification_status=True
    )

    return render(
        request,
        'children/list.html',
        {
            'children': children
        }
    )


def child_detail(request, pk):
    child = get_object_or_404(
        Child,
        pk=pk,
        is_public=True,
        organization__verification_status=True
    )

    milestones = child.milestones.all()

    return render(
        request,
        'children/detail.html',
        {
            'child': child,
            'milestones': milestones
        }
    )


from django.shortcuts import render

# Create your views here.
