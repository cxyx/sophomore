# Generated by Django 3.1.13 on 2021-09-08 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkorderRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='工单角色名')),
                ('desc', models.CharField(default='', max_length=20, verbose_name='描述')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='workorder_role',
            field=models.ManyToManyField(blank=True, to='rbac.WorkorderRole', verbose_name='工单角色'),
        ),
    ]
