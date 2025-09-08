# Write your solution here
import urllib.request, json

def retrieve_all() -> list[tuple]:
    active_courses = []
    url_request = urllib.request.urlopen('https://studies.cs.helsinki.fi/stats-mock/api/courses').read()
    responses = json.loads(url_request)
    # fullName, name, year, sum(exercises)
    for response in responses:
        if response['enabled']:
            exercises = [int(ex) for ex in response['exercises']]
            active_courses.append((response['fullName'], response['name'], response['year'], sum(exercises)))
    
    return active_courses

def retrieve_course(course_name: str) -> dict:
    course_stats = {}
    url_string = f'https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats'
    request = urllib.request.urlopen(url_string).read()
    content = json.loads(request)
    course_stats['weeks'] = len(content)

    for week in content.values():
        if not 'students' in course_stats:
            course_stats['students'] = week['students']
        else:
            if week['students'] > course_stats['students']:
                course_stats['students'] = week['students']
            
        if not 'hours' in course_stats:
            course_stats['hours'] = week['hour_total']
        else:
            course_stats['hours'] += week['hour_total']

        if not 'exercises' in course_stats:
            course_stats['exercises'] = week['exercise_total']
        else:
            course_stats['exercises'] += week['exercise_total']
        
        
    course_stats['hours_average'] = course_stats['hours'] // course_stats['students']
    course_stats['exercises_average'] = course_stats['exercises'] // course_stats['students']

    return course_stats



if __name__ == '__main__':
    print(retrieve_course('docker2019'))