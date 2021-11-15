# Generated by Django 3.2.9 on 2021-11-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researcher', '0002_researcher_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchTeamAuth',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='universal id')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='universal create time')),
                ('researcher_id', models.BigIntegerField(verbose_name='id of the researcher/team member')),
                ('team_id', models.BigIntegerField(verbose_name='id of the team')),
                ('state', models.IntegerField(default=0, verbose_name='the state of this invitation')),
                ('role_tag', models.CharField(default='', max_length=64, verbose_name='role of the invitee')),
            ],
            options={
                'db_table': 'researcher_research_team_auth',
            },
        ),
    ]
