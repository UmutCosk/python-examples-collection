import cv2


def ColoredContour(bgr, gray_image, line_thickness):
    b, g, r = bgr

    _, threshold = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        counter_image = cv2.drawContours(
            gray_image, [contour], 0, 0, line_thickness)
    # Create a mask of contours and create its inverse mask also
    _, mask = cv2.threshold(counter_image, 10, 255, cv2.THRESH_BINARY)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    mask_inv = cv2.bitwise_not(mask)
    mask_inv[:, :, 0] = b
    mask_inv[:, :, 1] = g
    mask_inv[:, :, 2] = r
    new_mask = cv2.bitwise_or(mask_inv, mask)
    return new_mask
