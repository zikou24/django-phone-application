from django.shortcuts import redirect, render

from .models import Product, Category, Review
from .forms import ReviewForm
# Create your views here.


def home(request):

    product = Product.objects.all()

    context = {"product": product}

    return render(request, 'phones/index.html', context)


def store(request):

    products = Product.objects.all()

    category = Category.objects.all()

    counter = products.count()

    context = {"products": products, 'category': category, "counter": counter}

    return render(request, 'phones/store.html', context)


def pricerange(request):

    if request.method == "POST":

        price = request.POST['price']

        productss = Product.objects.filter(Price=price)

        category = Category.objects.all()

        counter = productss.count()

    else:

        return redirect("store-apge")

    context = {"products": productss, 'category': category, "counter": counter}

    return render(request, 'phones/storePrices.html', context)


def categoryProduct(request, pk):

    category = Category.objects.all()

    categoryproduct = Category.objects.get(id=pk)

    donc = Product.objects.filter(category=categoryproduct)
    counter = donc.count()

    context = {"donc": donc, 'category': category, "counter": counter}

    return render(request, 'phones/categoryproduct.html', context)


def Productdetail(request, pk):

    product_detail = Product.objects.get(id=pk)

    forms = ReviewForm()

    review = Review.objects.filter(prouduct_review=product_detail)

    context = {"productD": product_detail, "review": review, "form": forms}

    return render(request, 'phones/product_detail.html', context)


def submitReview(request, product_id):
    url = request.META.get('HTTP_REFERER')

    if request.method == "POST":

        try:
            reviewss = Review.objects.get(
                profiles=request.user, prouduct_review__id=product_id)
            forms = ReviewForm(request.POST, instance=reviewss)

            forms.save()

            return redirect(url)

        except:

            forms = ReviewForm(request.POST)

            if forms.is_valid():
                formss = forms.save(commit=False)
                formss.prouduct_review_id = product_id
                formss.profiles = request.user
                formss.save()
                return redirect(url)
