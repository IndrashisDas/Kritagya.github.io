# Generated by Django 2.0.6 on 2018-08-31 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newapp', '0003_auto_20180831_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='branches',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='branches',
            name='Branch',
            field=models.CharField(max_length=5),
        ),
    ]
