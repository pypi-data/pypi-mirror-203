import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "iosense_connect_onprem",
    version = "0.0.1",
    author = "Faclon-Labs",
    author_email = "reachus@faclon.com",
    description = "iosense connect library",
    packages = ["iosense_connect_onprem"]
)