from django.contrib import admin
from cmbs.models import Deal, Loan, Property, Lease, Keywords, Articles, Publisher

admin.site.register(Deal)
admin.site.register(Loan)
admin.site.register(Property)
admin.site.register(Lease)
admin.site.register(Keywords)
admin.site.register(Articles)
# admin.site.register(Keyword)
# admin.site.register(Article)
admin.site.register(Publisher)
