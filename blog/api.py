# blog/api.py
import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Post, Comment

def post_to_dict(post):
    return {
        "id":       post.id,
        "title":    post.title,
        "slug":     post.slug,
        "body":     post.body,
        "pub_date": post.pub_date.isoformat(),
        "category": post.category.name if post.category else None,
    }

@method_decorator(csrf_exempt, name="dispatch")
class PostListView(View):

    def get(self, request):
        posts = Post.objects.all()

        query = request.GET.get("search", "")
        if query:
            posts = posts.filter(title__icontains=query)

        return JsonResponse({"posts": [post_to_dict(p) for p in posts]})

    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Authentication required."}, status=401)

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)

        required_fields = ["title", "slug", "body"]
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return JsonResponse(
                {"error": f'Missing required field(s): {", ".join(missing_fields)}.'},
                status=400,
            )

        post = Post.objects.create(
            title=data["title"],
            slug=data["slug"],
            body=data["body"],
        )
        return JsonResponse(post_to_dict(post), status=201)

@method_decorator(csrf_exempt, name="dispatch")
class PostDetailView(View):

    def get_post(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None

    def get(self, request, pk):
        post = self.get_post(pk)
        if post is None:
            return JsonResponse({"error": "Not found."}, status=404)
        return JsonResponse(post_to_dict(post))

    def patch(self, request, pk):
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Authentication required."}, status=401)

        post = self.get_post(pk)
        if post is None:
            return JsonResponse({"error": "Not found."}, status=404)

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)

        allowed_fields = ["title", "body", "slug"]
        updated = False

        for field in allowed_fields:
            if field in data:
                setattr(post, field, data[field])
                updated = True

        if updated:
            post.save()

        return JsonResponse(post_to_dict(post))

    def delete(self, request, pk):
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Authentication required."}, status=401)

        post = self.get_post(pk)
        if post is None:
            return JsonResponse({"error": "Not found."}, status=404)

        post.delete()
        return JsonResponse({}, status=204)

@method_decorator(csrf_exempt, name="dispatch")
class PostCommentView(View):
    """GET/POST comments for a given post."""

    def get(self, request, pk):
        post = Post.objects.filter(pk=pk).first()
        if post is None:
            return JsonResponse({"error": "Not found."}, status=404)

        comments = post.comments.filter(active=True)
        data = [
            {
                "id": c.id,
                "author": c.author,
                "body": c.body,
                "created": c.created.isoformat(),
            }
            for c in comments
        ]
        return JsonResponse({"comments": data})

    def post(self, request, pk):
        post = Post.objects.filter(pk=pk).first()
        if post is None:
            return JsonResponse({"error": "Not found."}, status=404)

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)

        required_fields = ["author", "body"]
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return JsonResponse(
                {"error": f'Missing required field(s): {", ".join(missing_fields)}.'},
                status=400,
            )

        comment = Comment.objects.create(
            post=post,
            author=data["author"],
            body=data["body"],
            active=True,
        )

        return JsonResponse(
            {
                "id": comment.id,
                "author": comment.author,
                "body": comment.body,
                "created": comment.created.isoformat(),
            },
            status=201,
        )