from django.db import migrations

def create_data(apps, schema_editor):
    Student = apps.get_model('students', 'Student')
    Student(name="Joe Silver", email="joe@email.com", document="22342342", phone="00000000").save()

class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]

# Generated by Django 4.1.1 on 2022-09-22 20:39

# from django.db import migrations


# class Migration(migrations.Migration):

#     dependencies = [
#         ('students', '0001_initial'),
#     ]

#     operations = [
#     ]
