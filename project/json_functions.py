def bgplay_table_source(bpgplay_result_dict):
    path_change_list = []
    for initial_state in bpgplay_result_dict['data']['initial_state']:
        previous_path = initial_state['path']
        for event in bpgplay_result_dict['data']['events']:
            if event['attrs']['source_id'] == initial_state['source_id'] and \
                    event['attrs']['target_prefix'] == initial_state['target_prefix']:
                if 'path' in event['attrs']:
                    if event['attrs']['path'] != previous_path:
                        path_event = {'source_id': event['attrs']['source_id'],
                                      'change_date': event['timestamp'],
                                      'target_prefix': event['attrs']['target_prefix'],
                                      'path_change': {}
                                      }

                        # find the ip address and AS number of the source
                        # which the BGP route is taken place in the event
                        source_ip, source_as = next((item['ip'], item['as_number'])
                                                    for item in bpgplay_result_dict['data']['sources']
                                                    if item["id"] == path_event['source_id'])
                        # find the source owner as name (ISP name etc.)
                        source_owner = next(item['owner'] for item in bpgplay_result_dict['data']['nodes']
                                            if item['as_number'] == source_as)

                        path_event['source_as'] = '<a href="#" data-toggle="tooltip" data-placement="top" ' \
                                                  'data-html="true" title="<b>Owner:</b> {}<br> <b>IP:</b> {}">' \
                                                  '{}</a>'.format(source_owner, source_ip, str(source_as))
                        path_event['source_ip'] = source_ip
                        path_event['source_owner'] = source_owner
                        path_event['path_change']['previous_path'] = previous_path
                        path_event['path_change']['transitioned_path'] = event['attrs']['path']
                        path_event['path_change_str'] = '<span class="my-w100">Previous: </span><em>{}</em><br>' \
                                                        '<span class="my-w100">Transitioned: </span>' \
                                                        '<em>{}</em>'.format(" ".join(map(str, previous_path)),
                                                                             " ".join(map(str, event['attrs']['path'])))
                        previous_path = event['attrs']['path']
                        path_change_list.append(path_event)
    return path_change_list