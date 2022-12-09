from pathlib import Path

puzzle_input = Path('inputs/8').read_text()

trees = puzzle_input.splitlines()


def is_visible(trees_row, tree_index):
    tree_height = int(trees_row[tree_index])
    higher_trees_from_left_side = [tree for tree in trees_row[:tree_index] if int(tree) >= tree_height]
    higher_trees_from_right_side = [tree for tree in trees_row[tree_index + 1:] if int(tree) >= tree_height]
    if higher_trees_from_left_side and higher_trees_from_right_side:
        return False
    return True


def calculate_scenic_score(trees_row, tree_index):
    tree_height = int(trees_row[tree_index])
    trees_on_the_left_side = reversed(trees_row[:tree_index])
    trees_on_the_right_side = trees_row[tree_index + 1:]
    score_on_the_left_side = 0
    score_on_the_right_side = 0

    for tree in trees_on_the_left_side:
        if int(tree) >= tree_height:
            score_on_the_left_side += 1
            break
        score_on_the_left_side += 1
    for tree in trees_on_the_right_side:
        if int(tree) >= tree_height:
            score_on_the_right_side += 1
            break
        score_on_the_right_side += 1
    return score_on_the_left_side * score_on_the_right_side


def get_trees_column(column_index):
    return [tree_row[column_index] for tree_row in trees]


# 8.1
visible_trees_count = 4 * len(trees[0]) - 4
for tree_row_index in range(1, len(trees) - 1):
    for tree_index in range(1, len(trees[tree_row_index]) - 1):
        trees_column = get_trees_column(tree_index)
        if is_visible(trees[tree_row_index], tree_index) or is_visible(trees_column, tree_row_index):
            visible_trees_count += 1
print(visible_trees_count)

# 8.2
scenic_scores = []
for tree_row_index in range(len(trees)):
    for tree_index in range(len(trees[tree_row_index])):

        trees_column = get_trees_column(tree_index)
        horizontal_scenic_score = calculate_scenic_score(trees[tree_row_index], tree_index)
        vertical_scenic_score = calculate_scenic_score(trees_column, tree_row_index)

        if tree_row_index == 3 and tree_index == 2:
            calculate_scenic_score(trees[tree_row_index], tree_index)

        scenic_scores.append(horizontal_scenic_score * vertical_scenic_score)
print(max(scenic_scores))