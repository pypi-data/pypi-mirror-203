"""Django middleware to handle subdomains."""
from typing import Callable

from django.conf import settings
from django.http.request import HttpRequest


class Subdomain:
    """Django subdomain middleware."""

    def __init__(self, get_response: Callable):
        """
        Init to setup.

        Args:
            get_response: get_response callable.
        """
        self._get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpRequest:
        """
        Handle the business logic for each call.

        Args:
            request:

        Returns:
            HttpRequest generated from get_response with our modified request.
        """
        self._set_subdomain(request=request)
        self._set_url_conf(request=request)
        response = self._get_response(request)
        return response

    def _set_url_conf(self, request: HttpRequest):
        """
        Identify the expected urlconf and populate it in the request object.

        Args:
            request: The request object
        """
        if not (request.subdomain and hasattr(settings, "SUBDOMAIN_URL_CONF")):
            return
        urlconfs: dict = settings.SUBDOMAIN_URL_CONF
        default_conf = urlconfs.get("*", None)
        urlconf = urlconfs.get(request.subdomain, None)
        if urlconf:
            request.urlconf = urlconf
        elif default_conf:
            request.urlconf = default_conf

    def _set_subdomain(self, request: HttpRequest):
        """
        Identify and populate the subdomain in the request object.

        Args:
            request: The request object
        """
        try:
            hostname = request.META["HTTP_HOST"]
        except KeyError:
            return

        allowed_hosts = []
        for allow_host in settings.ALLOWED_HOSTS:
            if allow_host.startswith("."):
                allowed_hosts.append(allow_host)
                continue

        hostname_split = hostname.split(":")
        hostname = hostname_split[0]

        subdomain = hostname.split(".")[0]
        length = len(subdomain) + 1
        hostname_without_subdomain = hostname[length:]
        if f".{hostname_without_subdomain}" in allowed_hosts:
            subdomain = subdomain
        else:
            subdomain = ""
        request.subdomain = f"{subdomain}" if subdomain else ""
