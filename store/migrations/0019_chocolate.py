# Generated by Django 4.1 on 2024-04-21 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_vanilla'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chocolate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('regular', 'Regular'), ('Donut Hole', 'Donut Hole')], max_length=20)),
                ('flavor', models.CharField(choices=[('Chocolate', 'Chocolate')], max_length=20)),
                ('image', models.ImageField(upload_to='Chocolate_images/')),
            ],
        ),
    ]
