from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import SupporterFeedback
from .forms import SupporterFeedbackForm


# Feedback List
def feedback_list(request):
    feedback = SupporterFeedback.objects.all().order_by('-created_at')
    return render(request, 'feedback/list.html', {'feedback': feedback})


# Feedback Create View
def feedback_create(request):
    if request.method == 'POST':
        form = SupporterFeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)

            # If user didn't write a name but is logged in, use username
            if not instance.supporter_name and request.user.is_authenticated:
                instance.supporter_name = request.user.username
                instance.supporter = request.user

            instance.save()
            messages.success(request, "Feedback submitted successfully!")
            return redirect('feedback_list')
    else:
        form = SupporterFeedbackForm()
    return render(request, 'feedback/form.html', {'form': form})


# Feedback Update View
def feedback_update(request, pk):
    feedback_item = get_object_or_404(SupporterFeedback, pk=pk)
    if request.method == 'POST':
        form = SupporterFeedbackForm(request.POST, request.FILES, instance=feedback_item)
        if form.is_valid():
            form.save()
            messages.success(request, "Feedback updated successfully!")
            return redirect('feedback_list')
    else:
        form = SupporterFeedbackForm(instance=feedback_item)
    return render(request, 'feedback/form.html', {'form': form, 'is_edit': True})


# Feedback Delete View
def feedback_delete(request, pk):
    feedback_item = get_object_or_404(SupporterFeedback, pk=pk)
    feedback_item.delete()
    messages.success(request, "Feedback deleted successfully!")
    return redirect('feedback_list')