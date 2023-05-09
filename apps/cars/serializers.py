from rest_framework import serializers

from apps.cars.models import Car, SpecialMarks, PeriodsOwnership, CarPost, CarPostImage, CarPostComment, CarPostFavorite


class CarPostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPostImage
        fields = "__all__"

class CarPostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPostComment
        fields = "__all__"

class CarPostFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPostFavorite
        fields = "__all__"

class CarPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPost
        fields = "__all__"

class CarPostDetailSerializer(serializers.ModelSerializer):
    post_images = CarPostImageSerializer(many=True, read_only=True)
    posts_comment = CarPostCommentSerializer(many=True, read_only=True)
    count_comments = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CarPost
        fields = ('id', 'brand', 'model', 'year', 'color',
                  'rudder_location', 'engine_volume', 'price', 
                  'mileage', 'transmission', 'region',
                  'accounting', 'another', 'user',
                  'post_images', 'posts_comment', 'count_comments')
        
    def get_count_comments(self, obj):
        return obj.posts_comment.all().count()

class SpecialMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialMarks
        fields = "__all__"

class PeriodsOwnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodsOwnership
        fields = "__all__"

class CarSerializer(serializers.ModelSerializer):
    cars_special_marks = SpecialMarksSerializer(read_only=True, many=True)
    cars_periods_ownership = PeriodsOwnershipSerializer(read_only=True, many=True)
    class Meta:
        model = Car
        fields = ('id', 'license_plate', 'brand', 'model', 'color', 
                'year', 'rudder_location', 'engine_volume',
                'cars_special_marks', 'cars_periods_ownership')