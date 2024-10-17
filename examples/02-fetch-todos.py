"""
Fetch list of TODOs from Logseq
"""
from logspyk import LogseqAPI

logseq = LogseqAPI()

todos = logseq.db.q("(task TODO)")
print(todos)
