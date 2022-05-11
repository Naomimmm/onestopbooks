from django.test import TestCase
from django.core.exceptions import ValidationError
from bookstore.models import *

# Create your tests here.
# Django test example: https://docs.djangoproject.com/en/4.0/topics/testing/overview/
class BookTestCase(TestCase):
    def test_valid_book(self):
        Book.objects.create(
            isbn = "195153448",
            title = "Classical Mythology",
            authors = "Mark P. O. Morford",
            year_public = "2002",
            publisher = "Oxford University Press",
            thumbnail_pic = "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
            quantity = 10,
            price = 10)
        
        valid_book = Book.objects.get(isbn="195153448")
        self.assertIsNotNone(valid_book)

    def test_invalid_book_isbn_too_long(self):
        Book.objects.create(
            isbn = "0000000000000000000000000000000",
            title = "Classical Mythology",
            authors = "Mark P. O. Morford",
            year_public = "2002",
            publisher = "Oxford University Press",
            thumbnail_pic = "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
            quantity = 10,
            price = 10)
        
        # max_length is not enforced.
        # verifying using full_clean and save, reference: https://stackoverflow.com/questions/8478054/django-model-charfield-max-length-does-not-work
        try:
            invalid_book = Book.objects.get(isbn="0000000000000000000000000000000")
            invalid_book.full_clean()
            invalid_book.save()
        except ValidationError:
            pass

    def test_invalid_book_title_too_long(self):
        Book.objects.create(
            isbn = "195153448",
            title = "This title is too long. This title is too long. This title is too long. This title is too long. This title is too long. This title is too long. This title is too long. This title is too long. This title is too long. This title is too long.",
            authors = "Mark P. O. Morford",
            year_public = "2002",
            publisher = "Oxford University Press",
            thumbnail_pic = "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
            quantity = 10,
            price = 10)
        
        # max_length is not enforced.
        # verifying using full_clean and save, reference: https://stackoverflow.com/questions/8478054/django-model-charfield-max-length-does-not-work
        try:
            invalid_book = Book.objects.get(isbn="195153448")
            invalid_book.full_clean()
            invalid_book.save()
        except ValidationError:
            pass

    def test_invalid_book_authors_too_long(self):
        Book.objects.create(
            isbn = "195153448",
            title = "Classical Mythology",
            authors = "Authors is too long. Authors is too long. Authors is too long. Authors is too long. Authors is too long. Authors is too long. Authors is too long. Authors is too long. Authors is too long. Authors is too long. Authors is too long. Authors is too long.",
            year_public = "2002",
            publisher = "Oxford University Press",
            thumbnail_pic = "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
            quantity = 10,
            price = 10)
        
        valid_book = Book.objects.get(isbn="195153448")
        self.assertIsNotNone(valid_book)

    def test_invalid_book_invalid_year(self):
        with self.assertRaises(ValueError):
            Book.objects.create(
                isbn = "195153448",
                title = "Classical Mythology",
                authors = "Mark P. O. Morford",
                year_public = "NotRealYear",
                publisher = "Oxford University Press",
                thumbnail_pic = "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
                quantity = 10,
                price = 10)

    def test_invalid_book_publisher_too_long(self):
        Book.objects.create(
            isbn = "195153448",
            title = "Classical Mythology",
            authors = "Mark P. O. Morford",
            year_public = "2002",
            publisher = "Publisher too long. Publisher too long. Publisher too long. Publisher too long. Publisher too long. Publisher too long. Publisher too long. Publisher too long. Publisher too long. Publisher too long. Publisher too long. Publisher too long. Publisher too long.",
            thumbnail_pic = "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
            quantity = 10,
            price = 10)
        
        valid_book = Book.objects.get(isbn="195153448")
        self.assertIsNotNone(valid_book)

    def test_book_to_string(self):
        Book.objects.create(
            isbn = "195153448",
            title = "Classical Mythology",
            authors = "Mark P. O. Morford",
            year_public = "2002",
            publisher = "Oxford University Press",
            thumbnail_pic = "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
            quantity = 10,
            price = 10)
        
        valid_book = Book.objects.get(isbn="195153448")
        self.assertEqual(str(valid_book), "Classical Mythology")

    def test_book_decrease_quantity(self):
        Book.objects.create(
            isbn = "195153448",
            title = "Classical Mythology",
            authors = "Mark P. O. Morford",
            year_public = "2002",
            publisher = "Oxford University Press",
            thumbnail_pic = "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
            quantity = 10,
            price = 10)
        
        valid_book = Book.objects.get(isbn="195153448")
        self.assertEqual(10, valid_book.quantity)
        
        valid_book.decrease_quantity(3)
        self.assertEqual(7, valid_book.quantity)

class CustomerTestCase(TestCase):
    def test_valid_customer(self):
        Customer.objects.create(
            first_name = "Amy",
            last_name = "Test",
            email = "AmyTest@gmail.com",
            address_1 = "123 S. Denver",
            city = "Denver",
            state = "Colorado",
            zip_code = "80123")

        valid_customer = Customer.objects.get(first_name="Amy")
        self.assertIsNotNone(valid_customer)

    def test_invalid_customer_name_too_long(self):
        Customer.objects.create(
            first_name = "AmyAmyAmyAmyAmyAmyAmyAmyAmyAmyAmy",
            last_name = "Test",
            email = "AmyTest@gmail.com",
            address_1 = "123 S. Denver",
            city = "Denver",
            state = "Colorado",
            zip_code = "80123")

        try:
            invalid_customer = Customer.objects.get(first_name = "AmyAmyAmyAmyAmyAmyAmyAmyAmyAmyAmy")
            invalid_customer.full_clean()
            invalid_customer.save()
        except ValidationError:
            pass

    def test_invalid_customer_last_name_too_long(self):
        Customer.objects.create(
            first_name = "Amy",
            last_name = "Last name is too long. Last name is too long.Last name is too long. Last name is too long. Last name is too long. Last name is too long. Last name is too long. Last name is too long. Last name is too long. Last name is too long. Last name is too long. Last name is too long.",
            email = "AmyTest@gmail.com",
            address_1 = "123 S. Denver",
            city = "Denver",
            state = "Colorado",
            zip_code = "80123")

        try:
            invalid_customer = Customer.objects.get(first_name = "Amy")
            invalid_customer.full_clean()
            invalid_customer.save()
        except ValidationError:
            pass

    def test_invalid_customer_invalid_address_1(self):
        Customer.objects.create(
            first_name = "Amy",
            last_name = "Test",
            email = "AmyTest@gmail.com",
            address_1 = "Address is too long. Address is too long. Address is too long. Address is too long. Address is too long. Address is too long. Address is too long. Address is too long. Address is too long. Address is too long. Address is too long. Address is too long. Address is too long.",
            city = "Denver",
            state = "Colorado",
            zip_code = "80123")

        try:
            invalid_customer = Customer.objects.get(first_name = "Amy")
            invalid_customer.full_clean()
            invalid_customer.save()
        except ValidationError:
            pass

    def test_invalid_customer_invalid_city(self):
        Customer.objects.create(
            first_name = "Amy",
            last_name = "Test",
            email = "AmyTest@gmail.com",
            address_1 = "123 S. Denver",
            city = "City is too long. City is too long. City is too long. City is too long. City is too long. City is too long. City is too long. City is too long. City is too long. City is too long. City is too long. City is too long. City is too long. City is too long. City is too long. City is too long.",
            state = "Colorado",
            zip_code = "80123")

        try:
            invalid_customer = Customer.objects.get(first_name = "Amy")
            invalid_customer.full_clean()
            invalid_customer.save()
        except ValidationError:
            pass

    def test_invalid_customer_invalid_state(self):
        Customer.objects.create(
            first_name = "Amy",
            last_name = "Test",
            email = "AmyTest@gmail.com",
            address_1 = "123 S. Denver",
            city = "Denver",
            state = "State is too long. State is too long. State is too long. State is too long. State is too long. State is too long. State is too long. State is too long. State is too long. State is too long. State is too long. State is too long. State is too long. State is too long. State is too long. State is too long.",
            zip_code = "80123")

        try:
            invalid_customer = Customer.objects.get(first_name = "Amy")
            invalid_customer.full_clean()
            invalid_customer.save()
        except ValidationError:
            pass

    def test_invalid_customer_invalid_zip_code(self):
        Customer.objects.create(
            first_name = "Amy",
            last_name = "Test",
            email = "AmyTest@gmail.com",
            address_1 = "123 S. Denver",
            city = "Denver",
            state = "Colorado",
            zip_code = "NoRealZipCode")

        try:
            invalid_customer = Customer.objects.get(first_name = "Amy")
            invalid_customer.full_clean()
            invalid_customer.save()
        except ValidationError:
            pass
    
    def test_customer_to_string(self):
        Customer.objects.create(
            first_name = "Amy",
            last_name = "Test",
            email = "AmyTest@gmail.com",
            address_1 = "123 S. Denver",
            city = "Denver",
            state = "Colorado",
            zip_code = "80123")

        valid_customer = Customer.objects.get(first_name="Amy")
        self.assertEqual(str(valid_customer), "Test")

class OrderTestCase(TestCase):
    def test_valid_order(self):
        Customer.objects.create(
            first_name = "Amy",
            last_name = "Test",
            email = "AmyTest@gmail.com",
            address_1 = "123 S. Denver",
            city = "Denver",
            state = "Colorado",
            zip_code = "80123")

        test_customer = Customer.objects.get(first_name="Amy")

        Order.objects.create(
            customer = test_customer,
            complete = "False",
            transaction_id = "1")

        valid_order = Order.objects.get(customer=test_customer)
        self.assertIsNotNone(valid_order)

    def test_invalid_order_invalid_customer(self):
        Book.objects.create(
            isbn = "195153448",
            title = "Classical Mythology",
            authors = "Mark P. O. Morford",
            year_public = "2002",
            publisher = "Oxford University Press",
            thumbnail_pic = "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
            quantity = 10,
            price = 10)

        test_book = Book.objects.get(isbn="195153448")

        with self.assertRaises(ValueError):
            Order.objects.create(
                customer = test_book,
                complete = "False",
                transaction_id = "1")

    def test_invalid_order_invalid_complete_status(self):
        with self.assertRaises(ValidationError):
            Order.objects.create(
                customer = None,
                complete = "notBoolean",
                transaction_id = "123 S. Denver")

    def test_invalid_order_invalid_customer(self):
        Customer.objects.create(
            first_name = "Amy",
            last_name = "Test",
            email = "AmyTest@gmail.com",
            address_1 = "123 S. Denver",
            city = "Denver",
            state = "Colorado",
            zip_code = "80123")

        test_customer = Customer.objects.get(first_name="Amy")

        Order.objects.create(
            customer = test_customer,
            complete = "False",
            transaction_id = "transaction_idtransaction_idtransaction_idtransaction_idtransaction_idtransaction_idtransaction_idtransaction_idtransaction_id")

        try:
            invalid_order = Order.objects.get(customer=test_customer)
            invalid_order.full_clean()
            invalid_order.save()
        except ValidationError:
            pass

    def test_order_to_string(self):
        Customer.objects.create(
            first_name = "Amy",
            last_name = "Test",
            email = "AmyTest@gmail.com",
            address_1 = "123 S. Denver",
            city = "Denver",
            state = "Colorado",
            zip_code = "80123")

        test_customer = Customer.objects.get(first_name="Amy")

        Order.objects.create(
            customer = test_customer,
            complete = "False",
            transaction_id = "1")

        order = Order.objects.get(customer=test_customer)

        self.assertEqual(str(order), "1")

    def test_order_cart_total(self):
        Customer.objects.create(
            first_name = "Amy",
            last_name = "Test",
            email = "AmyTest@gmail.com",
            address_1 = "123 S. Denver",
            city = "Denver",
            state = "Colorado",
            zip_code = "80123")

        test_customer = Customer.objects.get(first_name="Amy")

        Order.objects.create(
            customer = test_customer,
            complete = "False",
            transaction_id = "1")

        order = Order.objects.get(customer=test_customer)

        self.assertEqual(order.get_cart_total, 0)

    def test_order_cart_items(self):
        Customer.objects.create(
            first_name = "Amy",
            last_name = "Test",
            email = "AmyTest@gmail.com",
            address_1 = "123 S. Denver",
            city = "Denver",
            state = "Colorado",
            zip_code = "80123")

        test_customer = Customer.objects.get(first_name="Amy")

        Order.objects.create(
            customer = test_customer,
            complete = "False",
            transaction_id = "1")

        order = Order.objects.get(customer=test_customer)

        self.assertEqual(order.get_cart_items, 0)

class OrderItemCase(TestCase):
    def setUp(self):
        Book.objects.create(
            isbn = "195153448",
            title = "Classical Mythology",
            authors = "Mark P. O. Morford",
            year_public = "2002",
            publisher = "Oxford University Press",
            thumbnail_pic = "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
            quantity = 10,
            price = 10)

        self.test_book = Book.objects.get(isbn="195153448")
        
        Customer.objects.create(
            first_name = "Amy",
            last_name = "Test",
            email = "AmyTest@gmail.com",
            address_1 = "123 S. Denver",
            city = "Denver",
            state = "Colorado",
            zip_code = "80123")

        self.test_customer = Customer.objects.get(first_name="Amy")
        
    def test_valid_order_item(self):
        Order.objects.create(
            customer = self.test_customer,
            complete = "False",
            transaction_id = "1")

        test_order = Order.objects.get(customer=self.test_customer)

        OrderItem.objects.create(
            product = self.test_book,
            order = test_order,
            quantity = 1)

        valid_order_item = OrderItem.objects.get(order=test_order)

        self.assertIsNotNone(valid_order_item)

    def test_invalid_order_item_invalid_product(self):
        Order.objects.create(
            customer = self.test_customer,
            complete = "False",
            transaction_id = "1")

        test_order = Order.objects.get(customer=self.test_customer)

        with self.assertRaises(ValueError):
            OrderItem.objects.create(
                product = self.test_customer,
                order = test_order,
                quantity = 1)

    def test_invalid_order_item_invalid_order(self):
        with self.assertRaises(ValueError):
            OrderItem.objects.create(
                product = self.test_book,
                order = self.test_book,
                quantity = 1)

    def test_invalid_order_item_invalid_quantity(self):
        Order.objects.create(
            customer = self.test_customer,
            complete = "False",
            transaction_id = "1")

        test_order = Order.objects.get(customer=self.test_customer)

        with self.assertRaises(ValueError):
            OrderItem.objects.create(
                product = self.test_book,
                order = test_order,
                quantity = "not a number")

    def test_order_item_get_total(self):
        Order.objects.create(
            customer = self.test_customer,
            complete = "False",
            transaction_id = "1")

        test_order = Order.objects.get(customer=self.test_customer)

        OrderItem.objects.create(
            product = self.test_book,
            order = test_order,
            quantity = 1)

        order_item = OrderItem.objects.get(order=test_order)

        self.assertEqual(order_item.get_total, 10)

class RentItemCase(TestCase):
    def setUp(self):
        Book.objects.create(
            isbn = "195153448",
            title = "Classical Mythology",
            authors = "Mark P. O. Morford",
            year_public = "2002",
            publisher = "Oxford University Press",
            thumbnail_pic = "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
            quantity = 10,
            price = 10)

        self.test_book = Book.objects.get(isbn="195153448")
        
        Customer.objects.create(
            first_name = "Amy",
            last_name = "Test",
            email = "AmyTest@gmail.com",
            address_1 = "123 S. Denver",
            city = "Denver",
            state = "Colorado",
            zip_code = "80123")

        self.test_customer = Customer.objects.get(first_name="Amy")

        Order.objects.create(
            customer = self.test_customer,
            complete = "False",
            transaction_id = "1")

        self.test_order = Order.objects.get(customer=self.test_customer)

    def test_valid_rent_item(self):
        RentItem.objects.create(
            product1 = self.test_book,
            order1 = self.test_order,
            quantity1 = 1)

        valid_rent_item = RentItem.objects.get(order1=self.test_order)

        self.assertIsNotNone(valid_rent_item)

    def test_invalid_rent_item_invalid_product(self):
        with self.assertRaises(ValueError):
            RentItem.objects.create(
                product1 = self.test_customer,
                order1 = self.test_order,
                quantity1 = 1)

    def test_invalid_rent_item_invalid_order(self):
        with self.assertRaises(ValueError):
            RentItem.objects.create(
                product1 = self.test_book,
                order1 = self.test_book,
                quantity1 = 1)

    def test_invalid_rent_item_invalid_quantity(self):
        with self.assertRaises(ValueError):
            RentItem.objects.create(
                product1 = self.test_book,
                order1 = self.test_order,
                quantity1 = "not a number")

class ViewsTestCase(TestCase):
    def setUp(self):
        self.credentials = {
            'username' : 'testuser',
            'password' : 'testpass'
        }
        
        User.objects.create_user(**self.credentials)

        self.test_user = User.objects.get(username="testuser")
        self.assertIsNotNone(self.test_user)
        
        Book.objects.create(
            isbn = "195153448",
            title = "Classical Mythology",
            authors = "Mark P. O. Morford",
            year_public = "2002",
            publisher = "Oxford University Press",
            thumbnail_pic = "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
            quantity = 10,
            price = 10)
        
        self.test_book = Book.objects.get(isbn="195153448")
        
        Book.objects.create(
            isbn = "771074670",
            title = "Nights Below Station Street",
            authors = "David Adams Richards",
            year_public = "1988",
            publisher = "Emblem Editions",
            thumbnail_pic = "http://images.amazon.com/images/P/0771074670.01.MZZZZZZZ.jpg",
            quantity = 10,
            price = 10)
        
        self.test_book_2 = Book.objects.get(isbn="771074670")
        
        Customer.objects.create(
            user = self.test_user,
            first_name = "Amy",
            last_name = "Test",
            email = "AmyTest@gmail.com",
            address_1 = "123 S. Denver",
            city = "Denver",
            state = "Colorado",
            zip_code = "80123")
        
        self.test_customer = Customer.objects.get(first_name="Amy")
        
        Order.objects.create(
            customer = self.test_customer,
            complete = "False",
            transaction_id = "1")
        
        self.test_order = Order.objects.get(customer=self.test_customer)
        
        OrderItem.objects.create(
            product = self.test_book,
            order = self.test_order,
            quantity = 4)
        
        RentItem.objects.create(
            product1 = self.test_book_2,
            order1 = self.test_order,
            quantity1 = 1)

    def create_n_books(self, n):
        for i in range(n):
            Book.objects.create(
                isbn = "19515345" + str(i),
                title = "Book" + str(i),
                authors = "Test book author",
                year_public = "2002",
                publisher = "Oxford University Press",
                thumbnail_pic = "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
                quantity = 10,
                price = 10)
    
    def test_home_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_books_view_authenticated(self):
        self.client.post('/login/', self.credentials)
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')
    
    def test_books_view_authenticated_featured(self):
        self.client.post('/login/', self.credentials)
        response = self.client.post('/books/', {'book-filterd' : 'featured'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')
    
    def test_books_view_authenticated_titles_az(self):
        self.client.post('/login/', self.credentials)
        response = self.client.post('/books/', {'book-filterd' : 'titles_az'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')
    
    def test_books_view_authenticated_title(self):
        self.client.post('/login/', self.credentials)
        response = self.client.post('/books/', {'book-filterd' : 'title'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')
    
    def test_books_view_authenticated_authors(self):
        self.client.post('/login/', self.credentials)
        response = self.client.post('/books/', {'book-filterd' : 'authors'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')
    
    def test_books_view_authenticated_price(self):
        self.client.post('/login/', self.credentials)
        response = self.client.post('/books/', {'book-filterd' : 'price'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')
    
    def test_books_view_authenticated_dash_price(self):
        self.client.post('/login/', self.credentials)
        response = self.client.post('/books/', {'book-filterd' : '-price'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')
    
    def test_books_view_unauthenticated(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')
        
    def test_aboutus_view_authenticated(self):
        self.client.post('/login/', self.credentials)
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutus.html')
    
    def test_aboutus_view_unauthenticated(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutus.html')
    
    def test_checkout_view_authenticated(self):
        self.client.post('/login/', self.credentials)
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')
    
    def test_checkout_view_unauthenticated(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')
   
    def test_cart_view_authenticated(self):
        self.client.post('/login/', self.credentials)
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')
    
    def test_cart_view_unauthenticated(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')
    
    def test_loginPage(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_active)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_loginPage_already_authenticated(self):
        self.client.post('/login/', self.credentials)
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_active)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_loginPage_invalid_credentials(self):        
        response = self.client.post('/login/', None, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_active)
        self.assertTemplateUsed(response, 'login.html')
    
    def test_signupPage(self):
        form_values = {
            'username' : 'testuser',
            'password1' : 'testpass',
            'password2' : 'testpass',
            'first_name' : 'test',
            'last_name' : 'user',
            'email' : 'test@user.com',
            'address_1' : 'test',
            'city' : 'test',
            'state' : 'test',
            'zip_code' : '12345'
        }
        response = self.client.post('/signup/', form_values)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
    
    def test_signupPage_get_request(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
    
    def test_signupPage_already_authenticated(self):
        self.client.post('/login/', self.credentials)
        response = self.client.get('/signup/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_active)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_logoutPage(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_product_view_valid_book(self):
        response = self.client.get('/product/195153448')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product.html')
    
    def test_successcheckout_view_Not_Authenticated(self):
        response = self.client.get('/successcheckout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout-success.html')
    
    def test_successcheckout_view_Authenticated_Purchase_Book(self):
        self.client.post('/login/', self.credentials)
        
        response = self.client.get('/successcheckout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout-success.html')
        
        test_book = Book.objects.get(isbn="195153448")
        test_book_2 = Book.objects.get(isbn="771074670")
        
        self.assertEqual(6, test_book.quantity)
        self.assertEqual(9, test_book_2.quantity)
    
    def test_randombooks_view(self):
        self.create_n_books(20)
        response = self.client.get('/randombooks/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'genre-products.html')
    
    def test_booksunder_view(self):
        response = self.client.get('/booksunder/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'genre-products.html')
    
    def test_newestbook_view(self):
        self.create_n_books(20)
        response = self.client.get('/newestbooks/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'genre-products.html')
    
    def test_searched_view(self):
        response = self.client.post('/bookstore/search', {'searched': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
    
    def test_searched_view_get_request(self):
        response = self.client.get('/bookstore/search')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
    
    def test_submit_review(self):
        self.client.post('/login/', self.credentials)
        header = {'HTTP_REFERER': '/product/195153448'}
        review = {'rate': '5', 'subject': 'test', 'review': 'test'}
        response = self.client.post('/submit_review/195153448', review, **header, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product.html')

class ReviewRatingTestCase(TestCase):
    """ Test case for Review and Rating Models """
    
    def setUp(self):
        Book.objects.create(
            isbn = "195153448",
            title = "Classical Mythology",
            authors = "Mark P. O. Morford",
            year_public = "2002",
            publisher = "Oxford University Press",
            thumbnail_pic = "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
            quantity = 10,
            price = 10)
        self.test_book = Book.objects.get(isbn="195153448")
    
        Customer.objects.create(
            first_name = "Amy",
            last_name = "Test",
            email = "AmyTest@gmail.com",
            address_1 = "123 S. Denver",
            city = "Denver",
            state = "Colorado",
            zip_code = "80123")

        self.test_customer = Customer.objects.get(first_name="Amy")

    
    def test_invalid_user(self):
        with self.assertRaises(ValueError):
            ReviewRating.objects.create(
                user = self.test_book
            )
            
    def test_invalid_book(self):
        with self.assertRaises(ValueError):
            ReviewRating.objects.create(
                book = self.test_customer
            )
            
    def test_invalid_rate(self):
        with self.assertRaises(ValueError):
            ReviewRating.objects.create(
                rate = "Vầng Trăng Xưa",
            )
