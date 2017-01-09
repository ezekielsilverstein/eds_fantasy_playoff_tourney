from input_stats import read_in
from argparse import ArgumentParser


def calculate_points(team):
    """
    Inputs a team_stats dictionary from 'read_in' fcn
    Outputs the total value of stats in the dict
    
    :param team
    :return: number of points earned
    """
    
    points_dict, k_points_dict, dst_points_dict = point_values()
    
    point_total = 0
    
    for pos, stats in team.iteritems():
        if pos != 'name':
            positional_points = 0
            for stat, quantity in stats.iteritems():
                if pos in ['QB', 'RB1', 'RB2', 'WR1', 'WR2', 'WR3', 'TE']:
                    positional_points += quantity * points_dict[stat]
                elif pos == 'K':
                    positional_points += quantity * k_points_dict[stat]
                elif pos == 'D/ST':
                    if stat == 'PTs_allowed':
                        positional_points += 5 if quantity == 0 else 0
                        positional_points += 4 if 1 <= quantity <= 6 else 0
                        positional_points += 3 if 7 <= quantity <= 13 else 0
                        positional_points += 1 if 14 <= quantity <= 17 else 0
                        positional_points += 0 if 18 <= quantity <= 27 else 0
                        positional_points += -1 if 28 <= quantity <= 34 else 0
                        positional_points += -3 if 35 <= quantity <= 45 else 0
                        positional_points += -5 if quantity >= 46 else 0
                    else:
                        positional_points += quantity * dst_points_dict[stat]
            positional_points = round(positional_points, 1)
            point_total += positional_points
    return point_total


def point_values():
    """
    :return dictionaries with point values:
    """
    points_dict = {
        'TD_pass': 4,
        'YD_pass': 0.04,
        'two_pt_conversion_pass': 2,
        'INT_pass': -2,
        'TD_rush': 6,
        'YD_rush': 0.1,
        'two_pt_conversion_rush': 2,
        'TD_rec': 6,
        'YD_rec': 0.1,
        'recs': 1,
        'two_pt_conversion_rec': 2,
        'TD_kickoff_ret': 6,
        'TD_punt_ret': 6,
        'TD_fumble_rec': 6,
        'fumbles_lost': -2
    }
    
    k_points_dict = {
        'FG_0_39': 3,
        'FG_40_49': 4,
        'FG_50+': 5,
        'FG_miss': -1,
        'PAT': 1
    }
    
    dst_points_dict = {
        'TD_kickoff_ret': 6,
        'TD_punt_ret': 6,
        'TD_int_ret': 6,
        'TD_fumble_ret': 6,
        'PAT_return': 2,
        'PAT_safety': 1,
        'TD_block_kick_return': 6,
        'INT': 2,
        'fumble_recovery': 2,
        'block_kick': 2,
        'safety': 2,
        'sack': 1
    }
    
    return points_dict, k_points_dict, dst_points_dict


def main():
    parser = ArgumentParser()
    
    parser.add_argument('--filename', required=True,
                        help="Filename containing team's stats")
    
    args = parser.parse_args()
    
    team_stats = read_in(args.filename)
    
    points = calculate_points(team_stats)
    
    print "{0}'s players scored {1} points".format(team_stats['name'], points)


if __name__ == '__main__':
    main()
