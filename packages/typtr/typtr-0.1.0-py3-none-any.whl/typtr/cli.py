import sys

SUPPORTED_LANGUAGES = ['java', 'js']


def main():
    i = -1
    langtype = None
    for i, arg in enumerate(sys.argv):
        if arg in ('-t', '--type'):
            flag = sys.argv.pop(i)
            langtype = sys.argv.pop(i)
            sys.argv[0] += f' {flag} {langtype}'
            break

    if langtype == 'java':
        from . import java

        java.JavaTranspiler().main()

    elif langtype == 'js':
        from . import js

        js.JsTranspiler().main()

    else:
        import os.path

        cmd = os.path.basename(sys.argv[0])
        lang_alts = '{' + '|'.join(SUPPORTED_LANGUAGES) + '}'
        print(f"Usage: {cmd} -t {lang_alts}", file=sys.stderr)
        exit()


if __name__ == '__main__':
    main()
