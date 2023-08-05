# Generated by Django 2.2.12 on 2020-09-01 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corptools', '0031_auto_20200828_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactermarketorder',
            name='region_name',
            field=models.ForeignKey(
                default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corptools.MapRegion'),
        ),
        migrations.AddField(
            model_name='charactermarketorder',
            name='type_name',
            field=models.ForeignKey(
                default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corptools.EveItemType'),
        ),
        migrations.AddField(
            model_name='corporationmarketorder',
            name='region_name',
            field=models.ForeignKey(
                default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corptools.MapRegion'),
        ),
        migrations.AddField(
            model_name='corporationmarketorder',
            name='type_name',
            field=models.ForeignKey(
                default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corptools.EveItemType'),
        ),
    ]
