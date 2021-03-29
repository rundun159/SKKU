# Generated by Django 3.0.7 on 2020-06-09 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maritime', '0002_auto_20200609_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ship_rejected',
            fields=[
                ('ship_name', models.CharField(help_text='name of ship', max_length=20, primary_key=True, serialize=False)),
                ('age', models.IntegerField(default=0)),
                ('ship_comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maritime.Comp')),
            ],
        ),
        migrations.CreateModel(
            name='Plan_rejected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.DateField()),
                ('arrival', models.DateField()),
                ('plan_comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maritime.Comp')),
                ('plan_port1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depart_rejected', to='maritime.Port')),
                ('plan_port2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrive_rejected', to='maritime.Port')),
                ('plan_ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maritime.Ship_stored')),
            ],
        ),
        migrations.CreateModel(
            name='Mate_rejected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mate_name', models.CharField(help_text='name of mate', max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField(default=0)),
                ('mate_comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maritime.Comp')),
            ],
        ),
        migrations.CreateModel(
            name='Eng_rejected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_name', models.CharField(help_text='name of Engineer', max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField(default=0)),
                ('eng_comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maritime.Comp')),
            ],
        ),
    ]
