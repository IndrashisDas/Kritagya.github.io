# Generated by Django 2.0.6 on 2018-08-31 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Branch', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='register',
            name='Branch',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Newapp.Branches'),
        ),
    ]
