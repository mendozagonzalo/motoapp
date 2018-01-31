from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin, ImportMixin, ImportExportModelAdmin

from establecimiento.models import Establecimiento, Departamento, Provincia, Distrito

class DepartamentoResource(resources.ModelResource):
    class Meta:
        model = Departamento
        fields = ('id', 'nombre')
        export_order = fields


class DepartamentoAdmin(ImportExportModelAdmin):
    resource_class = DepartamentoResource
    list_display = (
        'id',
        'nombre',

    )
    search_fields = (
        'id',
        'nombre',

    )


class ProvinciaResource(resources.ModelResource):
    class Meta:
        model = Provincia
        fields = ('id', 'nombre', 'departamento')
        export_order = fields


class ProvinciaAdmin(ImportExportModelAdmin):
    resource_class = ProvinciaResource
    list_display = (
        'id',
        'nombre',

    )
    search_fields = (
        'id',
        'nombre',

    )


class DistritoResource(resources.ModelResource):
    class Meta:
        model = Distrito
        fields = ('id', 'nombre', 'provincia', 'ubigeo')
        export_order = fields


class DistritoAdmin(ImportExportModelAdmin):
    resource_class = DistritoResource
    list_display = (
        'id',
        'nombre',

    )
    search_fields = (
        'id',
        'nombre',

    )

admin.site.register(Establecimiento)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Distrito, DistritoAdmin)

