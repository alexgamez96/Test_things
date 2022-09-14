import time
import requests
import json
import base64

authkey = ""
vos_host = ""
dst_profile = ""
new_dst_profile = ""
api_endpoint = ""


def get_creds(config_file):
    with open(config_file, "r") as config:
        """Retrieve information from 'config_file' file and return credentials base64 encoded"""
        global vos_host
        global dst_profile
        global new_dst_profile
        global authkey
        global api_endpoint
        fields_json = dict(json.load(config))
        vos_user = fields_json["vos_user"]
        vos_password = fields_json["vos_pass"]
        vos_host = fields_json["vos_host"]
        dst_profile = fields_json["destination_profile"]
        new_dst_profile = fields_json["new_destination_profile"]
        api_endpoint = "https://" + vos_host + "/vos-api/configure/v1/destinations"
        authkey = base64.b64encode(bytes(vos_user + ":" + vos_password)).decode()
        config.close()
        return vos_host, dst_profile, new_dst_profile, authkey, api_endpoint


def get_destinations():
    """Retrieve destinations with type=Origin and call 'change_dst_profile' to replace with new profile"""
    destinations_data = json.loads(response.text)
    back_up_destination(data=destinations_data)
    print("Changing destination profile...")
    for destination in destinations_data:
        if destination["destinationProfileId"] == dst_profile:
            change_dst_profile(dst=destination)


def back_up_destination(data):
    """Back up all destinations in cluster"""
    with open("all_destinations.json", "w") as r:
        r.write(json.dumps(data))
        r.close()
    print("\nBacked up all destinations in 'all_destinations.json'\n")


def change_dst_profile(dst):
    """Replace destinations with new profile"""
    dst["destinationProfileId"] = new_dst_profile
    dst_data_j = json.dumps(dst, indent=4)
    response_put = requests.put(api_endpoint + "/" + dst["id"], data=dst_data_j,
                                headers={"Content-Type": "application/json", "Authorization": "Basic " + authkey})
    if response_put.status_code != 200:
        print("Failed to update {}. VOS returned {}".format(dst["name"], response_put.status_code))
        dst_failed.append(dst["name"])
        time.sleep(1)
    else:
        print(dst["name"])
        num_dst.append(dst)
        time.sleep(1)


get_creds(config_file="config_file")
print("\nChanging destination profile in {}.".format(vos_host))
time.sleep(3)
dst_failed = []
num_dst = []
response = requests.get(api_endpoint, headers={"Content-Type": "application/json",
                                               "Authorization": "Basic " + authkey})

if response.status_code == 200:
    get_destinations()
    print ("\n{} destinations have been changed\n".format(len(num_dst)))
else:
    print("\nUnable to retrieve the data. VOS response is {}".format(response.status_code))

if len(dst_failed) > 0:
    print("The below destinations failed to update: \n{}".format(dst_failed))
