# Generated by Django 5.1.1 on 2024-09-16 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serije', '0002_alter_serije_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='serije',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='serije',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='serije',
            name='godina',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='serije',
            name='imdb_ocena',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='serije',
            name='originalni_naziv',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='serije',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='serije',
            name='title',
            field=models.CharField(max_length=120),
        ),
        migrations.CreateModel(
            name='Epizoda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epizode_date', models.DateField(auto_now_add=True)),
                ('sezona', models.CharField(blank=True, max_length=120, null=True)),
                ('ep', models.CharField(blank=True, max_length=120, null=True)),
                ('epizode_link', models.CharField(max_length=300)),
                ('epizode_preuzmi', models.CharField(default='', max_length=300)),
                ('epizode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serije.serije')),
            ],
        ),
    ]
