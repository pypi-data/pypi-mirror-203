# yakui
Advanced Logging in Python
# Installation
You can install `yakui` with Python Installer of Python (`pip`)
```bash
pip install yakui
```
# Examples
`examples/basic.py`
```py
from yakui import Logger


logger = Logger(name="basic")


logger.info("Hello, world!")
logger.warn("Hello, world!")
logger.debug("Hello, world!")
logger.error("Hello, world!")
logger.fatal("Hello, world!")
```