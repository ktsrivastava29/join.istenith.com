# Generated by Django 4.0.6 on 2022-08-08 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0015_rename_registration_closed_template_registeration_closed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='social_link',
            old_name='s_link',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='social_link',
            old_name='s_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='terms_n_condition',
            old_name='tc_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='terms_n_condition',
            old_name='tc_title',
            new_name='title',
        ),
    ]
