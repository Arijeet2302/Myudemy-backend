# Generated by Django 4.2.4 on 2023-08-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_courses_courses_rating_constraint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product_name',
            new_name='course_name',
        ),
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
