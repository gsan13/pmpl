from django.shortcuts import redirect, render
from lists.models import Item


def home_page(request):
	total = Item.objects.count()
	if total > 4:
		comment = 'oh tidak'
	elif total == 0:
		comment = 'yey, waktunya berlibur'
	else:
		comment = 'sibuk tapi santai'

	return render(request, 'home.html', {'comment':comment})

def view_list(request):
	items = Item.objects.all()
	total = Item.objects.count()
	if total > 4:
		comment = 'oh tidak'
	elif total == 0:
		comment = 'yey, waktunya berlibur'
	else:
		comment = 'sibuk tapi santai'
	return render(request, 'list.html', {'items' : items, 'comment':comment})

def new_list(request):
	Item.objects.create(text=request.POST['item_text'])
	return redirect('/lists/the-only-list-in-the-world/')
	
	
