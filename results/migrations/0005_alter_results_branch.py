<<<<<<< HEAD
# Generated by Django 4.0.6 on 2022-08-14 02:17
=======
# Generated by Django 4.0.6 on 2022-08-12 16:58
>>>>>>> 6dde283eee2ec33356a3064d99fb0ea3a126c44a

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0004_resultpage_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='branch',
<<<<<<< HEAD
            field=models.CharField(choices=[('', 'Choose Your Branch'), ('Civil Engineering', 'Civil Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Electronics And Communication Engineering', 'Electronics And Communication Engineering'), ('ECE Dual', 'ECE Dual'), ('Chemical Engineering', 'Chemical Engineering'), ('Computer Science Engineering', 'Computer Science Engineering'), ('CSE Dual', 'CSE Dual'), ('Material Science', 'Material Science'), ('Engineering Physics', 'Engineering Physics'), ('Mathematics And Computing', 'Mathematics And Computing')], default='', max_length=100),
=======
            field=models.CharField(choices=[('', 'Choose Branch'), ('Civil Engineering', 'Civil Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Electronics And Communication Engineering', 'Electronics And Communication Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Computer Science Engineering', 'Computer Science Engineering'), ('Material Science', 'Material Science'), ('Engineering Physics', 'Engineering Physics'), ('Mathematics And Computing', 'Mathematics And Computing')], default='', max_length=100),
>>>>>>> 6dde283eee2ec33356a3064d99fb0ea3a126c44a
        ),
    ]
