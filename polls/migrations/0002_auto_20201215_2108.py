# Generated by Django 3.1.3 on 2020-12-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name': 'Note', 'verbose_name_plural': 'Notes'},
        ),
        migrations.AddField(
            model_name='notes',
            name='author',
            field=models.CharField(default='no one', max_length=50, verbose_name='author'),
        ),
    ]
