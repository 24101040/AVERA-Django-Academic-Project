from django.test import TestCase
from django.urls import reverse
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


class FeedbackViewTest(TestCase):

    def test_feedback_list_page_loads(self):
        response = self.client.get(reverse('feedback_list'))
        self.assertEqual(response.status_code, 200)

    def test_feedback_create_page_loads(self):
        response = self.client.get(reverse('feedback_create'))
        self.assertEqual(response.status_code, 200)

    def test_feedback_creation_redirects(self):
        response = self.client.post(reverse('feedback_create'), {
            'supporter_name': 'Jerin',
            'gift': 'Books',
            'comment': 'Thank you!'
        })

        self.assertRedirects(
            response,
            reverse('feedback_list')
        )

        self.assertEqual(SupporterFeedback.objects.count(), 1)
