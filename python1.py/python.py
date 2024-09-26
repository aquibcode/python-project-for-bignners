def best_performers(overs: list) -> list:
    '''Given a list of dictionaries, generate a ranking board, based on wickets taken and economy of the bowler.
    The output should be list of tuples, sorted on the basis of ranking of bowler.

    Args:
        overs (list[dict]): list of dictionaries, where each dictionary represents the performance 
                            of a bowlers in a over. 

    Returns:
        list of tuples - where each entry has format: (bowler_name, wickets, economy_rate).
    '''
    bowlers = {}
    for over in overs:
        for bowler in over:
            if bowler not in bowlers:
                bowlers[bowler] = {'runs':0,'wicket':0,'overs':0}
            #updating wicket and runs;
            for ball in over[bowler]:
                if isinstance(ball,int):
                    bowlers[bowler]['runs'] +=ball

                elif ball =='w':
                    bowlers[bowler]['wicket'] +=1
                elif ball == 'wd':
                    bowlers[bowler]['runs'] +=1
                elif ball.startwith['Nb']:
                    bowlers[bowler]['runs']+=1+int(ball[-2])
            #updating over count
            bowlers[bowler]['overs']+=1
    return sorted([(bow,bowlers[bow]['wicket'], round(bowlers[bow]['runs']/bowlers[bow]['overs'],2)) for bow in bowlers],key=lambda x:(x[1],-x[2]), reverse=True)                         