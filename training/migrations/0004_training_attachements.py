# Generated by Django 4.1.7 on 2023-06-02 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_resourceperson'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='attachements',
            field=models.FileField(default='', upload_to='attachments/'),
            preserve_default=False,
        ),
    ]