from django.shortcuts import render, get_object_or_404
from .models import Milestone

def timeline_view(request):
    milestones = Milestone.objects.all().order_by('id')  # Order by creation order
    return render(request, 'timeline/timeline.html', {'milestones': milestones})

def milestone_detail_view(request, pk):
    milestone = get_object_or_404(Milestone, pk=pk)
    return render(request, 'timeline/milestone_detail.html', {'milestone': milestone})
