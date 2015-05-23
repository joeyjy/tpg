from django.conf.urls import patterns, url

from package.views import PackageList

urlpatterns = patterns(
    "",
    url(r"^$", PackageList.as_view(), name="package_list"),
)
