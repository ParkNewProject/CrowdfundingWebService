# Generated by Django 2.2.3 on 2019-07-30 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunding', '0002_auto_20190731_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crfproject',
            name='pType',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='crfproject',
            name='pid',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]