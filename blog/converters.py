from django.urls.converters import StringConverter

class SlugUnicodeConverter(StringConverter):
    regex = r'[-\w]+'

class FourDigitYearConverter:
    regex = r'2[01]\d{2}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value