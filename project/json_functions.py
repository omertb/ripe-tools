def bgplay_table_source(bpgplay_result_dict):
    path_change_list = []
    for initial_state in bpgplay_result_dict['data']['initial_state']:
        previous_path = initial_state['path']
        for event in bpgplay_result_dict['data']['events']:
            if event['attrs']['source_id'] == initial_state['source_id'] and \
                    event['attrs']['target_prefix'] == initial_state['target_prefix']:
                if 'path' in event['attrs']:
                    if event['attrs']['path'] != previous_path:
                        path_event = {'source_id': event['attrs']['source_id'], 'change_date': event['timestamp'],
                                      'target_prefix': event['attrs']['target_prefix'], 'path_change': {}}
                        path_event['path_change']['previous_path'] = previous_path
                        path_event['path_change']['transitioned_path'] = event['attrs']['path']
                        path_event['path_change_str'] = "Previous: {} \n Transitioned: {}".format(" ".join(map(str, previous_path)),
                                                                                                  " ".join(map(str, event['attrs']['path'])))
                        previous_path = event['attrs']['path']
                        path_change_list.append(path_event)
    return path_change_list