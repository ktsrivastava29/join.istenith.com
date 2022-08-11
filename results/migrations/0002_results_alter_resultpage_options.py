# Generated by Django 4.0.6 on 2022-08-11 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000000)),
                ('roll_number', models.CharField(max_length=30)),
                ('branch', models.CharField(choices=[('', 'Choose Your Branch'), ('Civil Engineering', 'Civil Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Electronics And Communication Engineering', 'Electronics And Communication Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Computer Science Engineering', 'Computer Science Engineering'), ('Material Science', 'Material Science'), ('Engineering Physics', 'Engineering Physics'), ('Mathematics And Computing', 'Mathematics And Computing')], default='', max_length=100)),
            ],
            options={
                'verbose_name': 'Interview Result',
                'verbose_name_plural': 'Interview Results',
            },
        ),
        migrations.AlterModelOptions(
            name='resultpage',
            options={'verbose_name': 'Result Page Content', 'verbose_name_plural': 'Result Page'},
        ),
    ]
