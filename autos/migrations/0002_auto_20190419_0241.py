# Generated by Django 2.1.5 on 2019-04-19 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='content_type',
            field=models.CharField(help_text='The MIMEType of the file', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='picture',
            field=models.BinaryField(editable=True, null=True),
        ),
    ]
