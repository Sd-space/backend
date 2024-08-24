# from django.db import models

# class Course(models.Model):
#     title = models.CharField(max_length=255,null=True)
#     course_code = models.CharField(max_length=50, unique=True)
#     description = models.TextField(null=True)
#     year = models.IntegerField(null=True)
#     semester = models.IntegerField(null=True)

#     def __str__(self):
#         return f"{self.title} ({self.course_code})"

# class CourseInstance(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     year = models.IntegerField(null=True)
#     semester = models.IntegerField(null=True)

#     def __str__(self):
#         return f"{self.course.title} - {self.year}/{self.semester}"
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255, null=True)
    course_code = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True)
    year = models.IntegerField(null=True)
    semester = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.title} ({self.course_code})"

class CourseInstance(models.Model):
    id=models.AutoField(primary_key=True)
    course= models.ForeignKey(Course, to_field='course_code', on_delete=models.CASCADE)
    year = models.IntegerField(null=True)
    semester = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.course_code.title} - {self.year}/{self.semester}"
