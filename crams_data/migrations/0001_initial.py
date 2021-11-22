# Generated by Django 3.1.1 on 2021-03-16 03:37
import os

from django.db import migrations


def load_eresearch_body_systems_from_sql():
    file_name = 'eresearch_body_system.sql'
    sqls_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../sqls'))
    sql_statements = open(os.path.join(sqls_dir, file_name), 'r').read()

    return sql_statements


def load_zones_from_sql():
    file_name = 'zones.sql'
    sqls_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../sqls'))
    sql_statements = open(os.path.join(sqls_dir, file_name), 'r').read()
    return sql_statements


def load_allocation_homes_from_sql():
    file_name = 'allocation_home.sql'
    sqls_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../sqls'))
    print('sqls_dir: {}'.format(sqls_dir))
    sql_statements = open(os.path.join(sqls_dir, file_name), 'r').read()
    print('sql_statements: {}'.format(sql_statements))
    return sql_statements


def load_storage_products_from_sql():
    file_name = 'storage_products.sql'
    sqls_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../sqls'))
    sql_statements = open(os.path.join(sqls_dir, file_name), 'r').read()

    return sql_statements


def load_compute_products_from_sql():
    file_name = 'compute_products.sql'
    sqls_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../sqls'))
    sql_statements = open(os.path.join(sqls_dir, file_name), 'r').read()

    return sql_statements


def load_contact_roles_from_sql():
    file_name = 'contact_roles.sql'
    sqls_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../sqls'))
    sql_statements = open(os.path.join(sqls_dir, file_name), 'r').read()

    return sql_statements


def load_questions_from_sql():
    file_name = 'questions.sql'
    sqls_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../sqls'))
    sql_statements = open(os.path.join(sqls_dir, file_name), 'r').read()

    return sql_statements


def load_support_email_from_sql():
    file_name = 'support_email.sql'
    sqls_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../sqls'))
    sql_statements = open(os.path.join(sqls_dir, file_name), 'r').read()

    return sql_statements


def load_email_notification_from_sql():
    file_name = 'email_notifcation_templetes.sql'
    sqls_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../sqls'))
    sql_statements = open(os.path.join(sqls_dir, file_name), 'r').read()
    return sql_statements


def load_member_notification_from_sql():
    file_name = 'member_notification_templates.sql'
    sqls_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../sqls'))
    sql_statements = open(os.path.join(sqls_dir, file_name), 'r').read()
    return sql_statements


def load_org_faculty_from_sql():
    file_name = 'organisation_faculty_department.sql'
    sqls_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../sqls'))
    sql_statements = open(os.path.join(sqls_dir, file_name), 'r').read()
    return sql_statements


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.RunSQL(load_eresearch_body_systems_from_sql()),
        migrations.RunSQL(load_zones_from_sql()),
        migrations.RunSQL(load_allocation_homes_from_sql()),
        migrations.RunSQL(load_storage_products_from_sql()),
        migrations.RunSQL(load_compute_products_from_sql()),
        migrations.RunSQL(load_contact_roles_from_sql()),
        migrations.RunSQL(load_questions_from_sql()),
        migrations.RunSQL(load_support_email_from_sql()),
        migrations.RunSQL(load_org_faculty_from_sql()),
        migrations.RunSQL(load_email_notification_from_sql()),
        migrations.RunSQL(load_member_notification_from_sql()),
    ]
