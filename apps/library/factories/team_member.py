import factory
from faker import Faker

from apps.core.decorators import restrict_factory
from apps.core.models import Person, Role, RoleType
from apps.library.models import TeamMember

fake = Faker("ru_RU")


@restrict_factory(general=(Person, Role))
class TeamMemberFactory(factory.django.DjangoModelFactory):
    """Create TeamMember object.

    The factory will fail if non of `performance` or `reading` or `masterclass`
    is set during call.

    Default behavior: the factory sets random but permitted roles based on the
    type of related objects: masterclass, reading, or performance. It's model
    logic: team_member could be connected to only one of these objects.

    Parameters:
    1. `set_role_with_slug=<str>`: if the parameter is set the factory will use
    that role instead of a random one. Please use with caution: with that
    parameter, you can set any of existed roles, even with an incorrect role
    type.
    """

    class Meta:
        model = TeamMember
        django_get_or_create = (
            "person",
            "role",
            "performance",
            "reading",
            "masterclass",
        )

    performance = None
    reading = None
    masterclass = None

    @factory.lazy_attribute
    def person(self):
        return Person.objects.order_by("?").first()

    @factory.lazy_attribute
    def role(self):
        if self.performance:
            role_type = RoleType.objects.filter(role_type="performanse_role")
        if self.reading:
            role_type = RoleType.objects.filter(role_type="reading_role")
        if self.masterclass:
            role_type = RoleType.objects.filter(role_type="master_class_role")

        allowable_roles = Role.objects.filter(types__in=role_type)
        allowable_random_role = allowable_roles.order_by("?").first()
        return allowable_random_role

    @factory.post_generation
    def set_role_with_slug(self, create, role_slug, **kwargs):
        """Override the `role` attribute with the role that matches `role_slug`."""
        if create and role_slug:
            role = Role.objects.get(slug=role_slug)
            self.role = role
