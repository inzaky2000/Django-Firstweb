# Generated by Django 5.0.3 on 2024-05-05 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_askqa_detail_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='myresearch',
            name='rs_abs_th',
            field=models.TextField(blank=True, null=True, verbose_name='บทคัดย่อ'),
        ),
    ]