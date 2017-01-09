import csv


def read_in(fname):
    """
    Reads in a textfile containing the stats of a participant's selected players
    
    :param fname:
    :return: dictionary of positions and their stats
    """
    
    with open(fname, 'rU') as f:
        team_stats = {}
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            pos = row[0]
            # print pos
            stats_dict = txt_to_dict(row)
            team_stats[pos] = stats_dict
            team_stats['name'] = fname.split('.')[0]
    
    return team_stats


def txt_to_dict(row):
    # stats
    stats = ['pos',
             'TD_pass',
             'YD_pass',
             'two_pt_conversion_pass',
             'INT_pass',
             'TD_rush',
             'YD_rush',
             'two_pt_conversion_rush',
             'TD_rec',
             'YD_rec',
             'recs',
             'two_pt_conversion_rec',
             'TD_kickoff_ret',
             'TD_punt_ret',
             'TD_fumble_rec',
             'fumbles_lost']
    
    k_stats = ['pos',
               'FG_50+',
               'FG_40_49',
               'FG_0_39',
               'PAT',
               'FG_miss']
    
    dst_stats = ['pos',
                 'TD_kickoff_ret',
                 'TD_punt_ret',
                 'TD_int_ret',
                 'TD_fumble_ret',
                 'PAT_return',
                 'PAT_safety',
                 'TD_block_kick_return',
                 'INT',
                 'fumble_recovery',
                 'block_kick',
                 'safety',
                 'sack',
                 'PTs_allowed']
    
    d = {}
    pos = row[0]
    
    if pos == 'D/ST':
        for i in range(1, len(dst_stats)):
            d[dst_stats[i]] = int(row[i])
    
    elif pos is 'K':
        for i in range(1, len(k_stats)):
            d[k_stats[i]] = int(row[i])
    
    elif pos is not 'K' and pos is not 'D/ST':
        for i in range(1, len(stats)):
            d[stats[i]] = int(row[i])
    
    return d
