from django.contrib import admin
from testapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
	list_display=["eno", "esal", "ename", "eaddr"]
	search_fields = ["ename"]
	list_filter = ["esal"]

admin.site.site_header = "Tapan Admin"
admin.site.index_title = "Employee Management"
admin.site.register(Employee, EmployeeAdmin)
