# Generated by Django 4.2.5 on 2023-09-11 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30, verbose_name='사용자 ID')),
                ('name', models.CharField(max_length=30, verbose_name='사용자 이름')),
                ('password', models.CharField(max_length=150, verbose_name='사용자 비밀번호')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('tag', models.CharField(max_length=30, verbose_name='태그')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='작성일')),
                ('img', models.ImageField(upload_to='', verbose_name='이미지 파일')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
