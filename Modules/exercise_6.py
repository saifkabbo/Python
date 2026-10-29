import exercise_3,exercise_4,exercise_5

def generate_colors(color,x):
    color=color.lower()
    if color=="hexa":
     return exercise_4.list_of_hexa_colors(x)
    elif color=="rgb":
      return exercise_5.list_of_rgb_colors(x)
    else:
      return "Invalid! Color."

print(generate_colors('Hexa', 3))


