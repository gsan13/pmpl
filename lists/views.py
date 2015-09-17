from django.shortcuts import redirect, render
from lists.models import Item


def home_page(request):
	if request.method =='POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/')

	items = Item.objects.all()
	total = Item.objects.count()
	if total > 4:
		comment = 'oh tidak'
	elif total == 0:
		comment = 'yey, waktunya berlibur'
	else:
		comment = 'sibuk tapi santai'

	return render(request, 'home.html', {'items': items, 'comment':comment})

