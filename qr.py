import qrcode
import io
import base64

def make_qr(data = ':)', colour="black", bg_colour="white"):
    my_qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    my_qr.add_data(data)
    my_qr.make(fit=True)
    qr_img = my_qr.make_image(
        fill_color = colour,
        back_color = bg_colour,
    )
    byte_storage = io.BytesIO()
    qr_img.save(byte_storage)

    qr_bytes = byte_storage.getvalue()
    display_bytes = base64.b64encode(qr_bytes).decode('utf-8')
    return display_bytes