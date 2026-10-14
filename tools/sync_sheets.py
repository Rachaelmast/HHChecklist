"""Fetch the public Redzone and job sheets as CSV and write the dashboard's sync/latest document.

Usage: python3 -I tools/sync_sheets.py OUT.json
Then write OUT.json to the published dashboard's shared data, collection "sync", doc "latest".
"""
import json, sys, time, urllib.parse, urllib.request

PEND_ID = '18jRALHAXGl1aRHakl40pxn9ybdzEsyKnYvJX2mnWuCo'
JOB_ID = '1wUAUuAPpE18ikWuuZgbQJHLhMgKHkbRh3jgn17BXgYw'
JOB_TABS = ['Home Health RN', 'Hospice RN', 'Home Health LPN']


def csv(sheet_id, tab=None):
    url = 'https://docs.google.com/spreadsheets/d/%s/gviz/tq?tqx=out:csv' % sheet_id
    if tab:
        url += '&sheet=' + urllib.parse.quote(tab)
    with urllib.request.urlopen(url, timeout=60) as r:
        text = r.read().decode('utf-8')
    if not text.startswith('"'):
        raise SystemExit('Unexpected response for %s %s' % (sheet_id, tab or ''))
    return text


doc = {'pending': csv(PEND_ID), 'at': int(time.time() * 1000)}
for i, tab in enumerate(JOB_TABS):
    doc['jobs%d' % i] = csv(JOB_ID, tab)
json.dump(doc, open(sys.argv[1], 'w'))
print('ok', {k: len(v) if isinstance(v, str) else v for k, v in doc.items()})
