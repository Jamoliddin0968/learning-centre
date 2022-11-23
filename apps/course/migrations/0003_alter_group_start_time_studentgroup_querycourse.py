# Generated by Django 4.1.3 on 2022-11-23 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_student_teacher_alter_user_role'),
        ('course', '0002_alter_group_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='start_time',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_dae', models.DateField(auto_now_add=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.group')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student')),
            ],
        ),
        migrations.CreateModel(
            name='QueryCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student')),
            ],
        ),
    ]
