def appearance(intervals):
    seconds_together = 0
    counter = 0
    m = 0

    lst = [[intervals['lesson'][ind], 1 - 2 * (ind % 2)] for ind in range(len(intervals['lesson']))]
    lst += [[intervals['pupil'][ind], 1 - 2 * (ind % 2)] for ind in range(len(intervals['pupil']))]
    lst += [[intervals['tutor'][ind], 1 - 2 * (ind % 2)] for ind in range(len(intervals['tutor']))]
    lst.sort()

    for elem in lst:
        counter += elem[1]
        if counter == 3:
            m = elem[0]
        if m != 0 and counter == 2:
            seconds_together += elem[0] - m
            m = 0

    print(seconds_together)


if __name__ == '__main__':
    appearance({
        'lesson': [1594663200, 1594666800],
        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
        'tutor': [1594663290, 1594663430, 1594663443, 1594666473],
    })
