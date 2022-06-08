def sort_of_wardrobe(wardrobe, count_items, count_colors):
    colors = [0]*count_colors
    for color_index in range(0, count_colors):
        colors[color_index] = wardrobe.count(str(color_index))
    sorted_wardrobe = ['']*count_items
    index = 0
    for value in range(count_colors):
        for amount in range(colors[value]):
            sorted_wardrobe[index] = str(value)
            index += 1
    return ' '.join(sorted_wardrobe)


if __name__ == "__main__":
    count_items = int(input())
    count_colors = 3
    wardrobe = input()
    print(sort_of_wardrobe(wardrobe, count_items, count_colors))