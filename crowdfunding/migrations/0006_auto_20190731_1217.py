# Generated by Django 2.2.3 on 2019-07-31 03:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunding', '0005_crfuser_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crfproject',
            name='email',
            field=models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='email',
            field=models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CrfUser',
        ),
    ]