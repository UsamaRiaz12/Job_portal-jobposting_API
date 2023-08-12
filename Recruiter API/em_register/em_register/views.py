from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import em_register
from .serializer import em_registerSerilaizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from django.shortcuts import render, redirect

# def em_register_view(request):
#         objects = em_register.objects.all() 


@api_view(['GET', 'POST'])
def em_register_list(request,format=None):
    if request.method == 'GET':
        em_registers = em_register.objects.all()
        serializer = em_registerSerilaizer(em_registers, many=True)
        return JsonResponse({'em_register': serializer.data})

    elif request.method == 'POST':
        serializer = em_registerSerilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def em_register_detail(request, id,format=None):
    try:
        em_reg = em_register.objects.get(pk=id)
    except em_register.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
         
    if request.method == 'GET':
        serializer = em_registerSerilaizer(em_reg)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = em_registerSerilaizer(em_reg, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        em_reg.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


def em_register_view(request):
    if request.method == 'POST':
        form = em_registerSerilaizer(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = em_registerSerilaizer()
    return render(request, 'em_register.py', {'form': form})

def date_api(request):
    if request.method == 'GET':
        date_str = request.GET.get('date', '')  # Get the date from the query parameter
        
        try:
            # Parse the input date using the specified format
            input_date = datetime.strptime(date_str, '%d/%m/%Y')
            formatted_date = input_date.strftime('%Y-%m-%d')  # Format the date as YYYY-MM-DD
            
            response_data = {
                'formatted_date': formatted_date
            }
            
            return JsonResponse(response_data)
        except ValueError:
            error_message = 'Invalid date format. Please use DD/MM/YYYY.'
            return JsonResponse({'error': error_message}, status=400)

