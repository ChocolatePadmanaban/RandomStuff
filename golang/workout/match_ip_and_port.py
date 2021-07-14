import csv
import os

def convert_to_csv(input_k8s_txt, output_ip):
    with open(input_k8s_txt, 'r') as Input_k8s_txt:
        with open(output_ip, 'w', newline='') as Output_ip: 
            for i, line in enumerate(Input_k8s_txt):
                nodedata= line.split()
                ipwriter = csv.writer(Output_ip, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                ipwriter.writerow([nodedata[0].replace('aserv',''),nodedata[5].split(':')[-1].split('/')[0]])


def csv_to_csv(labels_with_ips , ns_with_port):
    label_with_ip_dict = {}
    with open(labels_with_ips, newline='')as  csvfile:
        ipreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in ipreader:
            label_with_ip_dict[row[-1].replace('slavens=','')]=row[1]
    #print(label_with_ip_dict)
    with open(ns_with_port, newline='')as  csvfile:
        portreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in portreader:
            print(label_with_ip_dict[row[0]]+','+row[1])
        



if __name__ == '__main__':
    csv_to_csv('labels_with_ips.csv', 'ns_with_port.csv')