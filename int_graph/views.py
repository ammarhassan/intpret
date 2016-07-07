from django.shortcuts import render
from django.http import JsonResponse
from .models import QueriesStore
from django.db.models import Max

# Create your views here.


def shell(request, group_id=None):
	
				
	queries = []
	query = None
	if request.method=='POST':
		# print('i am in post')
		if not group_id:
			group_id = QueriesStore.objects.all(
						).aggregate(group_max=Max('group'))['group_max']
			print('there was not id, but we found it', group_id)
			if group_id is not None:
				group_id+=1
			else:
				group_id=0

		query_string = request.POST.get('light-shell')
		# print('query string is'+query_string)
		# print('group_id is '+ str(group_id))
		if query_string:
			query = QueriesStore(query=query_string, group=group_id)
			query.save()

	else:
		pass
	
	if group_id is not None:
		queries = QueriesStore.objects.filter(group=group_id)


	return render(request, 'shell.html', {'queries':queries, 'group_id':group_id})

def ajax_shell(request):

	return JsonResponse({'data':[
        ['Task', 'Hours per Day'],
        ['Work',     11],
        ['Eat',      2],
        ['Commute',  2],
        ['Watch TV', 2],
        ['Sleep',    7]
    ]})


