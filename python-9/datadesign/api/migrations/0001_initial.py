# Generated by Django 3.0.7 on 2020-06-13 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('status', models.BooleanField(verbose_name='status')),
                ('env', models.CharField(max_length=20, verbose_name='env')),
                ('version', models.CharField(max_length=5, verbose_name='version')),
                ('address', models.CharField(max_length=39, verbose_name='adress')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('last_login', models.DateField(verbose_name='last_login')),
                ('email', models.CharField(max_length=254, verbose_name='email')),
                ('password', models.CharField(max_length=50, verbose_name='password')),
            ],
        ),
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Agent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=20, verbose_name='level')),
                ('data', models.DateField(verbose_name='data')),
                ('arquivado', models.BooleanField(verbose_name='arquivado')),
                ('date', models.DateField(verbose_name='date')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Agent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
    ]