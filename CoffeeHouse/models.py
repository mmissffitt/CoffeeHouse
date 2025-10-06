from django.db import models

class Clients(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    phone_number = models.CharField("Номер телефона", max_length=20)
    email = models.EmailField("Почта", max_length=255)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["last_name", "first_name"]
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Positions(models.Model):
    position_name = models.CharField("Название должности", max_length=100)
    rate_per_hour = models.DecimalField("Ставка в час", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
    
    def __str__(self):
        return self.position_name

class Employees(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    phone_number = models.CharField("Номер телефона", max_length=20)
    email = models.EmailField("Почта", max_length=255)
    date_of_hiring = models.DateTimeField("Дата приема на работу")
    position = models.ForeignKey(
        Positions,
        on_delete=models.CASCADE,
        verbose_name="Должность"
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ["last_name", "first_name"]
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class CategoriesOfProducts(models.Model):
    category_name = models.CharField("Название категории", max_length=100)

    class Meta:
        verbose_name = "Категория товаров"
        verbose_name_plural = "Категории товаров"
    
    def __str__(self):
        return self.category_name

class Products(models.Model):
    name = models.CharField("Название", max_length=100)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        CategoriesOfProducts,
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
    
    def __str__(self):
        return self.name

class Orders(models.Model):
    client = models.ForeignKey(
        Clients,
        on_delete=models.CASCADE,
        verbose_name="Клиент"
    )
    employee = models.ForeignKey(
        Employees,
        on_delete=models.CASCADE,
        verbose_name="Сотрудник"
    )
    order_time = models.DateTimeField("Время заказа")
    payment_time = models.DateTimeField("Время оплаты", null=True, blank=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
    
    def __str__(self):
        return f"Заказ {self.id} - {self.client}"

class OrderDetails(models.Model):
    order = models.ForeignKey(
        Orders,
        on_delete=models.CASCADE,
        verbose_name="Заказ"
    )
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        verbose_name="Товар"
    )
    quantity = models.IntegerField("Количество")
    price_at_the_time_of_purchase = models.DecimalField(
        "Цена на момент покупки",
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        verbose_name = "Деталь заказа"
        verbose_name_plural = "Детали заказов"
    
    def __str__(self):
        return f"{self.order} - {self.product}"