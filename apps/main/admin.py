from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget

from apps.core.models import Setting
from apps.main.models import SettingEmail, SettingFirstScreen, SettingGeneral, SettingMain

BANNER_HELP_TEXT = "Возможные варианты значения для кнопки: TICKETS, READ, " "DETAILS."
BANNER_LABEL = "Банер (заголовок (title), описание(description), кнопка (" "button))"
NEWS_HELP_TEXT = (
    "При включении данной настройки, автоматический будет "
    "выключена настройка Отображение дневника на главной страницы"
)
BLOG_HELP_TEXT = (
    "При включении данной настройки, автоматический будет "
    "выключена настройка 'Отображение новостей на главной странице'"
)


@admin.register(SettingEmail, SettingGeneral, SettingMain, SettingFirstScreen)
class SettingAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "settings_key",
        "get_value",
        "group",
    )
    search_fields = (
        "field_type",
        "settings_key",
    )
    readonly_fields = (
        "field_type",
        "settings_key",
        "description",
    )

    def get_form(self, request, obj=None, **kwargs):
        widget = JSONEditorWidget(mode="form")
        form = super().get_form(request, obj, widgets={"json": widget}, **kwargs)
        if obj.field_type == Setting.SettingFieldType.BANNER:
            form.base_fields["json"].help_text = BANNER_HELP_TEXT
            form.base_fields["json"].label = BANNER_LABEL
        elif obj.settings_key == "main_add_blog":
            form.base_fields["boolean"].help_text = NEWS_HELP_TEXT
        elif obj.settings_key == "main_add_news":
            form.base_fields["boolean"].help_text = BLOG_HELP_TEXT
        return form

    def get_fields(self, request, obj=None):
        field_for_setting_value = Setting.TYPES_AND_FIELDS[obj.field_type]
        return (
            "description",
            "settings_key",
            "field_type",
            "group",
            field_for_setting_value,
        )

    @admin.display(description="Значение")
    def get_value(self, obj: object):
        """Return value of the setting object."""
        return obj.value

    def has_add_permission(self, request, obj=None):
        """Remove the save and add new button."""
        return False

    def has_delete_permission(self, request, obj=None):
        """Remove the delete button."""
        return False
