# Generated by Django 3.2.20 on 2023-07-29 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snowboard_blog', '0005_rename_parrent_comment_comment_parrent_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='parrent_id',
            new_name='parent_id',
        ),
    ]
