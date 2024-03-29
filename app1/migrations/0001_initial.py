# Generated by Django 5.0.2 on 2024-02-21 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeFormater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('input_for_code', models.TextField()),
                ('output_for_code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProblemStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_statement', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TestCases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_case', models.TextField()),
                ('problem_statement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.problemstatement')),
            ],
        ),
    ]
