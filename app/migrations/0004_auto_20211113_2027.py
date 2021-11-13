# Generated by Django 3.2.9 on 2021-11-13 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211111_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='app.course'),
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('types', models.CharField(choices=[('L', 'Lab'), ('H', 'Homework'), ('P', 'Project')], max_length=1)),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=9999)),
                ('lab_deliverable', models.BooleanField(default=False)),
                ('ccreated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labs', to='app.course')),
            ],
        ),
    ]
