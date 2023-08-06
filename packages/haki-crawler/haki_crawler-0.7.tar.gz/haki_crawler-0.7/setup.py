from setuptools import setup, find_packages
import os
import shutil



LIB_NAME = "haki_crawler"


thu_muc_can_xoa = ["build", "dist", "{}.egg-info".format(LIB_NAME)]

for thu_muc in thu_muc_can_xoa:
    if os.path.exists(thu_muc):
        shutil.rmtree(thu_muc)
        print(f"Đã xóa thư mục: {thu_muc}")
    else:
        print(f"Thư mục {thu_muc} không tồn tại")

setup(
    name=LIB_NAME,
    version="0.7",
    packages=find_packages(),
    install_requires=[
        # Danh sách các gói phụ thuộc của gói này
        "requests",
    ],
    author="namhn1495",
    author_email="namhn1495@gmail.com",
    description="A short description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://example.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
