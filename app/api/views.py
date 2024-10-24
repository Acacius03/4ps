from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializer import StudentListSerializer, StudentSerializer

# FR = FaceRecognition()
# Create your views here.
@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    serializer = StudentListSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def enroll(request):
    student = StudentSerializer(data=request.data)
    if not student.is_valid(): 
        return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)
    student = student.save()
    return Response(student.data, status=status.HTTP_201_CREATED)

def find_user(pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return None
    return student

@api_view(['GET'])
def get_user(request, pk):
    student = find_user(pk)
    if not student:
        return Response(status=status.HTTP_400_NOT_FOUND)
    student = StudentSerializer(student)
    return Response(student.data)

@api_view(['PUT'])
def update_user(request, pk):
    student = find_user(pk)
    if not student:
        return Response(status=status.HTTP_400_NOT_FOUND)
    student = StudentSerializer(student)
    if not student.is_valid(): 
        return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)
    student.save()
    return Response(student.data)

@api_view(['DELETE'])
def delete_user(request, pk):
    student = find_user(pk)
    if not student:
        return Response(status=status.HTTP_400_NOT_FOUND)
    student = StudentSerializer(student)
    if not student.is_valid(): 
        return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)
    student.save()
    return Response(student.data)

@api_view(['POST'])
def login(request):
    return Response({'msg': 'Not yet finished'}, status=status.HTTP_200_OK)

    # if 'fingerprint' not in request.FILES:
    #     return Response({'error': 'Fingerprint file is required.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # # fingerprint = request.FILES['fingerprint']

    # # Implement your fingerprint matching logic here
    # # If match found:
    # # return Response('success', status=status.HTTP_200_OK)

    # return Response({'error': 'Fingerprint not recognized.'}, status=status.HTTP_400_BAD_REQUEST)