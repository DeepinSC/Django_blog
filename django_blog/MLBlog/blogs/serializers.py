from rest_framework import serializers
from models import Blogs

class BlogsSerializer(serializers.HyperlinkedModelSerializer):
    #author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Blogs
        fields = ('url','id','title','author','content','category','tag','created_time','modify_time')