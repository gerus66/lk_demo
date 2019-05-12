"""
Backwards-compatible URLconf for existing django-registration
installs; this allows the standard ``include('registration.urls')`` to
continue working, but that usage is deprecated and will be removed for
django-registration 1.0. For new installs, use
``include('lkregistration.backends.default.urls')``.

"""

import warnings

warnings.warn("include('lkregistration.urls') is deprecated; use include('lkregistration.backends.default.urls') instead.",
              DeprecationWarning)
