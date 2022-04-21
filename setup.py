from distutils.core import setup

setup(
    name="GrandpaDos",
    py_modules=["grandpados"],
    entry_points={"console_scripts": ["grandpados=grandpados:main"]},
    version="0.1",
    description="Partial HTTPS DoS tool. A Slowloris rewrite in Python.",
    author="Onkar Singh",
    author_email="onkar.singh23@avenues.org",
    url="https://github.com/onkarbatra/grandpados",
    keywords=["dos", "http", "grandpados"],
    license="MIT",
)
