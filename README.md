# Logspyq

Python for Logseq API and Plugins


## Examples:


### Display notification in Logseq 

```python

from logspyq import LogseqAPI

logseq = LogseqAPI(auth_token="test")

logseq.call("logseq.UI.showMsg", "Hello from Python!")
```


You can use the API in async code as-is:

```python
import asyncio
from logspyq import LogseqAPI

logseq = LogseqAPI(auth_token="test")


async def main():
    await logseq.call("logseq.UI.showMsg", "Hello from Python!")


asyncio.run(main())
```

References:
- [Logseq Local API Server](https://docs.logseq.com/#/page/local%20http%20server)