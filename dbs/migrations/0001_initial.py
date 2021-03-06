# Generated by Django 2.0.4 on 2018-04-07 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractTools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('input_value', models.CharField(max_length=300)),
                ('output_value', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steps_id', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('abstracttools_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dbs.AbstractTools')),
                ('username', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=300)),
                ('hostname', models.CharField(max_length=300)),
            ],
            bases=('dbs.abstracttools',),
        ),
        migrations.CreateModel(
            name='Diamond',
            fields=[
                ('abstracttools_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dbs.AbstractTools')),
            ],
            bases=('dbs.abstracttools',),
        ),
        migrations.CreateModel(
            name='Parabola',
            fields=[
                ('abstracttools_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dbs.AbstractTools')),
                ('types', models.CharField(max_length=300)),
            ],
            bases=('dbs.abstracttools',),
        ),
        migrations.CreateModel(
            name='Square',
            fields=[
                ('abstracttools_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dbs.AbstractTools')),
                ('files', models.FileField(upload_to='./data/yml')),
            ],
            bases=('dbs.abstracttools',),
        ),
        migrations.AddField(
            model_name='steps',
            name='actiontool_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dbs.AbstractTools'),
        ),
        migrations.AddField(
            model_name='steps',
            name='workflow_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dbs.Workflow'),
        ),
    ]
