# Generated by Django 5.0.2 on 2024-04-04 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='Email_ID',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='Number',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='Password',
            new_name='password',
        ),
    ]
