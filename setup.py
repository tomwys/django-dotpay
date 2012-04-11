from setuptools import setup
    
setup(
    name = 'django-dotpay',
    version = '0.2.7',
    author = 'Krzysztof Hoffmann',
    author_email = 'krzysiekpl@gmail.com',
    license='BSD',
    url = 'https://github.com/hoffmannkrzysztof/django-dotpay/',
    packages = ['dotpay','dotpay.sms','dotpay.payment'],
    )
