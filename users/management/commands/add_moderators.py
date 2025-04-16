from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from mailing.models import Mailing, Receiver
from users.models import User


class Command(BaseCommand):
    help = "Add Moderators group to the database"

    def handle(self, *args, **kwargs):
        # Create of get group Moderators
        moderators_group, created = Group.objects.get_or_create(name="Moderators")

        # Get content for model Mailing
        content_type_mailing = ContentType.objects.get_for_model(Mailing)

        # Get content for model Receiver
        content_type_receiver = ContentType.objects.get_for_model(Receiver)

        # Get content for model User
        content_type_user = ContentType.objects.get_for_model(User)

        # Get permissions for view_all_mailings
        view_all_mailings_permission = Permission.objects.get(
            codename="view_all_mailings", content_type=content_type_mailing
        )

        # Get permissions for deactivate_mailings
        deactivate_mailings_permission = Permission.objects.get(
            codename="deactivate_mailings", content_type=content_type_mailing
        )

        # Get permissions for view_all_users
        view_all_users_permission = Permission.objects.get(
            codename="view_all_users", content_type=content_type_user
        )

        # Get permissions for deactivate_users
        deactivate_users_permission = Permission.objects.get(
            codename="deactivate_user", content_type=content_type_user
        )

        # Get permissions for view_all_receivers
        view_all_receivers_permission = Permission.objects.get(
            codename="view_all_receivers", content_type=content_type_receiver
        )

        # Add permissions to group Moderators
        moderators_group.permissions.add(
            view_all_mailings_permission,
            view_all_receivers_permission,
            deactivate_mailings_permission,
            view_all_users_permission,
            deactivate_users_permission,
        )

        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    "Group Moderators is created and permission has been added"
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("Group Moderators exists, permissions updated")
            )
