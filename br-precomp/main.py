import brotli
import os

ALLOWED_PATHS = [
    '.js',
    '.wasm',
    '.pck'
]

def compress_all_in(d):
    for fn in os.scandir(d):
        if os.path.isdir(fn):
            compress_all_in(fn)
        else:
            ofn = os.path.abspath(fn) + '._autobr'
            print(f'{os.path.abspath(fn)=} {ofn=} {os.path.basename(fn)}')

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
                        with open(ofn, 'wb') as f_out:
                            print(f'Compressing {os.path.abspath(fn)} to {os.path.abspath(ofn)}')
                            f_out.write(brotli.compress(uncompressed_bytes))
                    else:
                        print(f'NOT Compressing {os.path.abspath(fn)} to {os.path.abspath(ofn)}')


compress_all_in(os.getenv('BR_PRECOMP_TRG'))
