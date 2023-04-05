# Generated by Django 3.0.2 on 2020-01-02 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('otp', models.CharField(max_length=6)),
                ('is_verified', models.BooleanField(default=False)),
                ('picture', models.ImageField(null=True, upload_to=None)),
                ('data', models.TextField(blank=True, null=True)),
                ('in_hash', models.CharField(max_length=8)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
