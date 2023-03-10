from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='berrycheck',
    version='1.0.5',
    license='MIT License',
    author='Eduardo de Sousa e Carlos Henrique',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='eduardosousa1718@gmail.com, ch123carlos@gmail.com',
    keywords='berry check',
    description=u'Fornecer aos usuários uma maneira fácil e acessível de obter cotações atualizadas de várias moedas, incluindo as principais moedas do mundo, para fins de negociação, investimento ou outras finalidades financeiras. Além dos preços de ações das principais empresas brasileiras.',
    packages=['berry_check'],
    install_requires=['requests', 'bs4', 'typing', 'yfinance'],)

