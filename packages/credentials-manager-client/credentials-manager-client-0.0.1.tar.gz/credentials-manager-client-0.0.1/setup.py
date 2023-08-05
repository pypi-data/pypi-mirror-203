import os
from setuptools import setup, find_packages

install_requires = [
    ('psycopg2-binary', '2.9.5'),
    ('alembic', '1.8.1'),
    ('environs', '9.5.0'),
    ('psutil', '5.9.4'),
    ('fastapi', '0.85.0'),
    ('pydantic', '1.9.2'),
    ('SQLAlchemy', '1.4.36'),
]

CI_PROJECT_NAME = os.environ.get("CI_PROJECT_NAME", "credentials_manager")
ARTIFACT_VERSION = os.environ.get("ARTIFACT_VERSION", "0.1a+")
CI_PROJECT_TITLE = os.environ.get("CI_PROJECT_TITLE", "Backend service")
CI_PROJECT_URL = os.environ.get("CI_PROJECT_URL", "https://github.com/makersdevs/credentials_manager")

setup(
    name=CI_PROJECT_NAME,
    version=ARTIFACT_VERSION,
    description=CI_PROJECT_TITLE,
    url=CI_PROJECT_URL,
    install_requires=[">=".join(req) for req in install_requires],
    python_requires=">=3.10.3",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            CI_PROJECT_NAME + " = " + "credentials_manager.main:execute",
        ]
    }
)
