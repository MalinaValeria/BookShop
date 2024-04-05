import factory

from shop.models import Category, Author, Publisher, Book, Series

factory.Faker._DEFAULT_LOCALE = 'ru_RU'


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'shop.Author'

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class PublisherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'shop.Publisher'

    name = factory.Faker('company')


class SeriesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'shop.Series'

    name = factory.Faker('sentence', nb_words=2)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'shop.Category'

    name = factory.Faker('sentence', nb_words=2)


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'shop.Book'

    name = factory.Faker('sentence', nb_words=2)
    category = factory.Faker('random_element', elements=Category.objects.all())
    author = factory.Faker('random_element', elements=Author.objects.all())


class BookInfoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'shop.BookInfo'

    book = factory.Faker('random_element', elements=Book.objects.all())
    price = factory.Faker('pyint', min_value=1, max_value=10000)
    publisher = factory.Faker('random_element', elements=Publisher.objects.all())
    publication_year = factory.Faker('pyint', min_value=1900, max_value=2024)
    series = factory.Faker('random_element', elements=Series.objects.all())
    isbn = factory.Faker('isbn13')
    page_count = factory.Faker('pyint', min_value=1, max_value=1000)
    type_of_cover = factory.Faker('random_element', elements=('hard', 'soft', 'dutch'))
    circulation = factory.Faker('pyint', min_value=1, max_value=10000)
    age_limit = factory.Faker('random_element', elements=(0, 6, 12, 16, 18))
    description = factory.Faker('sentence', nb_words=10)


class BookAuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'shop.BookAuthor'

    book = factory.Faker('random_element', elements=Book.objects.all())
    author = factory.Faker('random_element', elements=Author.objects.all())
