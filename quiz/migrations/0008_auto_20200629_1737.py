# Generated by Django 2.2 on 2020-06-29 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20200626_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]