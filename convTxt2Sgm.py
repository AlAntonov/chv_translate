import os
import argparse
import io

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-src', required=True, type=str)
    parser.add_argument('-ref', required=True, type=str)
    parser.add_argument('-tst', required=True, type=str)

    args = parser.parse_args()

    path2src = args.src
    path2ref = args.ref
    path2tst = args.tst

    lstSrc = []
    with io.open(path2src, encoding='utf8') as fread:
        for line in fread:
            lstSrc.append(line)

    lstRef = []
    with io.open(path2ref, encoding='utf8') as fread:
        for line in fread:
            lstRef.append(line)
			
    lstTst = []
    with io.open(path2tst, encoding='utf8') as fread:
        for line in fread:
            lstTst.append(line)

    with io.open(path2src + '.sgm', 'w', encoding='utf8') as fwrite:
        fwrite.write(u'<srcset setid="ruchv_150K_skv_dev19" srclang="ru">\n')
        fwrite.write(u'<doc docid="demo1" genre="news" origlang="ru">\n')
        fwrite.write(u'<p>\n')
        for i, line in enumerate(lstSrc):
            _str = u'<seg id="'
            _str += str(i+1)
            _str += u'"> '
            _str += line.strip()
            _str += u'</seg>\n'
            fwrite.write(_str)
        fwrite.write(u'</p>\n')
        fwrite.write(u'</doc>\n')
        fwrite.write(u'</srcset>')
        fwrite.flush()

    with io.open(path2ref + '.sgm', 'w', encoding='utf8') as fwrite:
        fwrite.write(u'<refset setid="ruchv_150K_skv_dev19" srclang="ru" trglang="chv">\n')
        fwrite.write(u'<doc docid="demo1" genre="news" origlang="ru" sysid="ref">\n')
        fwrite.write(u'<p>\n')
        for i, line in enumerate(lstRef):
            _str = u'<seg id="'
            _str += str(i+1)
            _str += u'"> '
            _str += line.strip()
            _str += u'</seg>\n'
            fwrite.write(_str)
        fwrite.write(u'</p>\n')
        fwrite.write(u'</doc>\n')
        fwrite.write(u'</refset>')
        fwrite.flush()
		
    with io.open(path2tst + '.sgm', 'w', encoding='utf8') as fwrite:
        fwrite.write(u'<tstset setid="ruchv_150K_skv_dev19" srclang="ru" trglang="chv">\n')
        fwrite.write(u'<doc docid="demo1" genre="news" origlang="ru" sysid="ref">\n')
        fwrite.write(u'<p>\n')
        for i, line in enumerate(lstTst):
            _str = u'<seg id="'
            _str += str(i+1)
            _str += u'"> '
            _str += line.strip()
            _str += u'</seg>\n'
            fwrite.write(_str)
        fwrite.write(u'</p>\n')
        fwrite.write(u'</doc>\n')
        fwrite.write(u'</tstset>')
        fwrite.flush()

if __name__ == '__main__':
    main()