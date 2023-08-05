from setuptools import setup

with open("README.md", "r", encoding='utf-8') as arq:
    readme = arq.read()

setup(
    name='vagas_cfs',
    version='0.1',
    author='Gabriel Ernesto Barboza Pereira',
    author_email='ernesto.gabriel@pucpr.br',
    packages=['vagas_cfs'],
    description='Conversor utilizado para a geração do Relatório de Vagas dos CFS',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='conversor vagas_cfs',
)
