# Generated by Django 4.2.4 on 2023-08-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_cart_course_id_alter_courses_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
