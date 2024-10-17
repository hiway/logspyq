"""
Fetch list of TODOs from Logseq
"""
from logspyq import LogseqAPI

logseq = LogseqAPI()

todos = logseq.db.q("(task TODO)")
print(todos)
