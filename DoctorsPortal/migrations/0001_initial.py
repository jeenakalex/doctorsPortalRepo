# Generated by Django 3.2.4 on 2021-06-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(default='')),
                ('name', models.CharField(default='', max_length=100)),
                ('age', models.IntegerField(default='')),
                ('email', models.CharField(default='', max_length=100)),
                ('mobile', models.IntegerField(default='')),
                ('password', models.CharField(default='', max_length=100)),
                ('dattimeCreated', models.DateTimeField()),
                ('intLastAction', models.IntegerField(default='')),
            ],
        ),
    ]
