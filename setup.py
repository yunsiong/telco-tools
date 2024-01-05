# -*- coding: utf-8 -*-

import glob
import os

from setuptools import setup

pkg_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "telco_tools"))

agents = glob.glob(os.path.join(pkg_dir, "*_agent.*"))
assert len(agents) > 0, "Agents not compiled; run “npm install && npm run build” in agents/*/"

setup(
    name="telco-tools",
    version="12.3.0",
    description="Telco CLI tools",
    long_description="CLI tools for [Telco](https://telco.re).",
    long_description_content_type="text/markdown",
    author="Telco Developers",
    author_email="oleavr@telco.re",
    url="https://telco.re",
    install_requires=[
        "colorama >= 0.2.7, < 1.0.0",
        "telco >= 16.0.9, < 17.0.0",
        "prompt-toolkit >= 2.0.0, < 4.0.0",
        "pygments >= 2.0.2, < 3.0.0",
    ],
    license="wxWindows Library Licence, Version 3.1",
    zip_safe=False,
    keywords="telco debugger dynamic instrumentation inject javascript windows macos linux ios iphone ipad android qnx",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: JavaScript",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=["telco_tools"],
    package_data={
        "telco_tools": agents,
    },
    entry_points={
        "console_scripts": [
            "telco = telco_tools.repl:main",
            "telco-ls-devices = telco_tools.lsd:main",
            "telco-ps = telco_tools.ps:main",
            "telco-kill = telco_tools.kill:main",
            "telco-ls = telco_tools.ls:main",
            "telco-rm = telco_tools.rm:main",
            "telco-pull = telco_tools.pull:main",
            "telco-push = telco_tools.push:main",
            "telco-discover = telco_tools.discoverer:main",
            "telco-trace = telco_tools.tracer:main",
            "telco-itrace = telco_tools.itracer:main",
            "telco-join = telco_tools.join:main",
            "telco-create = telco_tools.creator:main",
            "telco-compile = telco_tools.compiler:main",
            "telco-apk = telco_tools.apk:main",
        ]
    },
)
