# Generated by Django 4.0.4 on 2022-04-24 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meme_id', models.IntegerField()),
                ('author_id', models.IntegerField()),
                ('url', models.CharField(max_length=1200)),
                ('likes', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
