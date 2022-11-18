import urllib.request
from bs4 import BeautifulSoup
import csv


def get_urls(track, date):
    url = "https://www.racenet.com.au/form-guide/horse-racing/" + track + "-" + date + "/all-races"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    req = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(req)
    page_html = response.read()
    response.close()

    html_soup = BeautifulSoup(page_html, 'html.parser')
    numbers = html_soup.find_all('a', class_='meeting-event-number')
    links = []
    for k in numbers:
        links.append("https://www.racenet.com.au" + k.attrs['href'])
    form_links = []
    for link in links:
        form_links.append(link.replace("overview", "full-form"))
    return form_links


def get_horses(race_url):
    url = race_url
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    req = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(req)
    page_html = response.read()
    response.close()

    html_soup = BeautifulSoup(page_html, 'html.parser')
    long_names = html_soup.find_all('div', class_='selection-details__name')
    names = []
    for long_name in long_names:
        names.append(str(long_name.find_all('strong')[0])[8:-9])
    return names


def get_horse_html(race_url):
    url = race_url
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    req = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(req)
    page_html = response.read()
    response.close()

    html_soup = BeautifulSoup(page_html, 'html.parser')
    horse_htmls = html_soup.find_all('div', class_='form-guide-full-form__selection')
    return horse_htmls


def get_name(h_html):
    name = h_html.find('div', class_='selection-details__name')
    if name is None:
        return
    return str(name.find_all('strong')[0])[8:-9]


def get_career(h_html):
    career = h_html.find('div', id="filter-career")
    if career is None:
        return
    return str(career.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_last_10(h_html):
    last10 = h_html.find('div', id="filter-last10")
    if last10 is None:
        return
    return str(last10.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_last_win(h_html):
    win = h_html.find('div', id="filter-lastWin")
    if win is None:
        return
    return str(win.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_wins(h_html):
    wins = h_html.find('div', id="filter-wins")
    if wins is None:
        return
    return str(wins.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_places(h_html):
    places = h_html.find('div', id="filter-places")
    if places is None:
        return
    return str(places.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_tj(h_html):
    tj = h_html.find('div', id="filter-tjWin")
    if tj is None:
        return
    return str(tj.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_jh(h_html):
    jh = h_html.find('div', id="filter-jockeyHorse")
    if jh is None:
        return
    return str(jh.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_twelveMonth(h_html):
    twelveMonth = h_html.find('div', id="filter-twelveMonth")
    if twelveMonth is None:
        return
    return str(twelveMonth.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_season(h_html):
    season = h_html.find('div', id="filter-season")
    if season is None:
        return
    return str(season.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_track(h_html):
    track = h_html.find('div', id="filter-track")
    if track is None:
        return
    return str(track.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_distance(h_html):
    distance = h_html.find('div', id="filter-distance")
    if distance is None:
        return
    return str(distance.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_trackDistance(h_html):
    trackDistance = h_html.find('div', id="filter-trackDistance")
    if trackDistance is None:
        return
    return str(trackDistance.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_firm(h_html):
    firm = h_html.find('div', id="filter-firm")
    if firm is None:
        return
    return str(firm.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_good(h_html):
    good = h_html.find('div', id="filter-good")
    if good is None:
        return
    return str(good.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_soft(h_html):
    soft = h_html.find('div', id="filter-soft")
    if soft is None:
        return
    return str(soft.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_heavy(h_html):
    heavy = h_html.find('div', id="filter-heavy")
    if heavy is None:
        return
    return str(heavy.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_wet(h_html):
    wet = h_html.find('div', id="filter-wet")
    if wet is None:
        return
    return str(wet.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_class(h_html):
    hclass = h_html.find('div', id="filter-class")
    if hclass is None:
        return
    return str(hclass.find('div', class_='form-grid-box__details'))[36:-6].strip()


def get_roi(h_html):
    roi = h_html.find('div', id="filter-roi")
    if roi is None:
        return
    return str(roi.find('div', class_='form-grid-box__details'))[36:-6].strip()


def calc_win_rate(races):
    win_rate = 0
    if races is None or races == '-':
        win_rate = 0.0
    else:
        tot_races = races.split(":")[0]
        podium = races.split(":")[1]
        first = podium.split("-")[0]
        second = podium.split("-")[1]
        third = podium.split("-")[2]
        win_rate = float(int(first) + int(second) + int(third)) / float(tot_races)
    return win_rate


def parse_percent(percent):
    if percent is None or percent == '' or percent == '-':
        return 0.0
    else:
        return float(percent[0:-1])/100


def parse_l10(l10):
    if l10 is None or l10 == '' or l10 == '-':
        return 0.0
    else:
        total = 0
        amount = 0
        for position in l10:
            if position in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                amount += 1
                total += int(position)
        if total == 0 or amount == 0:
            return 0.0
        return float(amount) / float(total)


def parse_last_win(lwin):
    if lwin is None or lwin == '' or lwin == '-':
        return 0.0
    else:
        if int(lwin[0:2].strip()) > 100:
            return 100/100
        else:
            return (100.0/int(lwin[0:2].strip())) / 100


def actual_winners(race_url):
    url = race_url
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    req = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(req)
    page_html = response.read()
    response.close()

    html_soup = BeautifulSoup(page_html, 'html.parser')
    names = []
    long_names = html_soup.find_all('div', class_='selection-result')
    for long_name in long_names:
        names.append(long_name.find_all("a", class_="")[0].text.replace('\n', '').strip())

    return names


def parse_horses(race_url):
    winners = actual_winners(race_url)
    horse_htmls = get_horse_html(race_url)
    horses_arr = []
    for horse in horse_htmls:

        data = []
        name = get_name(horse)
        career = calc_win_rate(get_career(horse))
        last10 = parse_l10(get_last_10(horse))
        lwin = parse_last_win(get_last_win(horse))
        wins = parse_percent(get_wins(horse))
        places = parse_percent(get_places(horse))
        tj = parse_percent(get_tj(horse))
        jh = calc_win_rate(get_jh(horse))
        twelveMonth = calc_win_rate(get_twelveMonth(horse))
        season = calc_win_rate(get_season(horse))
        track = calc_win_rate(get_track(horse))
        distance = calc_win_rate(get_distance(horse))
        trackDistance = calc_win_rate(get_trackDistance(horse))
        firm = calc_win_rate(get_firm(horse))
        good = calc_win_rate(get_good(horse))
        soft = calc_win_rate(get_soft(horse))
        heavy = calc_win_rate(get_heavy(horse))
        wet = calc_win_rate(get_wet(horse))
        hclass = calc_win_rate(get_class(horse))
        roi = parse_percent(get_roi(horse))

        if name in winners:
            is_winner = 1
        else:
            is_winner = 0

        data.append(str(name))
        data.append(str(career))
        data.append(str(last10))
        data.append(str(lwin))
        data.append(str(wins))
        data.append(str(places))
        data.append(str(tj))
        data.append(str(jh))
        data.append(str(twelveMonth))
        data.append(str(season))
        data.append(str(track))
        data.append(str(distance))
        data.append(str(trackDistance))
        data.append(str(firm))
        data.append(str(good))
        data.append(str(soft))
        data.append(str(heavy))
        data.append(str(wet))
        data.append(str(hclass))
        data.append(str(roi))
        data.append(str(is_winner))
        horses_arr.append(data)

    return horses_arr


def get_winner(hrace):
    horse_and_scores = []
    scores = []
    for horse in hrace:
        score = 0
        for stat in horse:
            if isinstance(stat, float):
                score += float(stat)
        scores.append(score)
        horse_and_scores.append([horse[0], score])
    scores.sort(reverse=True)
    order = []
    for score in scores:
        for pair in horse_and_scores:
            if pair[1] == score:
                order.append(pair)
    return order



if __name__ == '__main__':

    with open('horse_data.csv', 'w', newline='') as file:
        track = "ascot"
        dates = ["20221112", "20221109", "20221105", "20221103", "20221101", "20221029", "20221026", "20221022", "20221019", "20221015", "20221012", "20221008", "20220507", "20220504", "20220430", "20220425", "20220423", "20220420", "20220416", "20220415", "20220409", "20220406", "20220402", "20220331", "20220326", "20220323", "20220319", "20220316", "20220313", "20220312", "20220309", "20220305", "20220302", "20220226", "20220223", "20220219", "20220212", "20220129", "20220124", "20220115", "20220108", "20220101"]

        writer = csv.writer(file)
        writer.writerow(
            ["name", "career", "last10", "lwin", "wins", "places", "tj", "jh", "twelveMonth", "season", "track",
             "distance", "trackDistance", "firm", "good", "soft", "heavy", "wet", "hclass", "roi", "is_winner"])

        for date in dates:
            urls = get_urls(track, date)

            for race in urls:
                for horse in parse_horses(race):
                    writer.writerow(horse)
#track = "ascot"
    #date = "20221103"
    #for url in get_urls(track, date):
    #    print(actual_winners(url))

