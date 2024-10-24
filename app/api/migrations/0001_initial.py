# Generated by Django 5.1.2 on 2024-10-23 13:42

import api.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('face_img', models.ImageField(blank=True, null=True, upload_to=api.models.student_directory_path)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]