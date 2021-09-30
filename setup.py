from setuptools import setup, find_packages

setup(
        name="q2-utensil", 
        version='0.0.1',
        packages=find_packages(),
        author="Keegan Evan",
        author_email="keegan.evans@gmail.com",
        url="keeganevans.com",
        license="BSD-3-Clause",
        description="Some examples for Semantic Validation",
        entry_points={
            "qiime2.plugins":
            ["q2-utensils=q2_utensils.plugin_setup:plugin"]},
        package_data={},
        zip_safe=False
        ) 
