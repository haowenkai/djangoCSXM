from django.shortcuts import render, get_object_or_404, redirect
from .models import Community, House, Owner
from .forms import CommunityForm, HouseForm, OwnerForm

def index(request):
    return render(request, 'app/index.html')

def house_management(request):
    houses = House.objects.all()
    return render(request, 'app/house_management.html', {'houses': houses})

def community_list(request):
    communities = Community.objects.all()
    return render(request, 'app/community_list.html', {'communities': communities})

def house_list(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    houses = House.objects.filter(community=community)
    return render(request, 'app/house_list.html', {'community': community, 'houses': houses})

def house_edit(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    if request.method == 'POST':
        form = HouseForm(request.POST, instance=house)
        if form.is_valid():
            form.save()
            return redirect('house_list', community_id=house.community.id)
    else:
        form = HouseForm(instance=house)
    return render(request, 'app/house_form.html', {'form': form})

def owner_list(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    owners = Owner.objects.filter(house=house)
    return render(request, 'app/owner_list.html', {'house': house, 'owners': owners})

def owner_edit(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_list', house_id=owner.house.id)
    else:
        form = OwnerForm(instance=owner)
    return render(request, 'app/owner_form.html', {'form': form})
