def appearance(intervals: dict[str, list[int]]) -> int:

    pupil_intervals = intervals['pupil']
    tutor_intervals = intervals['tutor']

    def merge_intervals(interval_list):
        pairs = sorted((interval_list[i], interval_list[i + 1])
                       for i in range(0, len(interval_list), 2))
        merged = []
        for start, end in pairs:
            if merged and start <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                merged.append((start, end))
        return merged

    def intersect_with_lesson(merged):
        lesson_start, lesson_end = intervals['lesson']
        return [(max(start, lesson_start), min(end, lesson_end))
                for start, end in merged
                if max(start, lesson_start) < min(end, lesson_end)]

    pupil_merged = merge_intervals(pupil_intervals)
    tutor_merged = merge_intervals(tutor_intervals)

    pupil_in_lesson = intersect_with_lesson(pupil_merged)
    tutor_in_lesson = intersect_with_lesson(tutor_merged)

    total_time = i = j = 0
    while i < len(pupil_in_lesson) and j < len(tutor_in_lesson):
        start = max(pupil_in_lesson[i][0], tutor_in_lesson[j][0])
        end = min(pupil_in_lesson[i][1], tutor_in_lesson[j][1])

        if start < end:
            total_time += end - start

        if pupil_in_lesson[i][1] < tutor_in_lesson[j][1]:
            i += 1
        else:
            j += 1
    return total_time