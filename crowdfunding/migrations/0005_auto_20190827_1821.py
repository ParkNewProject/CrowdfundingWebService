# Generated by Django 2.2.3 on 2019-08-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunding', '0004_auto_20190822_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contribute',
            old_name='pid',
            new_name='contrib_pid',
        ),
        migrations.AddField(
            model_name='contribute',
            name='contrib_coin',
            field=models.IntegerField(default=0, verbose_name='후원 코인'),
        ),
        migrations.AddField(
            model_name='crfproject',
            name='goalcoin',
            field=models.IntegerField(default=0, verbose_name='목표 코인'),
        ),
        migrations.AddField(
            model_name='crfproject',
            name='nowcoin',
            field=models.IntegerField(default=0, verbose_name='현재 모금 코인'),
        ),
    ]