"""
Use Logseq REST API to display notification in the Logseq desktop app.
"""

import asyncio
from logspyq import LogseqAPI

logseq = LogseqAPI(auth_token="test")

async def main():
    await logseq.call("logseq.UI.showMsg", "Hello from Python!")


asyncio.run(main())
