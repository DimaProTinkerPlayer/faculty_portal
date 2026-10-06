from django.db import models

class FacultyInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name="Faculty Name")
    description = models.TextField(verbose_name="Faculty Description")
    general_info = models.TextField(verbose_name="General Info")
    contact_info = models.TextField(verbose_name="Contact Info")

    def __str__(self):
        return self.name

class Department(models.Model):
    title = models.CharField(max_length=200, verbose_name="Department Title")
    head_name = models.CharField(max_length=200, verbose_name="Department Head")

    def __str__(self):
        return self.title

class Program(models.Model):
    code = models.CharField(max_length=50, verbose_name="Program Code")
    title = models.CharField(max_length=200, verbose_name="Program Title")
    description = models.TextField(verbose_name="Program Description")
    coordinator_name = models.CharField(verbose_name="Department Coordinator Name")
    coordinator_contact = models.EmailField(verbose_name="Department Coordinator Contact")
    department = models.ForeignKey(Department, on_delete=models.CASCADE,related_name="programs", verbose_name="Department Graduate")
    disciplines = models.TextField(verbose_name="Disciplines list")

    def short_description(self):
        words = self.description.split()
        return words[:50] + "..."

    def __str__(self):
        return self.title

class Teacher(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Teacher Name")
    position = models.CharField(max_length=200, verbose_name="Teacher Position")
    degree = models.CharField(max_length=200, verbose_name="Teacher Degree")
    department = models.ForeignKey(Department, on_delete=models.CASCADE,related_name="teachers", verbose_name="Department Graduate")

    def __str__(self):
        return self.full_name