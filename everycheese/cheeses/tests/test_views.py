import pytest
from pytest_django.asserts import assertContains

from django.urls import reverse

from .factories import CheeseFactory
from ..views import CheeseListView, CheeseDetailView

pytestmark = pytest.mark.django_db


def test_good_cheese_list_view_expanded(rf):
    url = reverse("cheeses:list")
    request = rf.get(url)
    callable_obj = CheeseListView.as_view()
    response = callable_obj(request)
    assertContains(response, "")


def test_good_cheese_list_view(rf):
    request = rf.get(reverse("cheeses:list"))
    response = CheeseListView.as_view()(request)
    assertContains(response, "Cheese List")


def test_good_cheese_detail_view(rf):
    cheese = CheeseFactory()
    url = reverse("cheeses:detail", kwargs={"slug": cheese.slug})
    request = rf.get(url)

    callable_obj = CheeseDetailView.as_view()
    response = callable_obj(request, slug=cheese.slug)
    assertContains(response, cheese.name)
