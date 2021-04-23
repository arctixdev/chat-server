# Generated by Django 3.1.7 on 2021-04-15 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatBackend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='messageFrom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='chatBackend.persons'),
        ),
        migrations.CreateModel(
            name='groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=20, verbose_name='Name')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('person', models.ManyToManyField(to='chatBackend.persons')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='messages',
            name='messageTo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='chatBackend.groups'),
        ),
    ]