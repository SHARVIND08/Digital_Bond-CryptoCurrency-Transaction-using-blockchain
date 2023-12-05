# Generated by Django 3.2.16 on 2022-11-17 04:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InversterProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('profile', models.ImageField(upload_to='profile/')),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('address', models.TextField()),
                ('org', models.CharField(max_length=255)),
                ('id_proff', models.FileField(upload_to='profileid/')),
                ('social_media', models.URLField(default='')),
                ('bank_name', models.CharField(blank=True, max_length=255)),
                ('holder_name', models.CharField(blank=True, max_length=255)),
                ('account_number', models.IntegerField(blank=True)),
                ('ifsc', models.CharField(blank=True, max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
