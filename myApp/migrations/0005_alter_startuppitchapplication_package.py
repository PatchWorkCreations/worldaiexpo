# Generated by Django 5.1.2 on 2025-06-23 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_startuppitchapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startuppitchapplication',
            name='package',
            field=models.CharField(choices=[('Startup Pitching + 1 Regular Ticket', 'Startup Pitching + 1 Regular Ticket'), ('Startup + 5 Regular Tickets + Table Top', 'Startup + 5 Regular Tickets + Table Top'), ('Startup Pitching + 5 Regular Tickets', 'Startup Pitching + 5 Regular Tickets'), ('Startup Pitching + 2 VIP Tickets', 'Startup Pitching + 2 VIP Tickets'), ('Startup Pitching + 3 VIP Tickets', 'Startup Pitching + 3 VIP Tickets'), ('Startup Pitching + 5 VIP Tickets', 'Startup Pitching + 5 VIP Tickets')], max_length=255),
        ),
    ]
