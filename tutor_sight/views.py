from django.shortcuts import render, get_object_or_404, redirect
from .models import TeacherProfile, Booking
from .forms import TeacherProfileForm, BookingForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView, ListView, View

class Index(ListView):
    model = TeacherProfile
    template_name = 'index.html'
    context_object_name = 'teacherprofiles'

    def get_queryset(self):
        return TeacherProfile.objects.all()

class TeacherProfileDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = TeacherProfile.objects.filter(status=1)
        TeacherProfile = get_object_or_404(queryset, slug=slug)

        reviews = Review.objects.filter(teacher_id=teacher_profile)
        bookings = Booking.objects.filter(teacher_id=teacher_profile)
                
        return render(
                request,
                "profile_detail.html",
                {
                    "teacherprofile": TeacherProfile,
                    "reviews": reviews,
                    "bookings": bookings,
                },
            )


@login_required
def create_booking(request, teacher_id):
    teacher = get_object_or_404(TeacherProfile, pk=teacher_id)
    print(teacher)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_detail', teacher_id=teacher_id)
    else:
        form = BookingForm()
    
    context = {
        'booking_form': form,
        'teacher_id': teacher_id,
        'teacher': teacher,
    }
    return render(request, 'create_booking.html', context)


@login_required
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(request, 'booking_confirm_delete.html', {'booking': booking})

