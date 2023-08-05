import os
import re
import argparse
import subprocess
import csv
from collections import Counter, defaultdict


def analyze_file(directory, file_path):
    print(f"Analyzing the file: {file_path}\n")

    process = subprocess.run(["pylint", file_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             universal_newlines=True, check=False)
    pylint_output = process.stdout

    alert_count = Counter()
    alert_details = defaultdict(list)

    alert_pattern = re.compile(r'([CRWEF]\d{4})')

    for line in pylint_output.split("\n"):
        match = alert_pattern.search(line)
        if match:
            alert_code = match.group(0)
            alert_type = alert_code[0]
            alert_count[alert_type] += 1
            alert_details[alert_type].append(alert_code)

    return alert_count, alert_details


def export_to_csv(table_data, headers, csv_output):
    software_data = {}
    for subdir_data in table_data:
        software_directory, file_path, total_alerts, convention, refactor, warning, error, fatal, alert_codes_str = subdir_data
        software_name = os.path.basename(software_directory)
        alert_codes = [code for code in alert_codes_str.split(", ") if code]

        if software_name not in software_data:
            software_data[software_name] = {
                'alert_counts': defaultdict(int),
                'alert_codes': set()
            }

        software_data[software_name]['alert_counts']['Total Alerts'] += total_alerts
        software_data[software_name]['alert_counts']['Convention'] += convention
        software_data[software_name]['alert_counts']['Refactor'] += refactor
        software_data[software_name]['alert_counts']['Warning'] += warning
        software_data[software_name]['alert_counts']['Error'] += error
        software_data[software_name]['alert_counts']['Fatal'] += fatal
        software_data[software_name]['alert_codes'].update(alert_codes)

    with open(csv_output, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(headers)
        for row in table_data:
            csv_writer.writerow(row)

        csv_writer.writerow(["Software Analysis"])
        for software_name, data in software_data.items():
            csv_writer.writerow([software_name])
            row = [data['alert_counts'][header] for header in headers[2:-1]]
            csv_writer.writerow(["Total Alerts", "Convention", "Refactor", "Warning", "Error", "Fatal"])
            csv_writer.writerow(row)
            csv_writer.writerow([])  # Add a blank line
            top_10_alert_codes = sorted(data['alert_codes'], key=lambda x: int(x[1:]))[:10]
            top_10_line = f"Top 10 Alert Codes by {software_name}: " + ", ".join(top_10_alert_codes)
            csv_writer.writerow([top_10_line])
            csv_writer.writerow([])  # Add a blank line

        # Find the 10 common alert codes among the software directories
        common_alert_codes = set.intersection(*(data['alert_codes'] for data in software_data.values()))
        top_10_common_alert_codes = sorted(common_alert_codes, key=lambda x: int(x[1:]))[:10]
        common_alert_codes_line = f"The 10 common alert codes between {', '.join(software_data.keys())}: " + ", ".join(top_10_common_alert_codes)
        csv_writer.writerow([common_alert_codes_line])


def main():
    parser = argparse.ArgumentParser(description="Analyze Python files in the specified directories.")
    parser.add_argument("-p", "--project", required=True, help="The project directory containing the subdirectories with Python files to analyze.")
    parser.add_argument("-s", "--subdirs", nargs='+', required=True, help="The list of subdirectories in the project directory, each representing a software.")
    parser.add_argument("-csv", "--csv_output", help="The path and file name for the CSV output.")
    args = parser.parse_args()

    project_directory = os.path.abspath(args.project)

    headers = ["Software Directory", "File Path", "Total Alerts", "Convention", "Refactor", "Warning", "Error", "Fatal", "Alert Codes"]

    table_data = []
    for subdir in args.subdirs:
        software_directory = os.path.join(project_directory, subdir)

        if not os.path.isdir(software_directory):
            print(f"The directory '{software_directory}' does not exist or is not a directory.")
            continue

        for root, _, files in os.walk(software_directory):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    alert_count, alert_details = analyze_file(software_directory, file_path)

                    alert_codes = []
                    for alert_type, codes in alert_details.items():
                        alert_codes.extend(codes)

                    row = [software_directory, file_path, sum(alert_count.values()), alert_count['C'], alert_count['R'], alert_count['W'], alert_count['E'], alert_count['F'], ', '.join(sorted(alert_codes))]
                    table_data.append(row)

    if args.csv_output:
        csv_output = os.path.abspath(args.csv_output)
        export_to_csv(table_data, headers, csv_output)


if __name__ == "__main__":
    main()
