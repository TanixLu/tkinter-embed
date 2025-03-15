from setuptools import setup, find_packages
from setuptools.command.install import install
import sys
import shutil
from pathlib import Path


class CustomInstall(install):
    """Custom installation command to deploy tkinter files after installation"""

    def run(self):
        install.run(self)
        self._deploy_files()

    def _deploy_files(self):
        data_dir = Path(__file__).parent / "src" / "tkinter_embed" / "data"
        py_tag = f"cp{sys.version_info.major}{sys.version_info.minor}"
        src_dir = data_dir / py_tag

        if hasattr(self, "install_lib") and self.install_lib:
            dest_dir = Path(self.install_lib).resolve()
        else:
            dest_dir = Path(sys.executable).parent.resolve()

        if src_dir.exists():
            for item in src_dir.iterdir():
                dest_path = dest_dir / item.name
                shutil.move(str(item), str(dest_path))
            print("Tkinter files deployment completed!")
        else:
            print(f"Warning: Source directory not found: {src_dir}")

        # Clean up by removing the entire data directory
        try:
            if data_dir.exists():
                shutil.rmtree(data_dir)
                print(f"Removed data directory: {data_dir}")
        except Exception as e:
            print(f"Warning: Could not remove data directory: {e}")


setup(
    name="tkinter-embed",
    version="1.0.0",
    description="Tkinter for Windows Embedded Python",
    author="Tanix",
    author_email="tanixlu@foxmail.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "tkinter_embed": [
            "data/*",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development",
    ],
    cmdclass={
        "install": CustomInstall,
    },
)
