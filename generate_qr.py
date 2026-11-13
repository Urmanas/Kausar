
import qrcode


def generate_qr(url):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=12,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color="#34462D",
        back_color="white",
    )

    image.save("kausar_qr.png")

    print("QR code created: kausar_qr.png")


if __name__ == "__main__":
    website_url = input(
        "Enter KAUSAR website URL: "
    ).strip()

    if not website_url.startswith(
        ("https://", "http://")
    ):
        raise ValueError(
            "Enter a full http:// or https:// URL"
        )

    generate_qr(website_url)
