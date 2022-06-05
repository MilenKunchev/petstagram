# Generated by Django 4.0.5 on 2022-06-05 12:20

from django.db import migrations, models
import petstagram.main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_profile_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', validators=[petstagram.main.validators.validate_file_max_size_in_mb])),
                ('description', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('tagged_pets', models.ManyToManyField(to='main.pet')),
            ],
        ),
    ]
