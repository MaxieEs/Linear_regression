# Generated by Django 4.0.1 on 2022-01-20 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class_name', models.CharField(max_length=50)),
                ('Class_size', models.IntegerField()),
                ('Class_Teacher', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=40)),
                ('Student_details', models.CharField(max_length=20)),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Regression.classes')),
            ],
        ),
    ]
