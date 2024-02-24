# Generated by Django 3.2.23 on 2024-02-24 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_sight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='teacher_profile',
            field=models.ForeignKey(default='Name', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='tutor_sight.teacherprofile'),
            preserve_default=False,
        ),
    ]