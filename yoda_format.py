#!/usr/bin/env python
# coding:utf-8

import yoda
from yoda.formats.com import ComParser, ComWriter
from yoda.formats.formats_Center import Format

f1 = '1.mol'
s1 = Format(f1).parse()
header = "%men = 10GB"
write = ComWriter(s1)
print(write.write(header = header))
