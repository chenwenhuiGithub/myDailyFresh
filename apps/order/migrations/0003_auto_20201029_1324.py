# Generated by Django 3.1.1 on 2020-10-29 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201009_1630'),
        ('order', '0002_ordergoods_comment_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderinfo',
            old_name='order_status',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='addr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.address', verbose_name='收货地址'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='order_id',
            field=models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='transit_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='运费'),
        ),
    ]
