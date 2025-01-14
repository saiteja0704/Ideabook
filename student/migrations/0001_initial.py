# Generated by Django 2.0.3 on 2021-02-22 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentIdea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Fovourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NewIdea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('uploadpic', models.ImageField(upload_to='pic_folder/')),
                ('content', models.CharField(max_length=250)),
                ('dateofpublish', models.CharField(default='2020', max_length=4)),
                ('dateandtime', models.DateTimeField(default='2020-12-12 10:00:00')),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=250)),
                ('userid', models.CharField(max_length=250, unique=True)),
                ('password', models.CharField(max_length=250)),
                ('confirmpassword', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='newidea',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
        migrations.AddField(
            model_name='fovourite',
            name='newideaid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.NewIdea'),
        ),
        migrations.AddField(
            model_name='fovourite',
            name='studentid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
        migrations.AddField(
            model_name='commentidea',
            name='newideaid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.NewIdea'),
        ),
        migrations.AddField(
            model_name='commentidea',
            name='studentid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]
