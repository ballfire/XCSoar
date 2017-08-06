from build.zlib import ZlibProject
from build.autotools import AutotoolsProject
from build.freetype import FreeTypeProject

zlib = ZlibProject(
    'http://zlib.net/zlib-1.2.11.tar.xz',
    'http://downloads.sourceforge.net/project/libpng/zlib/1.2.11/zlib-1.2.11.tar.xz',
    '4ff941449631ace0d4d203e3483be9dbc9da454084111f97ea0a2114e19bf066',
    'lib/libz.a',
)

freetype = FreeTypeProject(
    'http://download.savannah.gnu.org/releases/freetype/freetype-2.8.tar.bz2',
    'http://downloads.sourceforge.net/project/freetype/freetype2/2.8/freetype-2.8.tar.bz2',
    'a3c603ed84c3c2495f9c9331fe6bba3bb0ee65e06ec331e0a0fb52158291b40b',
    'lib/libfreetype.a',
    [
        '--disable-shared', '--enable-static',
        '--without-bzip2', '--without-png',
        '--without-harfbuzz',
    ],
)

curl = AutotoolsProject(
    'http://curl.haxx.se/download/curl-7.54.1.tar.gz',
    'http://github.com/curl/curl/files/1101227/curl-7.54.1.tar.gz',
    'cd404b808b253512dafec4fed0fb2cc98370d818a7991826c3021984fc27f9d0',
    'lib/libcurl.a',
    [
        '--disable-shared', '--enable-static',
        '--disable-debug',
        '--enable-http',
        '--enable-ipv6',
        '--disable-ftp', '--disable-file',
        '--disable-ldap', '--disable-ldaps',
        '--disable-rtsp', '--disable-proxy', '--disable-dict', '--disable-telnet',
        '--disable-tftp', '--disable-pop3', '--disable-imap', '--disable-smb',
        '--disable-smtp',
        '--disable-gopher',
        '--disable-manual',
        '--disable-threaded-resolver', '--disable-verbose', '--disable-sspi',
        '--disable-crypto-auth', '--disable-ntlm-wb', '--disable-tls-srp', '--disable-cookies',
        '--without-ssl', '--without-gnutls', '--without-nss', '--without-libssh2',
    ],
    use_clang=True,
)

libpng = AutotoolsProject(
    'ftp://ftp.simplesystems.org/pub/libpng/png/src/libpng16/libpng-1.6.31.tar.xz',
    'http://downloads.sourceforge.net/project/libpng/libpng16/1.6.31/libpng-1.6.31.tar.xz',
    '232a602de04916b2b5ce6f901829caf419519e6a16cc9cd7c1c91187d3ee8b41',
    'lib/libpng.a',
    [
        '--disable-shared', '--enable-static',
        '--enable-arm-neon',
    ]
)

libjpeg = AutotoolsProject(
    'http://downloads.sourceforge.net/project/libjpeg-turbo/1.5.2/libjpeg-turbo-1.5.2.tar.gz',
    'http://sourceforge.mirrorservice.org/l/li/libjpeg-turbo/1.5.2/libjpeg-turbo-1.5.2.tar.gz',
    '9098943b270388727ae61de82adec73cf9f0dbb240b3bc8b172595ebf405b528',
    'lib/libjpeg.a',
    [
        '--disable-shared', '--enable-static',
        '--enable-arm-neon',
    ]
)
