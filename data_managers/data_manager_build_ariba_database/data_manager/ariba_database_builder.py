# Thanh Le Viet
# 7-Jan-2019

import argparse
import json
import os
import shutil


def main(args):
    output_path = os.getcwd()
    db_folder = [d for d in os.listdir(output_path) if os.path.isdir(d)]
    params = json.loads(open(args.output).read())
    target_directory = params['output_data'][0]['extra_files_path']
    os.mkdir(target_directory)
    data_manager_entry = []
    for db in db_folder:
        print("Current: ".format(os.path.join(output_path, d)))
        print("Target: {}".format(target_directory))
        shutil.move(os.path.join(output_path, d), os.path.join(target_directory, d))
        data_manager_entry.append(dict(value=db.lower(),
                                  name=db,
                                  path=target_directory)
                                    )
    data_manager_json = dict(data_tables=dict(ariba_databases=data_manager_entry))
    file(args.output, 'w').write(json.dumps(data_manager_json))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create data manager json.')
    parser.add_argument('--out', dest='output', action='store', help='JSON filename')
    args = parser.parse_args()
    main(args)