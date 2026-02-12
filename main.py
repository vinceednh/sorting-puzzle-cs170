

# This makes the size of the board so it can be run with multiple different sizes
def make_goal(size):
    goal = []
    value = 1

    for i in range(size):
        row = []
        for j in range(size):
            row.append(value)
            value += 1
        goal.append(row)

    goal[size - 1][size - 1] = 0
    return goal

def main():

if __name__ == "__main__":
    main()