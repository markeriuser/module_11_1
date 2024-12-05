from PIL import Image, ImageFilter

# Открытие изображения
image = Image.open('example.png')

# Изменение размера изображения
resized_image = image.resize((200, 200))
resized_image.save('resized_image.png')

# Применение размытия
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save('blurred_image.png')

# Показать изображение
image.show()
