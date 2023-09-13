# Generated by Django 4.2.5 on 2023-09-13 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_added',
        ),
        migrations.AddField(
            model_name='product',
            name='aplikasi',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='kelas',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='nama',
            field=models.CharField(max_length=255, null=True),
        ),
    ]