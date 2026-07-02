import os

import fitz

from schemas.image_data import ImageData


class ImageProcessor:

    OUTPUT_DIR = "images/extracted"

    @staticmethod
    def extract(pdf_path: str):

        os.makedirs(
            ImageProcessor.OUTPUT_DIR,
            exist_ok=True,
        )

        document = fitz.open(pdf_path)

        images = []

        for page_index in range(len(document)):

            page = document.load_page(page_index)

            image_list = page.get_images(
                full=True
            )

            for image_number, image in enumerate(
                image_list,
                start=1,
            ):

                xref = image[0]

                pix = fitz.Pixmap(
                    document,
                    xref,
                )

                if pix.n < 5:

                    filename = (
                        f"{os.path.basename(pdf_path)}"
                        f"_page{page_index+1}"
                        f"_img{image_number}.png"
                    )

                    path = os.path.join(
                        ImageProcessor.OUTPUT_DIR,
                        filename,
                    )

                    pix.save(path)

                else:

                    pix = fitz.Pixmap(
                        fitz.csRGB,
                        pix,
                    )

                    filename = (
                        f"{os.path.basename(pdf_path)}"
                        f"_page{page_index+1}"
                        f"_img{image_number}.png"
                    )

                    path = os.path.join(
                        ImageProcessor.OUTPUT_DIR,
                        filename,
                    )

                    pix.save(path)

                pix = None

                images.append(

                    ImageData(

                        document_name=os.path.basename(
                            pdf_path
                        ),

                        page_number=page_index + 1,

                        image_number=image_number,

                        image_path=path,
                    )

                )

        return images