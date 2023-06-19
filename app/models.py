from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Courses(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_number_topics(self):
        # course_id = id
        count = Lesson.objects.filter(course__id =self.id)
        return count.count()

    def get_absolute_url(self):
        return reverse('course', kwargs={'pk':self.pk})

    # def get_paid_users(self):
    #     users = Order.objects.filter(paid=True)

    class Meta:
        verbose_name_plural = "courses"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    paid = models.BooleanField(default="False")
    amount = models.IntegerField(default=0)
    stripe_payment_intent = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(default=None,max_length=800, null=True, blank=True)
    
    def __str__(self):
        return self.email


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    course = models.ManyToManyField(Courses, null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "topic"

    def get_absolute_url(self):
        return reverse('topic', kwargs={'id': self.id})


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,blank=True, null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user.username)