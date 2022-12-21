## Test project to demonstrate possible Django bug

This test project contains a single testcase to demonstrate what is possibly a Django bug.

We are testing the preference order of translation files in Django. According to 
[the documentation](https://docs.djangoproject.com/en/4.1/topics/i18n/translation/#how-django-discovers-translations),
translations are loaded according to the following:
1) the directories listed in `LOCALE_PATHS`;
2) the `locale` directories in each installed apps in `INSTALLED_APPS`;
3) Django-provided translations.

The project has i18n enabled, and contains the translation for a single string, `Active`, which has been translated
in Italian as `Operativo`. The folder containing the translation is listed in `LOCALE_PATHS` and should therefore have
the highest preference.

The dependency `django-extensions` contains a different translation for `Active`: `Attivo`; since `django_extension` is
listed in `INSTALLED_APPS`, this translation should get a lower preference and should not be used.

The test simply runs `assert _("Active") == "Operativo"` to prove that the translation included in the project takes
precedence over the one defined in `django-extensions`. The test currently fails.

To prove that the translation included in `django-extensions` is picked, simply comment it out of `INSTALLED_APPS`: the
test now passes.

Interestingly, by removing `Plural-Forms` from this project's `django.po` (and recompiling the messages) the test passes.
As another hint, if we instead add `Plural-Forms` to `django-extensions`'s `django.po`, the test also passes.
