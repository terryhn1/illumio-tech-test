import csv
import json
from collections import defaultdict

class FlowLogFileParser:

    def __init__(self, filePath : str):
        with open(filePath, "r") as file:
            self._logs = []
            for line in file.readlines():
                self._logs.append(line.rstrip())
            
    """
        This function collects the destination port and the protocol index and sets them into a list of tuple of size 2.
    """
    def get_line_data(self) -> list[tuple[2]]:
        log_data = []
        destination_port_index, protocol_index = 6, 7
        with open('protocols.json', 'r') as json_file:
            protocols = json.load(json_file)
        for line in self._logs:
            segmented_entry = line.split()
            log_data.append((segmented_entry[destination_port_index], str(protocols[segmented_entry[protocol_index]]).lower()))

        return log_data

"""
    Parses the lookup table and creates csv files after matching with the log data
"""
class CsvLookupTableParser:

    def __init__(self, filePath: str):
        self._mapper = defaultdict(dict)
        with open(filePath, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                self._mapper[line[0]][line[1]] = line[2]
            
    
    def get_match_tag_count(self, log_data: list[tuple[2]]) -> defaultdict[int]:
        tag_counter = defaultdict(int)

        for line in log_data:
            try:
                tag_counter[self._mapper[line[0]][line[1]]] += 1
            except KeyError:
                tag_counter["Untagged"] += 1
        
        return tag_counter

    def create_tag_count_csv(self, default_dict: defaultdict[int]) -> None:
        with open('tag_count.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Tag', 'Count'])
            for key, value in default_dict.items():
                writer.writerow([key, value])

    def get_port_portocol_count(self, log_data: list[tuple[2]])-> defaultdict[int]:
        tag_counter = defaultdict(int)

        for line in log_data:
            tag_counter[line[0] + ',' + line[1]] += 1

        return tag_counter

    
    def create_port_protocol_count_csv(self, default_dict: defaultdict[int]) -> None:
        with open('port_portcol_count.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Port', 'Protocol', 'Count'])
            for key, value in default_dict.items():
                port_protocol = str(key).split(',')
                writer.writerow([port_protocol[0], port_protocol[1], value])






if __name__ == "__main__":
    flow_log_path = input("Please type out the file to use for the flow logs: ")
    flow_log_parser = FlowLogFileParser(flow_log_path)
    log_data = flow_log_parser.get_line_data()

    csv_log_path = input("Please type out the file to use for the lookup table: ")
    csv_table_parser = CsvLookupTableParser(csv_log_path)
    match_tag_count = csv_table_parser.get_match_tag_count(log_data)
    port_protocol_count = csv_table_parser.get_port_portocol_count(log_data)
    csv_table_parser.create_port_protocol_count_csv(port_protocol_count)
    
