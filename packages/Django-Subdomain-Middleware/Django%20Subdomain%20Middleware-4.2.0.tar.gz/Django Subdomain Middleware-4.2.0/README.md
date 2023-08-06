# Djano Subdomain Middleware

The Django subdomain middleware provides the ability to configure
different url configurations for each subdomain.

## How To Install

This package can be installed using Pip. Prior to doing so however you
should identify the version that you require.

The versioning of this package matches the versioning of Django.
Therefore, if you are using Django 4.2 you should use version 4.2 of
this package.

Once you have identified the version you can simply do something along
the lines of:

```bash
pip install django_subdomain_middleware>=4.2,<5
```

## How To Use

To use this package simple do the following:

### Add django_subdomain_middleware To The Middleware

Within settings.py there will be a list assigned to the MIDDLEWARE
constant. Add the following to it after common:

```python
"django_subdomain_middleware.subdomain.Subdomain",
```

so that it looks like:

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django_subdomain_middleware.subdomain.Subdomain",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
```

Doing this will provide a subdomain entry in any request object.

### Add Subdomain Routing

If you would like to route based on the subdomain then the following
should also be carried out:

```python
SUBDOMAIN_URL_CONF = {
    'test': "project_name.testurls",
    '*': "project_name.wildcardurls",
}
```

In the above example test.domain.com would use the url configuration
called testurls in project_name, * acts as a wildcard, therefore,
any other subdomain will be routed towards the url configuration
called wildcardurls.

In the event that either of the following occurs the standard
default url configuration will be used:

* A subdomain is visited but no configuration or wildcard exists.
* A visitor goes directly to the allowed hosts domain.
