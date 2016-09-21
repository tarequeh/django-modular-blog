# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 05:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeFragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.TextField(choices=[(b'generic', b'Generic'), (b'python', b'Python'), (b'bash', b'Bash'), (b'javascript', b'JavaScript'), (b'html', b'HTML'), (b'css', b'CSS')], default=b'generic')),
            ],
        ),
        migrations.CreateModel(
            name='EmbedFragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('embed_type', models.TextField(choices=[(b'raw', b'Raw'), (b'vimeo', b'Vimeo'), (b'youtube', b'Youtube'), (b'tweet', b'Tweet'), (b'instagram', b'Instagram')], default=b'raw')),
            ],
        ),
        migrations.CreateModel(
            name='HTMLFragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_sanitized', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ImageFragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MarkdownFragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PlainTextFragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('tldr', models.TextField()),
                ('slug', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='organizations.Organization')),
            ],
        ),
        migrations.AddField(
            model_name='plaintextfragment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plain_text_fragments', to='fragments.Post'),
        ),
        migrations.AddField(
            model_name='markdownfragment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='markdown_fragments', to='fragments.Post'),
        ),
        migrations.AddField(
            model_name='imagefragment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_fragments', to='fragments.Post'),
        ),
        migrations.AddField(
            model_name='htmlfragment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='html_fragments', to='fragments.Post'),
        ),
        migrations.AddField(
            model_name='embedfragment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='embed_fragments', to='fragments.Post'),
        ),
        migrations.AddField(
            model_name='codefragment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='code_fragments', to='fragments.Post'),
        ),
    ]
