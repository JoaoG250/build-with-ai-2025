from google.cloud import vision


def get_image_tags(image_path: str) -> list[str]:
    client = vision.ImageAnnotatorClient()

    with open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    tags = []
    for label in labels:
        tags.append(label.description)

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: https://cloud.google.com/apis/design/errors".format(
                response.error.message
            )
        )

    return tags
