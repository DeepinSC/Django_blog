from rest_framework import serializers
from models import Blogs
from models import User

class BlogsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Blogs
        fields = ('url','id','title','content','category','tag','created_time','modify_time','owner')