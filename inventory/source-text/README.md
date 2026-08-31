# source-text/

Plain text of each old-site page, exactly as whoever fetched it saw it.

One file per page, named for its inventory prefix: `BL.txt`, `HOME.txt`,
`DONATE.txt` and so on. See the PAGES table in `../HERMES-PROMPT.md`.

`verify-inventory.py` checks every quoted line in the inventory against these
files. That is why they exist: the inventory is verified against what was
actually on the page at capture time, so a later change to the live site cannot
silently invalidate the check.

`BL.txt` is present as a worked example. The rest arrive with the inventory.
