from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='fastapi-rate-limit',
    version='0.1.0',
    author='Oscar Arias',
    author_email='ariasp26@gmail.com',
    description='Control and limit request rates to FastAPI applications with Redis and local memory support.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/oscarPyth/fastapi-rate-limit',
    packages=find_packages(),
    install_requires=requirements,
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='fastapi ratelimiting api security',  # Palabras clave sobre tu paquete
    python_requires='>=3.9',  # Versión mínima requerida de Python
    project_urls={
        'Bug Reports': 'https://github.com/oscarPyth/fastapi-rate-limit/issues',
        'Source': 'https://github.com/oscarPyth/fastapi-rate-limit',
    },
)