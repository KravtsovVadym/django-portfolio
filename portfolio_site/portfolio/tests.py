from django.test import TestCase
from portfolio.models import Portfolio
# Create your tests here.

class PortfolioTest(TestCase):
    
    def test_portfolio_creation_and_deletion(self):
        portfolio = Portfolio.objects.create(
            title = "TODO menager",
            description = "CRUD operations",
            image = "static/images/your_image.jpg",
            technologies = "Django, HTML, CSS",
            height_field = 100,
            width_field = 100,
            links = "https://github.com/KravtsovVadym/tasks_course"
        )

        self.assertIsNotNone(portfolio)

        portfolio.delete()

        self.assertFalse(Portfolio.objects.filter(id=portfolio.id).exists())

        