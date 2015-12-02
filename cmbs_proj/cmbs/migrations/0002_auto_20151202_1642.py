# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmbs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='cpn',
            field=models.DecimalField(max_digits=4, decimal_places=2, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='fifth_largest_tenant',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='fifth_lrg_tenant_exp_dt',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='fifth_lrg_tenant_pct',
            field=models.DecimalField(max_digits=4, decimal_places=2, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='fourth_largest_tenant',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='fourth_lrg_tenant_exp_dt',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='fourth_lrg_tenant_pct',
            field=models.DecimalField(max_digits=4, decimal_places=2, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='largest_tenant',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='lrg_tenant_exp_dt',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='lrg_tenant_pct',
            field=models.DecimalField(max_digits=4, decimal_places=2, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='protection',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='second_largest_tenant',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='second_lrg_tenant_exp_dt',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='second_lrg_tenant_pct',
            field=models.DecimalField(max_digits=4, decimal_places=2, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='third_largest_tenant',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='third_lrg_tenant_exp_dt',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='third_lrg_tenant_pct',
            field=models.DecimalField(max_digits=4, decimal_places=2, null=True),
        ),
    ]
