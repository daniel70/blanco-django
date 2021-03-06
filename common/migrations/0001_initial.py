# Generated by Django 3.1.1 on 2020-09-11 15:14
from django.contrib.postgres import operations
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        # these extension operations only work when the user is a superuser
        # normally this is bad practise so your options are:
        # 1. run the first migrations as superuser and then remove superuser priviledge
        # 2. remove the extensions from this migrations and manually run these statements as superuser:
        #    - create extension if not exists hstore;
        #    - create extension if not exists citext;
        #    - create extension if not exists unaccent;

        operations.HStoreExtension(),
        operations.CITextExtension(),
        operations.UnaccentExtension(),

        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=254)),
                ('last_name', models.CharField(blank=True, max_length=254)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
