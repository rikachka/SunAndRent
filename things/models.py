from django.db import models


RESERVATION_TYPES = (
    ('0', 'is_rented'),
    ('1', 'is_cancelled'),
    ('2', 'is_declined')
)

GOOD_STATUS = (
    ('0', 'at_service'),
    ('1', 'at_home'),
    ('2', 'damaged'),
    ('3', 'lost')
)


class Customer(models.Model):
    login = models.CharField('login', max_length=200)
    first_name = models.CharField('first name', max_length=200)
    last_name = models.CharField('last name', max_length=200)
    phone = models.CharField('phone number', max_length=20)
    email = models.CharField('e-mail', max_length=100)
    address = models.CharField('address', max_length=200)
    
    def __str__(self):
        return str(self.id) + " " + self.last_name


class Good(models.Model):
    title = models.CharField('title', max_length=100)
    owner_id = models.ForeignKey(Customer)
    good_info = models.CharField('good info', max_length=1000)
    reservation_type = models.CharField('type', max_length=1, choices=RESERVATION_TYPES)
    image_path = models.CharField('image', max_length=200)
    status = models.CharField('status', max_length=1, choices=GOOD_STATUS)
    
    def __str__(self):
        return '{} {}'.format(self.pk, self.title)


class StoragedGood(models.Model):
    good_id = models.ForeignKey(Good)
    start_date = models.DateTimeField('beginning of the storaging')
    end_date = models.DateTimeField('end of the storaging')


class Reservation(models.Model):
    start_date = models.DateTimeField('start date of the reservation')
    end_date = models.DateTimeField('end date of the reservation')
    return_date = models.DateTimeField('date of return', blank=True, null=True)
    customer_id = models.ForeignKey(Customer)
    good_id = models.ForeignKey(Good)

