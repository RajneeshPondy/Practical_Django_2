import os
from django.conf import settings
from django.test import TestCase
from django.core.files.images import ImageFile
from decimal import Decimal

from main import models


class TestSignal(TestCase):
    def test_thumbnails_are_generated_on_save(self):
        product = models.Product(
            name="The cathedral and the bazaar",
            price=Decimal("10.00"),
        )
        product.save()
        file_path = os.path.join(settings.BASE_DIR , "main/fixtures/the-cathedral-the-bazaar.jpg")
        with open(file_path, "rb") as f:
            image = models.ProductImage(
                product=product,
                image=ImageFile(f, name="tctb.jpg"),
            )
            with self.assertLogs("main", level="INFO") as cm:
                image.save()

        self.assertGreaterEqual(len(cm.output), 1)
        image.refresh_from_db()

        with open(file_path, "rb",) as f:
            expected_content = f.read()
            self.assertNotEqual(image.thumbnail.read(), expected_content)

        image.thumbnail.delete(save=False)
        image.image.delete(save=False)