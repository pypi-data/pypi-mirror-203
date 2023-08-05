from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import matplotlib.dates as mdates




def draw(data, title):
    dates = []
    date_labels = []
    counts = []

    for timestamp, count in data:
        count = int(count)
        timestamp = int(timestamp / 1000)
        dt_obj = datetime.fromtimestamp(int(timestamp))
        # print(dt_obj.strftime('%Y-%m-%d %H:%M'), count)
        dates.append(dt_obj)
        date_labels.append(dt_obj.strftime('%Y-%m-%d %H:%M'))
        counts.append(count)

    fig, ax = plt.subplots()
    fig.set_figwidth(16)
    fig.set_figheight(8)
    ax.plot(dates, counts, 'o-')
    # ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d %H:%M'))
    plt.xticks(rotation=45)
    # ax.set_xticks(dates)
    # ax.set_xticklabels(date_labels)
    plt.xlabel('Date')
    plt.ylabel('Email Count')
    plt.title(title)
    plt.savefig('ts.png', bbox_inches='tight')




def draw_histo(data, title):
    timestamps = [datetime.fromtimestamp(t/1000) for t, _ in data]
    values = [v for _, v in data]
    plt.hist(timestamps, bins=10, edgecolor='#000')
    plt.xlabel('Timestamp')
    plt.ylabel('Frequency')
    plt.title('Histogram of Timestamps')
    plt.savefig('hist.png', bbox_inches='tight')
