from rest_framework.permissions import BasePermission

class IsOwnerOrSessionOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.user == request.user
        session_key = request.session.session_key
        return obj.session_key == session_key

class IsOwnerOfRelatedTodo(BasePermission):
    """
    Allows access only if the request user/session owns the related Todo.
    """
    def has_object_permission(self, request, view, obj):
        todo = obj.todo
        if request.user.is_authenticated:
            return todo.user == request.user
        session_key = request.session.session_key
        return todo.session_key == session_key