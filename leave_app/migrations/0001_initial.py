# Generated by Django 4.1.3 on 2022-11-19 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_starting_date', models.DateTimeField()),
                ('leave_ending_date', models.DateTimeField()),
                ('leave_applying_date', models.DateTimeField(auto_now_add=True)),
                ('Employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave_app.employe')),
            ],
        ),
    ]
