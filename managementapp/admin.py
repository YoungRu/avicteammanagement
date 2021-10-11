from django.contrib import admin
from .models import UserReg
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('Assign_Time',)
class UserRegAdmin(admin.ModelAdmin):
    readonly_fields = ('Date_Joined',)


admin.site.register(Todo, TodoAdmin)
admin.site.register(UserReg, UserRegAdmin)