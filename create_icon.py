from PIL import Image, ImageDraw, ImageFont
import os

# Create a simple icon for the application
img = Image.new('RGB', (256, 256), color='#2C3E50')
draw = ImageDraw.Draw(img)

# Draw microphone symbol
# Microphone body
draw.rounded_rectangle([100, 60, 156, 160], radius=28, fill='#3498DB')
# Microphone base
draw.rectangle([120, 160, 136, 180], fill='#3498DB')
draw.rectangle([100, 180, 156, 190], fill='#3498DB')

# Draw document symbol
# Document body
draw.rectangle([170, 100, 220, 180], fill='#ECF0F1')
# Document corner fold
draw.polygon([(220, 100), (200, 100), (220, 120)], fill='#BDC3C7')
# Document lines
for y in range(115, 165, 15):
    draw.rectangle([180, y, 210, y+3], fill='#7F8C8D')

# Draw arrow from mic to doc
draw.polygon([(160, 120), (165, 115), (165, 118), (170, 118), 
              (170, 122), (165, 122), (165, 125)], fill='#E74C3C')

# Save icon
img.save('icon.png')
print("Icon created successfully!")

# Also create an ICO file for Windows
img.save('icon.ico', format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])