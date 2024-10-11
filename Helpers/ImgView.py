import matplotlib.pyplot as plt

def display_images(original, lbp_image, cls:{"ok","defective"}):
    plt.figure(figsize=(10, 5))

    # Original image
    plt.subplot(1, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.title(f"Original {cls} Image")
    plt.axis('off')

    # LBP image
    plt.subplot(1, 2, 2)
    plt.imshow(lbp_image, cmap='gray')
    plt.title(f"HOG {cls} Image")
    plt.axis('off')

    plt.show()