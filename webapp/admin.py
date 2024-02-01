from django.contrib import admin
from .models import Users
from .models import Donor
from .models import WigRecipient
from .models import Wig
from .models import DistributionHistory
from .models import Donation
from .models import UserAccount


admin.site.register(Users)
admin.site.register(Donor)
admin.site.register(WigRecipient)
admin.site.register(Wig)
admin.site.register(DistributionHistory)
admin.site.register(Donation)
admin.site.register(UserAccount)