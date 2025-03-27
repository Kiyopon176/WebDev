from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
from api.models import Product, Category


def product_list1(request):
    # select * from auth_product;
    products1 = Product.objects.all()
    products_json = [p.to_json() for p in products1]
    return JsonResponse(products_json, safe=False)


def category_list1(request):
    # select * from auth_category;
    categories1 = Category.objects.all()
    categories_json = [c.to_json() for c in categories1]
    return JsonResponse(categories_json, safe=False)

@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
            
            # Extract product fields
            name = data.get('name')
            price = data.get('price')
            description = data.get('description')
            count = data.get('count')
            is_active = data.get('is_active', True)  # Default to True if not provided
            
            # Validate required fields
            if not all([name, price, description, count]):
                return JsonResponse({'error': 'Missing required fields'}, status=400)
            
            # Create and save the product
            product = Product(
                name=name,
                price=float(price),
                description=description,
                count=int(count),
                is_active=is_active
            )
            product.save()
            
            # Return the created product as JSON
            return JsonResponse(product.to_json(), status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


def home(request):
    return HttpResponse('home page')


def about(request):
    return HttpResponse("<h1 style='color: red;'>About page</h1>")


products2 = [
    {
        'id': _id,
        'name': f'Product {_id}',
        'price': _id * 1000,
        'description': 'This is product',
        'count': _id,
        'category': _id,
        'is_activate': True
    }
    for _id in range(1, 11)
]

categories2 = [
    {
        'id': _id,
        'name': f'Category {_id}'
    }
    for _id in range(1, 11)
]


def product_list2(request):
    return JsonResponse(products2, safe=False)


def product_detail2(request, product_id):
    for product in products2:
        if product['id'] == product_id:
            return JsonResponse(product)

    return JsonResponse({'error': 'Product not found'})


def category_list2(request):
    return JsonResponse(categories2, safe=False)


def category_detail2(request, category_id):
    for category in categories2:
        if category['id'] == category_id:
            return JsonResponse(category)

    return JsonResponse({'error': 'Category not found'})


def category_products(request, category_id):
    for category in products2:
        if category['category'] == category_id:
            return JsonResponse(category)

    return JsonResponse({'error': 'Category id in Product not found'})
