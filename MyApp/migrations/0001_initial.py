# Generated by Django 3.0.4 on 2020-06-22 07:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(unique=True)),
                ('desc', models.TextField()),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/')),
                ('alternative_text', models.TextField()),
                ('title', models.TextField(default='NONE')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('fname_1', models.CharField(max_length=20)),
                ('lname_1', models.CharField(max_length=20)),
                ('year_1', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('fname_2', models.CharField(max_length=20)),
                ('lname_2', models.CharField(max_length=20)),
                ('year_2', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('fname_3', models.CharField(max_length=20)),
                ('lname_3', models.CharField(max_length=20)),
                ('year_3', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('desc', models.TextField()),
                ('url_link', models.URLField(default='http://127.0.0.1:8000/events')),
                ('document', models.FileField(blank=True, upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31)])),
                ('month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=12)),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030)])),
                ('title', models.TextField(unique=True)),
                ('desc', models.TextField()),
                ('pic', models.ImageField(upload_to='events_poster/')),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('End_time', models.DateTimeField()),
                ('url_link', models.URLField(blank=True, default='http://127.0.0.1:8000/events')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Resource')),
                ('winners', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Winner')),
            ],
        ),
    ]