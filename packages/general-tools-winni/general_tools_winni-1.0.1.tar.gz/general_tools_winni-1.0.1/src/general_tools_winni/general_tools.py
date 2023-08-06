def application_loader(
        url='http://192.168.0.220', path='path-to-view', write_js=True, write_json=False,
        force_reload_medium=False):
    import json
    import os
    from urllib.request import urlopen, urlretrieve

    # Creates a folder "imports" in the same directory and loads the data to it.
    my_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'imports'))
    if not os.path.exists(my_path):
        os.makedirs(my_path)

    try:
        # JSON structure
        # any... can be left out or repeated, the other should be present
        # after loading this script
        # - only handles the top-level data section
        # - removes the medium from the json after loading
        # The json form:
        # {
        #     "data": {
        #         "any_keys_or_not": ['OBJECT'],
        #         "mediums": []
        #     },
        #     "any_keys_or_not": ['OBJECT']
        # }

        my_json = json.loads(
            urlopen('{}/{}'.format(url, path)).read().decode()
        ).get('data', {})

        print('Got data. Now load mediums')
        for medium in my_json.get('mediums', []):
            destination = os.path.join(my_path, medium[1:])
            if not os.path.exists(os.path.dirname(destination)):
                os.makedirs(os.path.dirname(destination))
            if not os.path.exists(destination) or force_reload_medium:
                urlretrieve('{}/{}'.format(url, medium), destination)

        if write_js:
            f = open(os.path.join(my_path, 'data.js'), 'w')
            f.write('window.data = {};'.format(json.dumps(my_json, indent=4)))
            f.close()

        if write_json:
            f = open(os.path.join(my_path, 'data.json'), 'w')
            f.write('{}'.format(json.dumps(my_json, indent=4)))
            f.close()

    except:
        import traceback
        traceback.print_exc()
        # Error occurred
        print('Error')
        return False
