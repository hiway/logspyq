# Logspyq

Python for Logseq API and Plugins

## Examples:

### Display notification in Logseq 

```python
from logspyk import LogseqAPI

logseq = LogseqAPI()

logseq.UI.showMsg("Hello from Python!")
```

### Fetch all TODOs from Logseq

```python
from logspyk import LogseqAPI

logseq = LogseqAPI()

todos = logseq.db.q("(task TODO)")
print(todos)
```


References:
- [Logseq Local API Server](https://docs.logseq.com/#/page/local%20http%20server)