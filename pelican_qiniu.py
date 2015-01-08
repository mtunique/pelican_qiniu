__author__ = 'mtunique'
from os import path, access, R_OK

from pelican import signals

from bs4 import BeautifulSoup
from sevencow import Cow

import logging
logger = logging.getLogger(__name__)

BUCKET = None


def content_object_init(instance):
    global BUCKET
    if instance._content is not None:
        content = instance._content
        soup = BeautifulSoup(content)

        if 'img' in content:
            for img in soup('img'):
                img_path, img_filename = path.split(img['src'])
                # Strip off {filename}, |filename| or /static
                if img_path.startswith(('{filename}', '|filename|')):
                    img_path = img_path[10:]
                elif img_path.startswith('/static'):
                    img_path = img_path[7:]
                else:
                    continue

                try:
                    # Build the source image filename
                    src = instance.settings['PATH'] + img_path + '/' + img_filename

                    if not (path.isfile(src) and access(src, R_OK)):
                        logger.warning('pelican-qiniu. Error: image not found: {}'.format(src))
                    BUCKET.put(src)
                    img['src'] = '{}{}'.format(instance.settings['QINIU_PRE'], img_filename)
                except:
                    import traceback
                    logger.error(traceback.format_exc())

        instance._content = soup.decode()


def init(sender):
    global BUCKET
    cow = Cow(sender.settings['QINIU_AK'].encode('utf-8'), sender.settings['QINIU_SK'].encode('utf-8'),)
    BUCKET = cow.get_bucket(sender.settings['QINIU_BUCKET'])


def register():
    signals.content_object_init.connect(content_object_init)
    signals.initialized.connect(init)