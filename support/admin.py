from django.contrib import admin
from .models import Gift  # support অ্যাপের Gift model

# নিশ্চিত করুন এই লাইনটি ফাইলে মাত্র একবারই আছে
admin.site.register(Gift)