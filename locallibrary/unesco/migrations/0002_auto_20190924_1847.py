# Generated by Django 2.1 on 2019-09-24 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='site',
            name='area_hectares',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='description',
            field=models.CharField(blank=True, help_text='description', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='justification',
            field=models.CharField(blank=True, help_text='justification', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='latitutde',
            field=models.DecimalField(decimal_places=7, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='longitude',
            field=models.DecimalField(decimal_places=7, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.Category'),
        ),
        migrations.AddField(
            model_name='site',
            name='iso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unesco.Iso'),
        ),
        migrations.AddField(
            model_name='site',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.Region'),
        ),
        migrations.AddField(
            model_name='site',
            name='states',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.States'),
        ),
    ]
