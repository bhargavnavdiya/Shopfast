# Generated by Django 3.1.1 on 2021-04-01 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopfasthome', '0004_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbackForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.IntegerField(max_length=5)),
                ('experience', models.CharField(max_length=500)),
                ('suggestion', models.CharField(max_length=500)),
            ],
        ),
    ]
