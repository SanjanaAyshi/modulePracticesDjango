# Generated by Django 4.2.7 on 2024-01-01 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Musicians', '0003_initial'),
        ('Albums', '0002_alter_album_musician'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='musician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Musicians.musicians'),
        ),
    ]
