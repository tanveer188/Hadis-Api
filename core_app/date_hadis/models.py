from django.db import models
from django.core.exceptions import ValidationError
from core_app.settings import MEDIA_ROOT
from django.conf import settings
from modeltranslation.utils import build_localized_fieldname

class Block(models.Model):
    image = models.ImageField(upload_to=MEDIA_ROOT + "/" + 'block_images/', null=True, blank=True, verbose_name="Block Image")
    url = models.URLField(null=True, blank=True, verbose_name="Block URL")
    text = models.TextField(null=True, blank=True, verbose_name="Block Text")

    def clean(self):
        filled_fields = [field for field in ['image', 'url', 'text'] if getattr(self, field)]

        if len(filled_fields) != 1:
            raise ValidationError("Only one field should be filled at a time.")

        # Extract language codes from settings.LANGUAGES
        language_codes = [lang[0] for lang in settings.LANGUAGES]

        # Check if 'text' is filled for one language and all translations are filled
        for lang in language_codes:
            text_field_name = build_localized_fieldname('text', lang)
            if getattr(self, text_field_name) and not all(getattr(self, build_localized_fieldname('text', other_lang)) for other_lang in language_codes):
                raise ValidationError(f"All translations of 'text' field should be filled when one translation is filled in language {lang}.")
            
            
    def __str__(self):
        content_type = "Text"
        if self.image:
            content_type = "Image"
        elif self.url:
            content_type = "URL"
        return f"Block {self.id} ({content_type})"

    class Meta:
        verbose_name = "Content Block"
        verbose_name_plural = "Content Blocks"

class Post(models.Model):
    date = models.DateField(unique=True, verbose_name="Post Date")
    image = models.ImageField(upload_to=MEDIA_ROOT + "/" + 'post_images/', null=True, blank=True, verbose_name="Post Image")
    title = models.CharField(max_length=30, verbose_name="Post Title")
    
    def __str__(self):
        # Combine title and date for informative representation
        return f"{self.title} - {self.date}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

class Block_Post_Rel(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Post")
    block = models.OneToOneField(Block, on_delete=models.PROTECT, verbose_name="Content Block")
    order = models.PositiveIntegerField(editable=False, verbose_name="Block Order")  # Tracks block's position within the Post

    class Meta:
        ordering = ['post', 'order']  # Ensures correct order across multiple Posts
        unique_together = ('post', 'block')  # One block can only be linked to one post
        verbose_name = "Post Content Relation"
        verbose_name_plural = "Post Content Relations"

    def save(self, *args, **kwargs):
        if not self.order:
            try:
                last_order = Block_Post_Rel.objects.filter(post=self.post).latest('order').order
                self.order = last_order + 1
            except Block_Post_Rel.DoesNotExist:
                self.order = 1
        super().save(*args, **kwargs)
        
