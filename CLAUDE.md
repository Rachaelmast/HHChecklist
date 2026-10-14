# CLAUDE.md

## Working with Rachael
- Never ask the user to do something manually that you can do for them. Check your MCP servers, tools and connectors first; if you can do it, do it yourself.
- No hallucinations. Only state what you have checked. Say plainly when something is unknown or did not work.
- The user is not a developer. Explain changes in plain English, in a short list.
- No em dashes in any text shown to users. Keep wording short and plain.

## LHC Ownership Dashboard
- Source file: `lhc-ownership-dashboard.html` (single self-contained file, no build step). Backup: `lhc-ownership-dashboard.backup.html`.
- Published (team uses this): https://claude.ai/artifact/VynMtnxtra1asLNNA2sseq
- Do not change the BR, CT, ST or SNAP data arrays in the file.
- Contacts found in Gmail go into the published page's shared database, collection `contactsAdded` (doc id `gm-<email slug>`, `src: ["Gmail scan"]`). Fixes to built-in contacts go in `contactEdits/<contact id>`.
- Connected Gmail is rachaelskybridgehealthcare@gmail.com. LHC emails arrive there as forwards from the work address, so contacts are inside the forwarded bodies. LHC Group staff only.
- A daily routine (6:52 AM Eastern, in the original Claude session) adds new LHC contacts from Gmail and logs forwarded business development outreach emails into `bdlog`.
- Pending Submissions on the published page: live every 5 minutes for viewers with the Google Drive connector; everyone else reads an hourly copy in shared data `sync/latest` (fields `pending`, `jobs0..2` as CSV, `at`). Three fresh-session routines refresh it (Eastern time): hourly 9am-6pm plus 6:30pm Mon-Thu, hourly 9am-5pm Fri, none on weekends; they run on claude-haiku-5-5 (about $0.02 per run); `tools/sync_sheets.py` builds the same document by hand.
- Follow-up log: collection `followups` (fields key = rowKey(name + req or title+location), kind recruiter|client, at, by user id). Logged follow-ups in the last 48 hours turn orange/yellow rows blue.
- Tabs added: Open Jobs (LHC jobs from the job sheet; matched to submissions by Req ID digits or title+city+state) and Team Stats (from the Redzone sheet only, not all-time).
- Managers can cover several locations, so duplicate contacts are expected. Do not merge them.
- Business Dev tab: outreach log in collection `bdlog` (branch = BR id, contact, method, outcome, note, next, due, done, at, by or byName, src manual|gmail; Gmail entries use doc id `gm-<message id>`). Manual stage overrides in `bdstage/<branch id>` ({stage: 0-4 or null}). Stages: Not contacted, Reaching out, In conversation, Req received, Placed. Auto stage also uses tracker jobs/wins and open job sheet jobs.
