# Generated by Django 3.2.5 on 2021-08-18 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elevageAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vitamine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='', max_length=100)),
                ('description', models.CharField(blank=True, default='description not available', max_length=100)),
                ('date_debut', models.DateField(default='2021-06-20')),
                ('date_fin', models.DateField(default='2021-06-20')),
                ('prix', models.IntegerField(default=0)),
                ('etat', models.CharField(choices=[('Inachevé', 'Inachevé'), ('Achevé', 'Achevé')], default='Inachevé', max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='', max_length=20)),
                ('date_prescrit', models.DateField(default='2021-06-20')),
                ('description', models.CharField(blank=True, default='description not available', max_length=100)),
                ('prix_unitaire', models.CharField(blank=True, default='000', max_length=20)),
                ('prix_total', models.IntegerField(default=0)),
                ('etat', models.CharField(choices=[('Inachevé', 'Inachevé'), ('Achevé', 'Achevé')], default='Inachevé', max_length=9)),
                ('elevage', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='elevageAPI.elevage')),
            ],
        ),
        migrations.CreateModel(
            name='Nourriture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField(default='2021-06-20')),
                ('date_fin', models.DateField(default='2021-06-20')),
                ('quantité_journalière', models.IntegerField(default=1)),
                ('total_journalière', models.IntegerField(default=1)),
                ('quantité_total', models.IntegerField(default=1)),
                ('etat', models.CharField(choices=[('En cours', 'En cours'), ('Terminé', 'Terminé')], default='En cours', max_length=9)),
                ('details', models.CharField(blank=True, default='Aucune informations', max_length=200)),
                ('prix', models.IntegerField(default=1)),
                ('poids_estimé', models.CharField(blank=True, default='000', max_length=20)),
                ('poids_prelevé', models.IntegerField(default=0)),
                ('observation', models.CharField(choices=[('NaN', 'NaN'), ('Anormal', 'Anormal'), ('Normal', 'Normal'), ('Excellent', 'Excellent')], default='NaN', max_length=15)),
                ('elevage', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='elevageAPI.elevage')),
            ],
        ),
        migrations.CreateModel(
            name='Eau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField(default='2021-06-20')),
                ('date_fin', models.DateField(default='2021-06-20')),
                ('quantité_journalière', models.IntegerField(default=0)),
                ('total_journalière', models.IntegerField(default=0)),
                ('quantité_total', models.IntegerField(default=0)),
                ('etat', models.CharField(choices=[('En cours', 'En cours'), ('Terminé', 'Terminé')], default='En cours', max_length=9)),
                ('prix', models.IntegerField(default=0)),
                ('elevage', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='elevageAPI.elevage')),
            ],
        ),
    ]