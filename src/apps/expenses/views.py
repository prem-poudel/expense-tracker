from rest_framework.response import Response
from rest_framework import generics, status, permissions
from .models import Expense
from .serializers import ExpenseSerializer
from .permissions import IsExpenseOwnerOrAdmin


class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self) :
        """
        Return the list of expenses for the authenticated user.
        """
        user = self.request.user
        return Expense.objects.all() if user.is_superuser else Expense.objects.filter(user=user)
    
    def perform_create(self, serializer):
        """
        Save the expense with the authenticated user as the owner.
        """
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        return Response({
            "message": "Expense created successfully.",
            "data": ExpenseSerializer(data=request.data).data
        }, status=status.HTTP_201_CREATED)
    

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated, IsExpenseOwnerOrAdmin]

    def get_queryset(self):
        """
        Return the list of expenses for the authenticated user.
        """
        user = self.request.user
        return Expense.objects.all() if user.is_superuser else Expense.objects.filter(user=user)

    def update(self, request, *args, **kwargs):
        return Response({
            "message": "Expense updated successfully.",
            "data": ExpenseSerializer(data=request.data).data
        }, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        return Response({
            "message": "Expense deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)

