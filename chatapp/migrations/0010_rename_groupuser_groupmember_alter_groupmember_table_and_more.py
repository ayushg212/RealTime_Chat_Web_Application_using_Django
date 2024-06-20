# Generated by Django 5.0.6 on 2024-06-19 19:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0009_groupjoinrequest'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GroupUser',
            new_name='GroupMember',
        ),
        migrations.AlterModelTable(
            name='groupmember',
            table=None,
        ),
        migrations.CreateModel(
            name='MessageReadTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.groupmessage')),
                ('read_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='MessageReadBy',
        ),
    ]