from django.test import TestCase
from .models import SupporterFeedback
from .forms import SupporterFeedbackForm


class SupporterFeedbackTest(TestCase):

    def test_feedback_creation(self):
        feedback = SupporterFeedback.objects.create(
            supporter_name='Jerin',
            gift='Books',
            comment='Thank you for your support!'
        )

        self.assertEqual(feedback.supporter_name, 'Jerin')
        self.assertEqual(feedback.gift, 'Books')
        self.assertTrue(feedback.is_approved)

    def test_feedback_string_representation(self):
        feedback = SupporterFeedback.objects.create(
            supporter_name='Jerin',
            comment='Great support!'
        )

        self.assertEqual(
            str(feedback),
            f'Feedback #{feedback.id} - Jerin'
        )

    def test_feedback_form_valid(self):
        form = SupporterFeedbackForm(data={
            'supporter_name': 'Jerin',
            'gift': 'Books',
            'comment': 'Thank you!'
        })

        self.assertTrue(form.is_valid())
