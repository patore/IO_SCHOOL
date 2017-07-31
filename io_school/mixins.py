from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


class MemberRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.free:
            return super(MemberRequiredMixin, self).dispatch(request, *args, **kwargs)

        return HttpResponse("Oops not free")


class StaffMemberRequiredMixin(object):
    @method_decorator(staff_member_required())
    def dispatch(self, request, *args, **kwargs):
        return super(StaffMemberRequiredMixin, self).dispatch(request, *args, **kwargs)
