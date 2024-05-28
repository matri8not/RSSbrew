# Generated by Django 5.0.6 on 2024-05-28 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeedManager', '0008_article_summary_one_line'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='custom_prompt',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='processedfeed',
            name='summary_language',
            field=models.CharField(default='English', help_text='Language for summarization, will be ignored if summarization is disabled or using custom prompt.', max_length=20),
        ),
    ]