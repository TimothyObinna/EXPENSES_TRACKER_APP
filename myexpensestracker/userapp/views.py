from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import UpdateView
from expenses.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


# class BaseProfileView(View):
#    def get_profile_info(self, user):
#       try:
#         myuser = Profile.objects.get(user=user)
#         # myuser = get_object_or_404(Profile, user=user)
#         profile_info = {
#           'profile_image_url': myuser.profile_image.url if myuser.profile_image else None,
#           'username': myuser.user.username,
#           'fullname': myuser.fullname,
#           'email': myuser.user.email,
#           'address': myuser.address,
#           'dob': myuser.dob,
#           'user': myuser,
#         }
#         return {'profile_info': profile_info}
#       except Profile.DoesNotExist:
#         return {}



# users = User.objects.all()

class BaseProfileView(View):
    def get_profile_info(self, user):
        try:
            profile = get_object_or_404(Userprofile, user=user)  # Access the related Profile using the lowercased name
        
            profile_info = {
                'profile_image_url': profile.profile_image if profile.profile_image else None,
                'username': profile.fullname,
                'fullname': profile.fullname,
                'email': profile.user.email,
                'address': profile.address,
                'dob': profile.dob,
                'user': profile.user,
            }

            return {'profile_info': profile_info}

        except Userprofile.DoesNotExist:
            return {}





class ProfilePage(LoginRequiredMixin, BaseProfileView):
    login_url = 'login'
    def get(self, request):
        context = self.get_profile_info(request.user)
        if not context:
            return redirect('dashboard')
        return render(request, 'usertemp/profile.html', context=context)
    
    def post(self, request):
        # Process the submitted form data
        return render(request, 'usertemp/profile.html')
    
    

class UserProfileUpdateView(LoginRequiredMixin, View):
    template_name = 'usertemp/profile_update.html'

    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Userprofile, user=request.user)
        context = {'profile': profile}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        profile = get_object_or_404(Userprofile, user=request.user)

        # Update profile fields based on POST data
        profile.fullname = request.POST.get('fullname')
        profile.address = request.POST.get('address')
        profile.dob = request.POST.get('dob')

        # Handle profile image
        profile_image = request.FILES.get('profile_image')
        if profile_image:
            profile.profile_image = profile_image

        profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profilepage')


# class UserProfileView(View):
#     @login_required
#     def get(self, request):
#         context = self.get_profile_info(request.user)
#         return render(request, 'profilepage.html', context)

#     def get_profile_info(self, user):
#         try:
#             user_profile = Userprofile.objects.get(user=user)
#             profile_info = {
#                 'profile_image_url': user_profile.profile_image.url if user_profile.profile_image else None,
#                 'username': user.username,
#                 'fullname': user_profile.fullname,
#                 'email': user.email,
#                 'address': user_profile.address,
#                 'dob': user_profile.dob,
#             }
#             return {'profile_info': profile_info}
#         except Userprofile.DoesNotExist:
#             return {}




# class ProfilePage(View):
#     def get(self, request):
#         return render(request, 'usertemp/profile.html')
    
#     def post(self, request):
#         return render(request, 'usertemp/profile.html')

# class ProfileUpdateView(View):
#     template_name = 'usertemp/profile_update.html'

#     def get(self, request):
#         context = self.get_profile_info(request.user)
#         if not context:
#             return redirect('dashboard')
        
#         return render(request, self.template_name, context=context)

#     def post(self, request):
#         try:
#             profile = Userprofile.objects.get(user=request.user)
#         except Userprofile.DoesNotExist:
#             return redirect('dashboard')

#         profile.fullname = request.POST.get('fullname')
#         profile.address = request.POST.get('address')
#         profile.dob = request.POST.get('dob')

#         # Save the updated profile
#         profile.save()

#         messages.success(request, 'Profile updated successfully!')
#         return redirect('profile')
    
    







# class Categories(DetailView):
#   def get(self, request, category_slug):
#     income_cat =  Income.objects.get(slug=category_slug)
#     context = {
#       'cat_item': income_cat,
      
#     }
#     return render(request, 'category.html', context=context)
  
#   def post(self, request):
#     return render(request, 'category.html')