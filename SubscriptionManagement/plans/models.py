from django.db import models
import uuid


class Plan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    billing_cycle = models.CharField(
        max_length=50, choices=[("monthly", "Mensal"), ("annual", "Anual")]
    )

    def __str__(self):
        return self.name


class Subscription(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pendente"),
        ("active", "Ativa"),
        ("suspended", "Suspensa"),
        ("canceled", "Cancelada"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plan = models.ForeignKey(
        Plan, on_delete=models.CASCADE, related_name="subscriptions"
    )
    customer_email = models.EmailField()
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="pending")
    next_billing_date = models.DateField()

    def __str__(self):
        return f"{self.customer_email} - {self.plan.name}"


class Event(models.Model):
    EVENT_TYPES = [
        ("subscription_created", "Assinatura Criada"),
        ("payment_success", "Pagamento Bem-sucedido"),
        ("payment_failed", "Pagamento Falhou"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=50, choices=EVENT_TYPES)
    data = models.JSONField()
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.type} - {self.processed}"
