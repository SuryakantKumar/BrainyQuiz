# Generated by Django 2.2 on 2020-06-25 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20200625_1901'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scoreboard',
            options={'ordering': ['-score']},
        ),
        migrations.AddField(
            model_name='questionwisequizscore',
            name='answer_triggered',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
