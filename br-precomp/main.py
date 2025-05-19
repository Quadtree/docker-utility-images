import brotli
import os
import pathlib

ALLOWED_PATHS = [
    '.js',
    '.wasm',
    '.pck',
    '.data',
]

OUT_DIR = os.getenv('BR_PRECOMP_DST', '/data/_autobr')

def compress_all_in(d, root=None):
    if root is None: root = d
    for fn in os.scandir(d):
        if os.path.isdir(fn):
            compress_all_in(fn, root)
        else:
            rel_to_root = pathlib.PurePath(fn).relative_to(root)
            ofn = os.path.join(OUT_DIR, rel_to_root) + '.br'
            #print(f'{rel_to_root=} {os.path.abspath(fn)=} {ofn=} {os.path.basename(fn)}')

            if len([1 for it in ALLOWED_PATHS if os.path.basename(fn).endswith(it)]) > 0:

                with open(fn, 'rb') as f_in:
                    uncompressed_bytes = f_in.read()
                    need_to_recompress = True

                    if os.path.exists(ofn):
                        with open(ofn, 'rb') as f_out:
                            try:
                                compressed_bytes_uncompressed = brotli.decompress(f_out.read())
                            except Exception as ex:
                                print(f'Decompression error: {ex}')
                                compressed_bytes_uncompressed = None

                        if compressed_bytes_uncompressed == uncompressed_bytes:
                            need_to_recompress = False

                    if need_to_recompress:
                        os.makedirs(os.path.dirname(ofn), exist_ok=True)
                        with open(ofn, 'wb') as f_out:
                            print(f'Compressing {os.path.abspath(fn)} to {os.path.abspath(ofn)}', flush=True)
                            f_out.write(brotli.compress(uncompressed_bytes))
                    else:
                        print(f'NOT Compressing {os.path.abspath(fn)} to {os.path.abspath(ofn)}', flush=True)

                    print(f'Original Size: {os.stat(fn).st_size / 1024 / 1024:.06f}MiB {os.stat(ofn).st_size / 1024 / 1024:.06f}MiB')


compress_all_in(os.getenv('BR_PRECOMP_TRG', '/data'))
