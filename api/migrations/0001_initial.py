# Generated by Django 4.0 on 2022-02-05 19:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'areas',
                'ordering': ['name', 'created'],
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descrpiption', models.TextField(blank=True, default='', max_length=500)),
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'db_table': 'journals',
                'ordering': ['name', 'created'],
            },
        ),
        migrations.CreateModel(
            name='MoodLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.CharField(choices=[('happy', 'happy'), ('sad', 'sad'), ('none', 'none'), ('love', 'love'), ('angry', 'angry')], default='none', max_length=10)),
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('note', models.TextField(default='')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.journal')),
            ],
            options={
                'db_table': 'mood_logs',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('notion', models.CharField(choices=[('good', 'good'), ('bad', 'bad')], default='good', max_length=10)),
                ('time_preffered', models.CharField(choices=[('morning', 'morning'), ('afternoon', 'afternoon'), ('evening', 'evening'), ('all', 'all')], default='all', max_length=20)),
                ('count_a_day', models.IntegerField(default=1)),
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('completed', models.IntegerField(default=0)),
                ('skipped', models.IntegerField(default=0)),
                ('failed', models.IntegerField(default=0)),
                ('streak', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.area')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.journal')),
            ],
            options={
                'db_table': 'habits',
                'ordering': ['name', 'created'],
            },
        ),
        migrations.CreateModel(
            name='HabitLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('completed', 'completed'), ('fail', 'fail'), ('skip', 'skip')], max_length=10)),
                ('notes', models.TextField(blank=True, default='', null=True)),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.habits')),
            ],
            options={
                'db_table': 'habit_logs',
            },
        ),
    ]
