from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from .models import Products
from .serializers import MyProductsSerializer
from .custom_token_authentication import CustomAPIKeyAuthentication



@api_view(['GET'])
def HomeAPI(request):
    
    data = {
                'status_code': 200,  # Example status code
                'message': 'Access APIs Page ',  # Example message
                'pages':{
                    'all products':'get/',
                    'single product':'getone/id'
                }
            }
    return Response(data)

@api_view(['GET'])
def GetAPI(request):
    products = Products.objects.all()
    serializer = MyProductsSerializer(products, many=True)
    
    data = {
                'status_code': 200,  # Example status code
                'message': 'Success',  # Example message
                'data': serializer.data
            }
    return Response(data)


@api_view(['GET'])
def GetOneAPI(request,id):
    product = Products.objects.filter(id=id)
    serializer = MyProductsSerializer(product, many=True)
    return Response(serializer.data)

# PostAPI

@api_view(['POST'])
@authentication_classes([CustomAPIKeyAuthentication])
def PostAPI(request):
    # API logic goes here
    return Response({'message': 'Data Post with Authenicated by API KEY'})