from django.http import HttpResponse

# Create your views here.
def home_page(request):
	return HttpResponse('<html><title>Homepage Pribadi</title>Givana Sandita, 1206208076</html>')
