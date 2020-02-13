# Generated by Django 3.0.3 on 2020-02-13 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('full_name', models.CharField(blank=True, help_text="User's full name", max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('TRANSGENDER', 'TRANSGENDER'), ('PREFER_NOT_TO_SAY', 'PREFER_NOT_TO_SAY')], help_text="User's Gender", max_length=255, null=True)),
                ('email', models.EmailField(blank=True, default='', help_text="User's Email", max_length=255, null=True, unique=True)),
                ('mobile_number', models.CharField(blank=True, help_text="User's Mobile number", max_length=10, null=True)),
                ('profile_photo', models.ImageField(blank=True, help_text="User's Profile photo", max_length=255, null=True, upload_to='images_profilephoto')),
                ('pincode', models.CharField(help_text="User's Residential pincode", max_length=6)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
