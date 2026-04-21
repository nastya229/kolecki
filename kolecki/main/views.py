from django.shortcuts import render, get_object_or_404
from .models import Jewelry, CatalogOrder, BuilderModel, BuilderOrder
#from bots.telegram_bot import send_telegram


def home(request):
    return render(request, "main/home.html")


def about(request):
    return render(request, "main/about.html")


def catalog(request):
    items = Jewelry.objects.all()
    return render(request, "main/catalog.html", {"items": items})


def create_catalog_order(request, id):
    jewelry = get_object_or_404(Jewelry, id=id)

    if request.method == "POST":
        customer_name = request.POST.get("customer_name", "").strip()
        phone = request.POST.get("phone", "").strip()

        if customer_name and phone:
            order = CatalogOrder.objects.create(
                jewelry=jewelry,
                customer_name=customer_name,
                phone=phone,
            )

            text = (
                f"<b>Новый заказ из каталога</b>\n\n"
                f"<b>Украшение:</b> {jewelry.name}\n"
                f"<b>Цена:</b> {jewelry.price} ₽\n"
                f"<b>Имя:</b> {customer_name}\n"
                f"<b>Телефон:</b> {phone}\n"
                f"<b>ID заказа:</b> {order.id}"
            )
            #send_telegram(text)

            return render(
                request,
                "main/checkout_success.html",
                {
                    "jewelry": jewelry,
                    "order": order,
                    "customer_name": customer_name,
                },
            )

    return render(request, "main/catalog_order_form.html", {"jewelry": jewelry})


def models_3d(request):
    builder_models = BuilderModel.objects.all().order_by("product_type", "title")

    if request.method == "POST":
        product_type = request.POST.get("product_type", "")
        model_id = request.POST.get("model_id", "")
        material = request.POST.get("material", "")
        stone = request.POST.get("stone", "")
        engraving = request.POST.get("engraving", "")
        customer_name = request.POST.get("customer_name", "").strip()
        phone = request.POST.get("phone", "").strip()

        selected_model = BuilderModel.objects.filter(id=model_id).first() if model_id else None

        if product_type != "ring":
            engraving = ""

        if customer_name and phone:
            order = BuilderOrder.objects.create(
                product_type=product_type,
                model=selected_model,
                material=material,
                stone=stone,
                engraving=engraving,
                customer_name=customer_name,
                phone=phone,
            )

            product_names = {
                "ring": "Кольцо",
                "bracelet": "Браслет",
                "earrings": "Серьги",
            }

            material_names = {
                "silver": "Серебро",
                "melchior": "Мельхиор",
            }

            stone_names = {
                "diamond": "Бриллиант",
                "emerald": "Изумруд",
                "ruby": "Рубин",
                "sapphire": "Сапфир",
            }

            text = (
                f"<b>Новый заказ из 3D конструктора</b>\n\n"
                f"<b>Тип:</b> {product_names.get(product_type, product_type or '-')}\n"
                f"<b>Модель:</b> {selected_model.title if selected_model else 'Не выбрана'}\n"
                f"<b>Материал:</b> {material_names.get(material, material or '-')}\n"
                f"<b>Камень:</b> {stone_names.get(stone, stone or '-')}\n"
                f"<b>Гравировка:</b> {engraving or '-'}\n"
                f"<b>Имя:</b> {customer_name}\n"
                f"<b>Телефон:</b> {phone}\n"
                f"<b>ID заказа:</b> {order.id}"
            )
            #send_telegram(text)

            return render(
                request,
                "main/builder_success.html",
                {
                    "order": order,
                    "selected_model": selected_model,
                    "customer_name": customer_name,
                },
            )

    return render(
        request,
        "main/models_3d.html",
        {"builder_models": builder_models},
    )