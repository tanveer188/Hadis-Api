from rest_framework import serializers
from .models import Post, Block, Block_Post_Rel

from core_app.settings import LANGUAGES

list = [code for code,lang in LANGUAGES]
print(list)

class BlockSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()

    class Meta:
        model = Block
        fields = ['image', 'url', 'content_type',"text"]
        fields.extend(["text_"+code for code in list])

    def get_content_type(self, obj):
        content_type = "Text"
        if obj.image:
            content_type = "Image"
        elif obj.url:
            content_type = "URL"
        return content_type

class PostDetailSerializer(serializers.ModelSerializer):
    blocks = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['date','blocks','title',"image"]
        fields.extend(["title_"+code for code in list])

    def get_blocks(self, obj):
        blocks = Block_Post_Rel.objects.filter(post=obj).order_by('order')
        return BlockSerializer([block.block for block in blocks], many=True).data
