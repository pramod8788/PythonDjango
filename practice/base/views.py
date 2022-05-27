from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render
from . import forms
from . import models
import json

# Create your views here.

# Both are for listing and creating infos model and also for searching
class HomeView(ListView):
    template_name = "base/index.html"
    model = models.info
    context_object_name = "info_items"

    def get_context_data(self, **kwargs):
        print("I am view for testing custom middleware.")

        form = forms.InfoForm()
        context = super().get_context_data(**kwargs)
        context["form"] = form
        context["infos"] = json.dumps(list(models.info.objects.values()))
        return context


class CreateInfoView(CreateView):
    model = models.info
    fields = "__all__"
    success_url = '/'

# # This function is used for creating info model using ajax 
# def create_info(request):
#     if request.method == "POST":
#         form = forms.InfoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({"status": "True"})
#         else:
#             return JsonResponse({"status": "False"})


# View for Dropzone.JS 
def fileupload(request):
    if request.method == "POST":
        my_file = request.FILES.get("file")
        models.file.objects.create(uploads=my_file)
        return HttpResponse('upload')
    else:
        return JsonResponse({"Post": "False"})


# Both Views are for star rating
def image_page(request):
    images = models.file.objects.filter(rating=0).order_by("?").first()
    all_images = models.file.objects.all()
    context = {
        "images": images,
        "all_images": all_images,
    }
    return render(request, "base/image-page.html", context)

def image_rate(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        rate_val = request.POST.get('rate')
        obj = models.file.objects.get(id=el_id)
        obj.rating = rate_val
        obj.save()
        return JsonResponse({'success':'True', 'score': rate_val})
    return JsonResponse({'success': 'False'})

def image_like(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        value = request.POST.get('value')
        image_obj = models.file.objects.get(id=post_id)
        
        if value == 'Like':
            image_obj.like = 'Like'
        else:
            image_obj.like = 'Unlike'
        image_obj.save()
        return JsonResponse({"success": "True"})
    return JsonResponse({"success": "False"})

def rating_remove(request, id):
    image_obj = models.file.objects.get(id=id)
    image_obj.rating = 0
    image_obj.save()
    return redirect('image-info')