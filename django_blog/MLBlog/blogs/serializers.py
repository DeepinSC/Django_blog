from rest_framework import serializers
from models import Blogs
from models import User

class BlogsSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Blogs
        fields = ('id','url','title','author','content','category','tag','created_time','modify_time')