# Generated by Django 4.0.5 on 2022-06-15 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_book_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='station',
            field=models.CharField(choices=[('Mwiki', 'Mwiki - 6:22 AM'), ('Maji Mazuri', 'Maji Mazuri - 6:24 AM'), ('Kamutini', 'Kamutini - 6:27 AM'), ('Sunton', 'Sunton - 6:30 AM'), ('Hunters', 'Hunters - 6:33 AM')], max_length=50, null=True),
        ),
    ]
