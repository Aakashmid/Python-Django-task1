# Generated by Django 5.0.3 on 2024-03-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profileImg',
            field=models.ImageField(default='app/profileImage/profile.jpg', upload_to='app/profileImage/', verbose_name='Profile Image'),
        ),
    ]
