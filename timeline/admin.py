from django.contrib import admin
from .models import Milestone

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'future')  # Include 'future' in the list view
    list_filter = ('future',)  # Add a filter for future milestones
