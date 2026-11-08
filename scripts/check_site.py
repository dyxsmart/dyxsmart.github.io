"""Check local page references without third-party dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.links = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        for name in ('href', 'src', 'poster'):
            if attrs.get(name):
                self.links.append(attrs[name])


pages = {p: Page(p.read_text()) for p in ROOT.glob('*.html')}
errors = []
for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if not target.is_file():
            errors.append(f'{path.name}: missing file {link}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f'{path.name}: missing anchor {link}')
    if 'undefined' in path.read_text():
        errors.append(f'{path.name}: unresolved placeholder')
for folder in ('assets',):
    for path in (ROOT / folder).rglob('*'):
        if path.is_file() and path.stat().st_size >= 100 * 1024**2:
            errors.append(f'{path.relative_to(ROOT)}: exceeds 100 MiB')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'Checked {len(pages)} HTML pages: local files, anchors, placeholders and asset sizes OK.')
