# Generated by Django 4.1.7 on 2023-04-03 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_alter_blog_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'permissions': [('can_delete_any_blog', 'Can delete any blog')]},
        ),
    ]