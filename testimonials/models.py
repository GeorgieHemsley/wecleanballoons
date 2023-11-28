from django.db import models

class Testimonial(models.Model):
    
    quote = models.TextField(
        max_length=500, 
        blank=False, 
        null=False
    )
    
    attribution = models.CharField(
        max_length=50, 
        blank=False, 
        null=False
    )
    
    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
    
    def __str__(self):
        return f"{self.quote} by {self.attribution}"