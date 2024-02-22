from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import TeacherProfile, Review, Booking, Comment
from .forms import TeacherProfileForm, BookingForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, View

class Index(ListView):
    model = TeacherProfile
    template_name = 'index.html'
    context_object_name = 'teacherprofiles'

    def get_queryset(self):
        return TeacherProfile.objects.all()

class ReviewDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = TeacherProfile.objects.filter(status=1)
        TeacherProfile = get_object_or_404(queryset, slug=slug)

        reviews = Review.objects.filter(teacher_id=teacher_profile)
        bookings = Booking.objects.filter(teacher_id=teacher_profile)
                
        return render(
                request,
                "review_detail.html",
                {
                    "teacherprofile": TeacherProfile,
                    "reviews": reviews,
                    "bookings": bookings,
                },
            )

@login_required
def create_booking(request, teacher_id):
    teacher = get_object_or_404(TeacherProfile, pk=teacher_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_acceptance', pk=teacher_id)
    else:
        form = BookingForm()
    
    context = {
        'booking_form': form,
        'teacher_id': teacher_id,
        'teacher': teacher,
    }
    return render(request, 'create_booking.html', context)

@login_required
def booking_acceptance(request):
    return render(request, 'booking_acceptance.html')

class ReviewList(ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

class ReviewDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "review_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "review_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

class ReviewLike(View):
    
    def review(self, request, slug, *args, **kwargs):
        review = get_object_or_404(Review, slug=slug)
        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)

        return HttpResponseRedirect(reverse('review_detail', args=[slug]))