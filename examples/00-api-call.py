"""
Use Logseq REST API to display notification in the Logseq desktop app.
"""

from logspyq import LogseqAPI

logseq = LogseqAPI(auth_token="test")

logseq.call(
    "logseq.UI.showMsg",
    "Hello from Python!",
    "success",
    {"key": "unique-key", "timeout": 5000},
)
