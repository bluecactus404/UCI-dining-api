import requests

def get_robots_txt(base_url:str)->str:
    request = requests.get(base_url + '/robots.txt')
    return request.text

def get_rules(robots_txt:str, user_agent:str)->list[str]:
    rules = []
    agents = []
    previous_line = ''
    robots_txt_as_array = robots_txt.split('\n')

    for line in robots_txt_as_array:
        line = line.strip()
        #sanitize line from comments
        index = None
        try:
            index = line.index('#')
        except:
            pass
        else:
            if index != None:
                line = line[:index]
        
        if 'User-agent:' in line:
            if 'User-agent:' not in previous_line:
                agents = []
            agents.append(line[len('User-agent: '):])

        elif user_agent in agents and len(line) != 0 and 'Sitemap: ' not in line:
            rules.append(line)
        previous_line = line
    return rules

def is_url_ok_to_scrape(url:str, rules:list[str]) -> bool:

    return False

