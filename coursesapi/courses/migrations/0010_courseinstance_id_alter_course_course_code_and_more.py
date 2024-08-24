# Generated by Django 5.1 on 2024-08-24 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_alter_course_course_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinstance',
            name='id',
            field=models.AutoField(default=12, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', to_field='course_code'),
        ),
    ]
