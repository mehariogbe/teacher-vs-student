# Generated by Django 3.2.9 on 2021-11-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_course_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teachers',
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
