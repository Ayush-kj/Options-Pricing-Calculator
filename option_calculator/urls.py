
from django.contrib import admin
from django.urls import path
from cal.views import two_step
from cal.views import n_step
from cal.views import black_scholes
from cal.views import home_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('two steps', two_step),
    path('n steps', n_step),
    path('black scholes', black_scholes),
]
