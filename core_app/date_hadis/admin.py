from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Block, Post, Block_Post_Rel
from modeltranslation.translator import TranslationOptions, translator,register

from .serializers import list

@register(Block)
class BlockTranslationOptions(TranslationOptions):
    fields = ('text',)

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ['title',]  # Add other fields that you want to translate
    required_languages = list
@admin.register(Block)
class BlockAdmin(TranslationAdmin):
    group_fieldsets = True
    class Media:
        js = (
            'https://code.jquery.com/jquery-3.6.4.min.js',  # Use the latest jQuery version
            'https://code.jquery.com/ui/1.12.1/jquery-ui.min.js',  # Use the latest jQuery UI version
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
@admin.register(Post)
class PostAdmin(TranslationAdmin):
    group_fieldsets = True

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.6.4.min.js',  # Use the latest jQuery version
            'https://code.jquery.com/ui/1.12.1/jquery-ui.min.js',  # Use the latest jQuery UI version
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Block_Post_Rel)
class Block_Post_RelAdmin(admin.ModelAdmin):
    pass