from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
	total = Item.objects.count()
	if total > 4:
		comment = 'oh tidak'
	elif total == 0:
		comment = 'yey, waktunya berlibur'
	else:
		comment = 'sibuk tapi santai'

	return render(request, 'home.html', {'comment':comment})

def view_list(request, list_id):
	list_ = List.objects.get(id = list_id)
	items = Item.objects.filter(list=list_)
	total = items.count()
	if total > 4:
		comment = 'oh tidak'
	elif total == 0:
		comment = 'yey, waktunya berlibur'
	else:
		comment = 'sibuk tapi santai'
	return render(request, 'list.html', {'list' : list_, 'comment':comment})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))
	
def add_item(request, list_id):
	list_ = List.objects.get(id = list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))
	
