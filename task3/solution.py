def checks_interval_data(key_intervals: list, key: str, lesson_interval: list) -> None:
    """check values of intervals"""
    if len(key_intervals) % 2 != 0:
        raise ValueError(f"{key} intervals: invalid data")

    if not len(lesson_interval) == 2:
        raise ValueError(f"lesson interval: invalid data")


def add_or_merge_interval(intervals: list[tuple[int, int]], start: int, end: int) -> None:
    """add new interval or merge last interval with new, if its intersect"""

    if intervals and intervals[-1][0] < start <= intervals[-1][1]:
        intervals[-1] = (min(intervals[-1][0], start), max(intervals[-1][1], end))
    else:
        intervals.append((start, end))


def parse_intervals(intervals: dict[str, list[int]], key: str) -> list[tuple[int, int]]:
    """parse intervals for list of tuples"""

    key_intervals = intervals[key]
    lesson_interval = intervals['lesson']

    # checks of values
    checks_interval_data(key_intervals, key, lesson_interval)

    lesson_start = lesson_interval[0]
    lesson_end = lesson_interval[1]
    parsed_intervals = []
    # could be situation, that lesson_start > entrance of pupil/tutor, lesson_end < exit of pupil/tutor
    for n in range(0, len(key_intervals), 2):
        start = max(lesson_start, key_intervals[n])
        end = min(lesson_end, key_intervals[n + 1])
        if start <= end:
            add_or_merge_interval(parsed_intervals, start, end)

    return parsed_intervals


def appearance(intervals: dict[str, list[int]]) -> int:
    """calculate common time of lesson for both - pupil and tutor"""

    pupil_intervals = parse_intervals(intervals, 'pupil')
    tutor_intervals = parse_intervals(intervals, 'tutor')

    common_time = 0
    i, j = 0, 0

    while i < len(pupil_intervals) and j < len(tutor_intervals):
        start = max(pupil_intervals[i][0], tutor_intervals[j][0])
        end = min(pupil_intervals[i][1], tutor_intervals[j][1])
        if start <= end:
            common_time += end - start

        # move the smallest interval
        if pupil_intervals[i][1] < tutor_intervals[j][1]:
            i += 1
        else:
            j += 1

    return common_time


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                             1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                             1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                             1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
