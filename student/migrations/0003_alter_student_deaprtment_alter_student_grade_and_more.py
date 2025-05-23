# Generated by Django 5.1.6 on 2025-02-21 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='deaprtment',
            field=models.CharField(choices=[('Bsc', 'Bsc'), ('B.Com', 'B.Com'), ('Bba', 'Bba')], max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mark',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
