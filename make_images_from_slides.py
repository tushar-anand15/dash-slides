from pdf2image import convert_from_path

def make_images_from_slides():
    pages = convert_from_path('../sl_ecourts.pdf')
    for count, page in enumerate(pages):
        page.save(f'assets/out{count}.jpg', 'JPEG')
    print('saved files')
    return None