import requests
import csv

url = "https://connectlogisticsapiprd.azurewebsites.net/odata/Suppliers/ConnectMobile.Web.AllWithinBounds(east=-85.47607058125,west=-141.50634401875,north=60.64288417027362,south=45.01431382682483)?$top=2000&$filter=SupplierType%20eq%20%27Liquor%20Store%27"

url = "https://connectlogisticsapiprd.azurewebsites.net/odata/Suppliers/?$filter=SupplierType%20eq%20%27Liquor%20Store%27"
url = "https://connectlogisticsapiprd.azurewebsites.net/odata/Suppliers/"
s = requests.session()


def getDealerInfo():
    r = s.get(url)
    if r.status_code != 200:
        print("An error has occured")
        return
    json = r.json()
    j = json["value"]
    dict_header = {}
    data = []
    for row in j:
        row.pop("GeoLocation", None)
        keys = row.keys()
        data.append(row)
        for k in keys:
            dict_header[k] = 1

    csv_file = "data.csv"
    fieldnames = dict_header.keys()
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)


getDealerInfo()

print("done")
