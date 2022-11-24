# Generated by Django 4.1.3 on 2022-11-24 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Estudante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('data_nascimento', models.DateTimeField()),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], default='Feminino', max_length=150)),
                ('minicursos', models.ManyToManyField(to='painel.minicurso')),
            ],
        ),
    ]