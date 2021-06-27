from distutils.core import setup

setup(
    name="teamx-two-factor-auth",  # How you named your package folder (MyLib)
    packages=[
        "two_factor_auth",
        "two_factor_auth/migrations",
    ],  # Chose the same as "name"
    version="0.0.6",  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="Package to enable two factor authentication using DRF",  # Give a short description about your library
    author="TeamX",  # Type in your name
    author_email="teamx@reckonsys.com",  # Type in your E-Mail
    url="https://github.com/rsys-teamx/django-2fa-qna",  # Provide either the link to your github or to your website
    download_url="https://github.com/rsys-teamx/django-2fa-qna/",
    keywords=["2FA", "Reckonsys Hackathon Submission", "team"],
    install_requires=[
        "jwt",
        "Django",
        "djangorestframework",
        "orm_choices",
        "djangorestframework-simplejwt",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3.9"
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
    ],
)
