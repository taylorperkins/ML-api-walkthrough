from setuptools import setup


setup(
    name='application',
    packages=['application'],
    include_package_data=True,
    install_requires=[
        'flask',
        'numpy==1.16.3',
        'scikit-learn==0.20.3',
        'scipy==1.2.1',
        'PyYAML==5.1',
        'Flask-Api==1.1',
        'marshmallow==2.19.2',
        'gunicorn==19.9.0',
        'locustio'
    ],
)