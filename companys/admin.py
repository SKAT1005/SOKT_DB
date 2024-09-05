from django.contrib import admin
from import_export import resources
from .models import HR



from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.widgets import BooleanWidget
from io import BytesIO
import openpyxl
from openpyxl.writer.excel import save_workbook

from .models import HR

class HRResource(resources.ModelResource):
    fio = Field(column_name='ФИО', attribute='fio')
    org_name = Field(column_name='Название организации', attribute='org_name')
    org_email = Field(column_name='Почта организации', attribute='org_email')
    org_type = Field(column_name='Тип организации', attribute='org_type')

    class Meta:
        model = HR
        fields = ('fio', 'org_name', 'org_email')
        export_order = ('fio', 'org_name', 'org_email')

    def export_data(self, queryset, fields, many_to_many_fields=None,
                   use_natural_foreign_keys=False, return_headers=False):
        """
        Export data as Excel file with UTF-8 encoding.
        """
        data = super().export_data(
            queryset, fields, many_to_many_fields, use_natural_foreign_keys,
            return_headers
        )

        workbook = openpyxl.Workbook()
        worksheet = workbook.active

        for row_index, row in enumerate(data):
            for col_index, value in enumerate(row):
                worksheet.cell(row=row_index + 1, column=col_index + 1).value = value

        output = BytesIO()
        save_workbook(workbook, output, encoding="utf-8")

        return output.getvalue()


@admin.register(HR)
class HRAdmin(ImportExportModelAdmin):
    resource_class = HRResource
    list_filter = ('excursion', 'practices', 'event', 'org_type')
