from django.shortcuts import (
    render,
    get_object_or_404
)

from .models import CareOrganization


def organization_list(request):
    organizations = CareOrganization.objects.filter(
        verification_status=True
    )

    return render(
        request,
        'organizations/list.html',
        {
            'organizations': organizations
        }
    )


def organization_detail(request, pk):
    organization = get_object_or_404(
        CareOrganization,
        pk=pk,
        verification_status=True
    )

    return render(
        request,
        'organizations/detail.html',
        {
            'organization': organization
        }
    )


from django.shortcuts import render

# Create your views here.
