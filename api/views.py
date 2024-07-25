from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

@api_view(["GET"])
def getRoutes(request):
    routes = [
    {
        "id": 1,
        "username": "user1",
        "profile_picture": "https://example.com/profiles/user1.jpg",
        "post_id": "post_101",
        "post_image": "https://example.com/posts/post_101.jpg",
        "caption": "Beautiful sunset at the beach!",
        "timestamp": "2024-07-24T18:25:43.511Z",
        "likes": 150,
        "comments": [
            {
                "username": "user2",
                "comment": "Amazing view!",
                "timestamp": "2024-07-24T18:30:00.000Z"
            },
            {
                "username": "user3",
                "comment": "Wish I was there!",
                "timestamp": "2024-07-24T18:32:45.123Z"
            }
        ]
    },
    {
        "id": 2,
        "username": "user2",
        "profile_picture": "https://example.com/profiles/user2.jpg",
        "post_id": "post_102",
        "post_image": "https://example.com/posts/post_102.jpg",
        "caption": "Exploring the city!",
        "timestamp": "2024-07-24T12:15:23.765Z",
        "likes": 230,
        "comments": [
            {
                "username": "user1",
                "comment": "Looks fun!",
                "timestamp": "2024-07-24T12:20:00.000Z"
            },
            {
                "username": "user4",
                "comment": "Great photo!",
                "timestamp": "2024-07-24T12:25:45.987Z"
            }
        ]
    },
    {
        "id": 3,
        "username": "user3",
        "profile_picture": "https://example.com/profiles/user3.jpg",
        "post_id": "post_103",
        "post_image": "https://example.com/posts/post_103.jpg",
        "caption": "Delicious homemade meal!",
        "timestamp": "2024-07-23T20:45:12.654Z",
        "likes": 320,
        "comments": [
            {
                "username": "user5",
                "comment": "Yummy!",
                "timestamp": "2024-07-23T20:50:00.000Z"
            },
            {
                "username": "user2",
                "comment": "Recipe, please!",
                "timestamp": "2024-07-23T20:55:30.789Z"
            }
        ]
    },
    {
        "id": 4,
        "username": "user4",
        "profile_picture": "https://example.com/profiles/user4.jpg",
        "post_id": "post_104",
        "post_image": "https://example.com/posts/post_104.jpg",
        "caption": "Hiking adventure!",
        "timestamp": "2024-07-22T10:05:55.234Z",
        "likes": 180,
        "comments": [
            {
                "username": "user3",
                "comment": "So scenic!",
                "timestamp": "2024-07-22T10:10:00.000Z"
            },
            {
                "username": "user1",
                "comment": "Where is this?",
                "timestamp": "2024-07-22T10:15:40.456Z"
            }
        ]
    },
    {
        "id": 5,
        "username": "user5",
        "profile_picture": "https://example.com/profiles/user5.jpg",
        "post_id": "post_105",
        "post_image": "https://example.com/posts/post_105.jpg",
        "caption": "New art piece!",
        "timestamp": "2024-07-21T16:35:48.123Z",
        "likes": 290,
        "comments": [
            {
                "username": "user4",
                "comment": "Stunning work!",
                "timestamp": "2024-07-21T16:40:00.000Z"
            },
            {
                "username": "user2",
                "comment": "Incredible talent!",
                "timestamp": "2024-07-21T16:45:35.678Z"
            }
        ]
    }
]

    return Response(routes)


@api_view(['GET'])
def getnotes(request):
    notes = Note.objects.all()
    serializer  = NoteSerializer(notes, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getnote(request,pk):
    note = Note.objects.get(id=pk)
    serializer  = NoteSerializer(note, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note,many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request,pk):
    note = Note.objects.get(id = pk)
    
    serializer = NoteSerializer(note,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request,pk):
    note = Note.objects.get(id = pk)
    note.delete()
    return Response("note was deleted")