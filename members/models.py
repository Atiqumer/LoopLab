from django.db import models

# Create your models here.
class Contributor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(
        blank=True,
        help_text="Short bio or description of their role/skills."
    )
    profile_photo = models.ImageField(
        upload_to='contributor_photos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name