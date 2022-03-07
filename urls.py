from django.urls import path, include
from . import views
from .ceh_modules import _1#, _2, _3, _4, _5, _6, _7, _8, _9
from .views import HomeView, RandomModuleView

urlpatterns = [
    path('', HomeView.as_view(), name='ceh_home'),
    #path('random/', RandomModuleView.as_view(modules = (_1, _2, _3, _4, _5, _6, _7, _8, _9)), name = 'all_random'),
    path('introduction_to_ethical_hacking/', RandomModuleView.as_view(modules = (_1,)), name = 'introduction_to_ethical_hacking'),
    #path('information_risk/', RandomModuleView.as_view(modules = (_2,)), name = 'rest_api'),
    #path('information_security_frameworks/', RandomModuleView.as_view(modules = (_3,)), name = 'information_security_frameworks'),
    #path('security_life_cycles/', RandomModuleView.as_view(modules = (_4,)), name = 'security_life_cycles'),
    #path('procedural_and_people_security_controls/', RandomModuleView.as_view(modules = (_5,)), name = 'procedural_and_people_security_controls'),
    #path('technical_security_controls/', RandomModuleView.as_view(modules = (_6,)), name = 'files_os'),
    #path('physical_and_environmental_security/', RandomModuleView.as_view(modules = (_7,)), name = 'physical_and_environmental_security'),
    #path('disaster_recovery_and_business_continuity_management/', RandomModuleView.as_view(modules = (_8,)), name = 'disaster_recovery_and_business_continuity_management'),
    #path('cryptography/', RandomModuleView.as_view(modules = (_9,)), name = 'files_os'),
] 