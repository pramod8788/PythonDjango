# Generated by Django 4.0.1 on 2022-01-31 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_file_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='like',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], max_length=10, null=True),
        ),
    ]