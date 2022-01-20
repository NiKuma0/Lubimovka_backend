import pytest
from django.urls import reverse

from apps.articles.tests.factories.blog_factory import BlogFactory
from apps.articles.tests.factories.news_factory import NewsFactory
from apps.content_pages.tests.factories import ImageForContentFactory, ImagesBlockFactory
from apps.core.tests.factories import PersonFactory
from apps.info.tests.factories import FestivalFactory, PlaceFactory
from apps.library.tests.factories import PlayFactory
from apps.main.tests.factories import BannerFactory

MAIN_URL = reverse("main:main_page")


@pytest.fixture
def images_for_content():
    PersonFactory.create_batch(3)
    return ImageForContentFactory.create_batch(2)


@pytest.fixture
def image(images_for_content):
    return ImagesBlockFactory(add_image=True)


@pytest.fixture
def festival():
    return FestivalFactory(start_date="2021-07-14", end_date="2021-07-15", year="2021")


@pytest.fixture
def plays(festival):
    return list(PlayFactory(year=festival.year) for _ in range(4))


@pytest.fixture
def play(festival):
    return PlayFactory(is_draft=False)


@pytest.fixture
def banners():
    return list(BannerFactory.create_batch(3))


@pytest.fixture
def news(plays, image):
    return list(
        NewsFactory.create_batch(
            3,
            add_several_preamble=1,
            add_several_text=1,
            add_several_title=1,
            add_several_quote=1,
            add_several_playsblock=1,
            add_several_imagesblock=1,
            add_several_personsblock=1,
            is_draft=False,
        )
    )


@pytest.fixture
def blog():
    return list(BlogFactory.complex_create(1))


@pytest.fixture
def places():
    return list(PlaceFactory.create_batch(3))
