# Generated by Django 4.2.7 on 2023-12-05 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baza_przepisow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='measurement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='baza_przepisow.measurementunit'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='measurement_qty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='baza_przepisow.measurementquantity'),
        ),
    ]
