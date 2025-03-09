from setuptools import setup, find_packages

setup(
    name="actividad2",
    version="0.0.1",
    author="Gepsi Quintero",
    author_email="",
    description="",
    py_modules=["actividad2"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests", # Páquete separado
        "matplotlib",  # Páquete separado
        "numpy",  # Páquete separado
        "seaborn"  # Páquete separado
        
    ]
) 