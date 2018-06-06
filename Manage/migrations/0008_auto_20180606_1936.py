# Generated by Django 2.0.2 on 2018-06-06 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Manage', '0007_student_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('birthday', models.DateField()),
                ('email', models.CharField(max_length=30)),
                ('phoneNumber', models.CharField(max_length=30)),
                ('wage', models.IntegerField()),
                ('role', models.CharField(choices=[('1', 'Manager'), ('2', 'Assistant Manager'), ('3', 'Trainer'), ('4', 'Assistant Trainer'), ('5', 'Events organizer'), ('6', 'Cleaner')], max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='training',
            name='trainer',
        ),
        migrations.DeleteModel(
            name='Trainer',
        ),
        migrations.AddField(
            model_name='training',
            name='employee',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Manage.Employee'),
            preserve_default=False,
        ),
    ]
