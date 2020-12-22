from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length = 200)
    picture = models.ImageField(upload_to = 'uploads')
    description = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.CASCADE)


    @staticmethod
    def get_all_images():
        return Image.objects.all()

    @staticmethod
    def get_all_images_by_id(category_id):
        if category_id:
            return Image.objects.filter(category = category_id)
        else:
            return Image.get_all_images()



class Category(models.Model):
    name = models.CharField(max_length= 50)



    @staticmethod

    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name