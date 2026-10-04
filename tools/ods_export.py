#!/usr/bin/env python3
"""ODS export - every row of every store in ONE worksheet, for reading in LibreOffice.

  python3 tools/ods_export.py [output]        default: build/abyss_boat_script.ods

Columns: Store, Unit, ID, Context, Japanese (the dump, tags as written), English (the
target from tl/, empty until translated).  Rows in dump order: script, scene, system.
Read-only with respect to dumps/ and tl/; never reads pending/; CHECK does not use it.
Standard library only: an ODS file is a zip of XML parts.
"""
import os
import re
import sys
import zipfile
from xml.sax.saxutils import escape

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from abyss.project import STORES, ROOT, path, units, translations    # noqa: E402

SHEET = 'Abyss Boat'
COLUMNS = [('Store', '1.8cm'), ('Unit', '5.2cm'), ('ID', '5.2cm'), ('Context', '3.4cm'),
           ('Japanese', '12cm'), ('English', '12cm')]
NS = ('xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" '
      'xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" '
      'xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" '
      'xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" '
      'xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" '
      'xmlns:config="urn:oasis:names:tc:opendocument:xmlns:config:1.0" '
      'xmlns:manifest="urn:oasis:names:tc:opendocument:xmlns:manifest:1.0" '
      'office:version="1.2"')


def rows_in_order():
    tl = translations()
    out = []
    for store in STORES:
        for unit, rows in units(store).items():
            for r in rows:
                out.append((r.line, store, unit, r.id, r.ctx, r.src, tl.get((store, r.id), '')))
    # dump order within each store (units() groups system rows by unit, not by dump line)
    order = {s: k for k, s in enumerate(STORES)}
    out.sort(key=lambda x: (order[x[1]], x[0]))
    return [x[1:] for x in out]


def ods_text(value):
    """Escape for <text:p>; runs of spaces become <text:s/> so readers keep them."""
    parts = re.split(r'( {2,}|^ | $)', value)
    return ''.join('<text:s text:c="%d"/>' % len(p) if k % 2 else escape(p)
                   for k, p in enumerate(parts))


def cell(value, style):
    return ('<table:table-cell table:style-name="%s" office:value-type="string">'
            '<text:p>%s</text:p></table:table-cell>' % (style, ods_text(value)))


def content_xml(rows):
    parts = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<office:document-content %s>' % NS,
             '<office:automatic-styles>']
    for k, (_, width) in enumerate(COLUMNS):
        parts.append('<style:style style:name="co%d" style:family="table-column">'
                     '<style:table-column-properties style:column-width="%s"/></style:style>'
                     % (k, width))
    parts += ['<style:style style:name="hd" style:family="table-cell">'
              '<style:table-cell-properties style:vertical-align="top"/>'
              '<style:text-properties fo:font-weight="bold"/></style:style>',
              '<style:style style:name="tx" style:family="table-cell">'
              '<style:table-cell-properties fo:wrap-option="wrap" style:vertical-align="top"/>'
              '</style:style>',
              '</office:automatic-styles>',
              '<office:body><office:spreadsheet>',
              '<table:table table:name="%s">' % escape(SHEET)]
    for k in range(len(COLUMNS)):
        parts.append('<table:table-column table:style-name="co%d"/>' % k)
    parts.append('<table:table-row>' + ''.join(cell(n, 'hd') for n, _ in COLUMNS)
                 + '</table:table-row>')
    for r in rows:
        parts.append('<table:table-row>' + ''.join(cell(v, 'tx') for v in r) + '</table:table-row>')
    last = chr(ord('A') + len(COLUMNS) - 1)
    parts += ['</table:table>',
              '<table:database-ranges><table:database-range table:name="__Anonymous_Sheet_DB__0" '
              'table:target-range-address="\'%s\'.A1:\'%s\'.%s%d" '
              'table:display-filter-buttons="true"/></table:database-ranges>'
              % (escape(SHEET), escape(SHEET), last, len(rows) + 1),
              '</office:spreadsheet></office:body></office:document-content>']
    return '\n'.join(parts)


def settings_xml():
    # freeze the header row
    return ('<?xml version="1.0" encoding="UTF-8"?>'
            '<office:document-settings %s><office:settings>'
            '<config:config-item-set config:name="ooo:view-settings">'
            '<config:config-item-map-indexed config:name="Views"><config:config-item-map-entry>'
            '<config:config-item-map-named config:name="Tables">'
            '<config:config-item-map-entry config:name="%s">'
            '<config:config-item config:name="VerticalSplitMode" config:type="short">2</config:config-item>'
            '<config:config-item config:name="VerticalSplitPosition" config:type="int">1</config:config-item>'
            '<config:config-item config:name="ActiveSplitRange" config:type="short">2</config:config-item>'
            '<config:config-item config:name="PositionBottom" config:type="int">1</config:config-item>'
            '</config:config-item-map-entry></config:config-item-map-named>'
            '</config:config-item-map-entry></config:config-item-map-indexed>'
            '</config:config-item-set></office:settings></office:document-settings>'
            % (NS, escape(SHEET)))


MANIFEST = ('<?xml version="1.0" encoding="UTF-8"?>'
            '<manifest:manifest xmlns:manifest="urn:oasis:names:tc:opendocument:xmlns:manifest:1.0" '
            'manifest:version="1.2">'
            '<manifest:file-entry manifest:full-path="/" manifest:version="1.2" '
            'manifest:media-type="application/vnd.oasis.opendocument.spreadsheet"/>'
            '<manifest:file-entry manifest:full-path="content.xml" manifest:media-type="text/xml"/>'
            '<manifest:file-entry manifest:full-path="settings.xml" manifest:media-type="text/xml"/>'
            '</manifest:manifest>')


def main(argv):
    out = argv[0] if argv else path('build', 'abyss_boat_script.ods')
    rows = rows_in_order()
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with zipfile.ZipFile(out, 'w') as z:
        # the mimetype entry must come first and be stored uncompressed
        z.writestr(zipfile.ZipInfo('mimetype'), 'application/vnd.oasis.opendocument.spreadsheet',
                   compress_type=zipfile.ZIP_STORED)
        z.writestr('META-INF/manifest.xml', MANIFEST, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr('content.xml', content_xml(rows), compress_type=zipfile.ZIP_DEFLATED)
        z.writestr('settings.xml', settings_xml(), compress_type=zipfile.ZIP_DEFLATED)
    done = sum(1 for r in rows if r[5].strip())
    print('wrote %s: %d rows (%s), %d translated'
          % (os.path.relpath(out, ROOT), len(rows),
             ', '.join('%s %d' % (s, sum(1 for r in rows if r[0] == s)) for s in STORES), done))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
