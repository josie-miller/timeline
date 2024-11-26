from django.db import models

class Milestone(models.Model):
    title = models.CharField(max_length=200)  # Title of the milestone
    date = models.CharField(max_length=100)  # Date (e.g., "200,000 years ago")
    description = models.TextField()  # Short description
    image = models.ImageField(upload_to='milestone_images/')  # Image upload path
    source = models.URLField(max_length=500, blank=True, null=True)  # Source URL for the milestone
    future = models.BooleanField(default=False)  # Optional field to mark future milestones

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']  # Default ordering by creation order