# Generated by Django 3.2.23 on 2024-02-11 13:08

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_sight', '0003_auto_20240210_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherProfileDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('expertise', models.CharField(max_length=100)),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('availability', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='review',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='teacherprofile',
            name='availability',
        ),
        migrations.RemoveField(
            model_name='teacherprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='teacherprofile',
            name='expertise',
        ),
        migrations.RemoveField(
            model_name='teacherprofile',
            name='hourly_rate',
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='profile_image'),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
