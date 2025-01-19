import copy

def spread_fire(grid):
    """
    Update the forest grid based on fire spreading rules.
    """
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)  # יצירת עותק של הגריד

    for i in range(grid_size):  # מעבר על כל שורות הגריד
        for j in range(grid_size):  # מעבר על כל עמודות הגריד
            if grid[i][j] == 1:  # אם התא הוא עץ
                neighbors = []

                # בדיקת שכנים בצורה בטוחה (רק אם הם בגבולות הגריד)
                if i > 0:  # שכנים מעל
                    neighbors.append(grid[i-1][j])
                if i < grid_size - 1:  # שכנים מתחת
                    neighbors.append(grid[i+1][j])
                if j > 0:  # שכנים משמאל
                    neighbors.append(grid[i][j-1])
                if j < grid_size - 1:  # שכנים מימין
                    neighbors.append(grid[i][j+1])

                # אם אחד מהשכנים בוער, העץ הנוכחי נדלק
                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid  # החזרת הגריד המעודכן
