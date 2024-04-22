# Generated by Django 4.1 on 2024-04-21 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_jellydonut_maplebacon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cruller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('Regular', 'Regular'), ('Donut Hole', 'Donut Hole')], max_length=20)),
                ('flavor', models.CharField(choices=[('Cruller', 'Cruller')], max_length=20)),
                ('image', models.ImageField(upload_to='Cruller_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Smore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('Regular', 'Regular'), ('Donut Hole', 'Donut Hole')], max_length=20)),
                ('flavor', models.CharField(choices=[('Smore', 'Smore')], max_length=20)),
                ('image', models.ImageField(upload_to='Smore_images/')),
            ],
        ),
    ]
