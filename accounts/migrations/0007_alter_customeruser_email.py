# Generated by Django 4.0.3 on 2022-03-07 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customeruser_driveruser_remove_user_confirm_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]