# Generated by Django 3.1.2 on 2021-01-17 15:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0004_auto_20210113_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curexptlect2',
            old_name='no_of_part',
            new_name='no_of_Participants',
        ),
        migrations.RenameField(
            model_name='curguestlect1',
            old_name='no_of_part',
            new_name='no_of_Participants',
        ),
        migrations.RenameField(
            model_name='curstudsponsor5',
            old_name='comp_rep',
            new_name='company_Representative',
        ),
        migrations.RenameField(
            model_name='curstudsponsor5',
            old_name='comp_sponsor',
            new_name='sponsoring_Company',
        ),
        migrations.RenameField(
            model_name='curstudvisit4',
            old_name='fac_name',
            new_name='faculty_Name',
        ),
        migrations.RenameField(
            model_name='curstudvisit4',
            old_name='no_of_stud',
            new_name='no_of_Students',
        ),
        migrations.RenameField(
            model_name='deptevent1',
            old_name='guest_affl',
            new_name='guest_Affiliation',
        ),
        migrations.RenameField(
            model_name='deptevent1',
            old_name='no_of_part',
            new_name='no_of_Participants',
        ),
        migrations.RenameField(
            model_name='deptevent2',
            old_name='act_name',
            new_name='activity_name',
        ),
        migrations.RenameField(
            model_name='deptevent2',
            old_name='fac_name',
            new_name='faculty_name',
        ),
        migrations.RenameField(
            model_name='deptevent2',
            old_name='part_no',
            new_name='no_of_Participants',
        ),
        migrations.RenameField(
            model_name='deptevent2',
            old_name='school_cont',
            new_name='school_Contact',
        ),
        migrations.RenameField(
            model_name='deptfacultydev4',
            old_name='amm_sponsored',
            new_name='amount_Sponsored',
        ),
        migrations.RenameField(
            model_name='deptfacultydev4',
            old_name='no_of_part',
            new_name='no_of_Participants',
        ),
        migrations.RenameField(
            model_name='deptproevent3',
            old_name='no_of_part',
            new_name='no_of_Participants',
        ),
        migrations.RenameField(
            model_name='deptstartup6',
            old_name='LLP_no',
            new_name='LLP_number',
        ),
        migrations.RenameField(
            model_name='deptstudpart5',
            old_name='no_of_part',
            new_name='no_of_Participants',
        ),
        migrations.RenameField(
            model_name='deptstudpart5',
            old_name='org_inst',
            new_name='organising_Institute',
        ),
        migrations.RenameField(
            model_name='facachieve',
            old_name='fac_name',
            new_name='faculty_Name',
        ),
        migrations.RenameField(
            model_name='studfac5',
            old_name='no_of_participants',
            new_name='no_of_Participants',
        ),
        migrations.AlterField(
            model_name='confinternational5',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='confnational6',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='curexptlect2',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='curguestlect1',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='curstudtrain3',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='curstudvisit4',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='deptevent1',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='deptfacultydev4',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='deptproevent3',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='deptstudpart5',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='facachieve',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='facevents8',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='facevents8',
            name='level',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='facpatents10',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='facpatents10',
            name='patent_Number',
            field=models.IntegerField(verbose_name='Patent/Application Number'),
        ),
        migrations.AlterField(
            model_name='professionalprac9',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='resinternational3',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='resnational4',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='resproject1',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AlterField(
            model_name='studentresult',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.CreateModel(
            name='NationalAttend11',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_Name', models.CharField(max_length=150)),
                ('conference_Name', models.CharField(max_length=150, verbose_name='Name of the Conference')),
                ('organised_By', models.CharField(max_length=150)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('amount', models.IntegerField(default=0, verbose_name='Amount (if paid by institute)')),
                ('location', models.CharField(max_length=150)),
                ('department', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
        ),
        migrations.CreateModel(
            name='InternationalAttend12',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_Name', models.CharField(max_length=150)),
                ('conference_Name', models.CharField(max_length=150, verbose_name='Name of the Conference')),
                ('organised_By', models.CharField(max_length=150)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('amount', models.IntegerField(default=0, verbose_name='Amount (if paid by institute)')),
                ('location', models.CharField(max_length=150)),
                ('department', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
        ),
    ]
