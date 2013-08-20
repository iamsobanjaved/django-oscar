from django.test import TestCase

from oscar.apps.partner import availability
from oscar.test import factories


class TestDelegateToStockRecordWrapper(TestCase):

    def setUp(self):
        self.product = factories.create_product()
        self.stockrecord = factories.create_stockrecord(self.product)
        self.assertTrue(self.product.get_product_class().track_stock)

        self.availability = availability.DelegateToStockRecord(
            self.product, self.stockrecord)

    def test_delegates_is_available_to_buy(self):
        self.assertEquals(
            self.stockrecord.is_available_to_buy,
            self.availability.is_available_to_buy)

    def test_delegates_is_purchase_permitted(self):
        self.assertEquals(
            self.stockrecord.is_purchase_permitted(1),
            self.availability.is_purchase_permitted(quantity=1))

    def test_delegates_availability_code(self):
        self.assertEquals(
            self.stockrecord.availability_code,
            self.availability.code)

    def test_delegates_availability_message(self):
        self.assertEquals(
            self.stockrecord.availability,
            self.availability.message)

    def test_delegates_lead_time(self):
        self.assertEquals(
            self.stockrecord.lead_time,
            self.availability.lead_time)

    def test_delegates_dispatch_date(self):
        self.assertEquals(
            self.stockrecord.dispatch_date,
            self.availability.dispatch_date)
