# Generated by Django 3.2.6 on 2022-05-06 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_title', models.CharField(max_length=200)),
                ('review_body', models.TextField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('profiles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('prouduct_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phone.product')),
            ],
            options={
                'unique_together': {('prouduct_review', 'profiles')},
            },
        ),
    ]
