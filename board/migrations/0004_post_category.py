# Generated by Django 4.2.20 on 2025-04-24 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_delete_boardpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('자유게시판', '자유게시판'), ('Q&A', 'Q&A'), ('잡담', '잡담')], default='자유게시판', max_length=20),
        ),
    ]
