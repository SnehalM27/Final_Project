# Generated by Django 4.1.6 on 2023-02-10 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_generation', '0002_alter_application_business_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='business_type',
            field=models.CharField(blank=True, choices=[('Individual', 'Individual'), ('Partnership', 'Partnership'), ('Corporation', 'Corporation'), ('Propriership', 'Propritorship')], default=0, max_length=250),
        ),
        migrations.AlterField(
            model_name='business',
            name='business_type',
            field=models.CharField(blank=True, choices=[('Individual', 'Individual'), ('Partnership', 'Partnership'), ('Corporation', 'Corporation'), ('Propriership', 'Propritorship')], default=0, max_length=250),
        ),
    ]
