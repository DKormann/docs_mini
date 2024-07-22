#%%
from werkzeug.datastructures.file_storage import FileStorage
import pymupdf

def ocr_file(file: FileStorage):
  print('Document received!', type(file))


  return "<document content>"

