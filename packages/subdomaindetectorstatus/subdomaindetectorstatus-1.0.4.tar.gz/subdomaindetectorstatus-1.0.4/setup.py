import setuptools

with open("README.md", "r") as fh:
    long_des = fh.read()

setuptools.setup(
    name="subdomaindetectorstatus",
    version="1.0.4",
    author="Hariharan C",
    description="This tools is used to bruteforce all the subdomain of the domain and filterout the live sites into domain folder",
    python_requires='>=3.6'
) 