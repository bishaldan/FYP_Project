# Generated by Django 5.0 on 2024-03-02 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_student_fee_student_first_name_student_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
