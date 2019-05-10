# Generated by Django 2.2 on 2019-05-01 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('score', models.CharField(choices=[('별로 추천하지 않아요', '노잼'), ('입문자가 쉽게 볼 수 있는 책이에요', '순한 맛'), ('유익하지만 어려운 책이에요', '몸에 좋은 맛'), ('교과서 같이 자세히 공부할 수 있는 책이에요', '교과서'), ('선택하지 않음', '----')], default='선택하지 않음', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='review.Review')),
            ],
        ),
    ]
