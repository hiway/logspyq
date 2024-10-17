"""
Use Logseq REST API to display notification in the Logseq desktop app.
"""
from logspyk import LogseqAPI

logseq = LogseqAPI()

logseq.UI.showMsg("Hello from Python!")
