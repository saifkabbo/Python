import exercise_3

def list_of_rgb_colors(x):
    rgb_array=[]
    for _ in range(x):
     rgb_array.append(exercise_3.rgb_color_gen())
    return rgb_array 


