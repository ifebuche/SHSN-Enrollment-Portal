from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Counting(models.Model):
    title = models.CharField(max_length=100, blank=True)
    counter = models.IntegerField()

    def __str__(self):
        return str(self.counter)

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    score = models.CharField(max_length=15)
    #grade = models.CharField(max_length=15)
    grade = models.CharField(max_length=100, verbose_name="Grade", blank=True, default=None)
    student_no = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    #counting = models.ForeignKey(Counting,on_delete=models.CASCADE)

    
    @property
    def get_grade(self):
        if int(self.score) >= 70:
            return 'A'

        elif int(self.score) <= 69 and int(self.score) > 64:
            return 'B'

        elif int(self.score) <= 64 and int(self.score) > 50:
            return 'C'

        elif int(self.score) <= 49 and int(self.score) > 45:
            return 'D'

        elif int(self.score) <= 44 and int(self.score) > 40:
            return 'E'

        elif int(self.score) < 40:
            return 'F'

    def save(self, *args, **kwargs):
        self.grade = self.get_grade
        super(Student, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.grade

        