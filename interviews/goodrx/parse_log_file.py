# The contents of the input file is an apache access log. It is on the file system at
# /home/coderpad/data/access.log.aa.

# Some of the fields available include: IP address, timestamp, HTTP request line, HTTP status code, and
# response size. For example:

#109.169.248.247 - - [12/Dec/2015:18:25:11 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
#109.169.248.247 - - [12/Dec/2015:18:25:11 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
#46.72.177.4 - - [12/Dec/2015:18:31:08 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
#46.72.177.4 - - [12/Dec/2015:18:31:08 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
#83.167.113.100 - - [12/Dec/2015:18:31:25 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
#83.167.113.100 - - [12/Dec/2015:18:31:25 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
#95.29.198.15 - - [12/Dec/2015:18:32:10 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
#95.29.198.15 - - [12/Dec/2015:18:32:11 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
#109.184.11.34 - - [12/Dec/2015:18:32:56 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"



# Task
# =====
# Given the dataset, produce a summary file (in any format suitable for machine parsing)
# containing the following data elements:
#
# - Number of requests for each status code
# - Top 10 most frequent URLs for each status code
# - Top 10 IPs for each status code


# Note the difference between the referrer URL vs the requested URL path.

from collections import defaultdict


log_file = open("/home/coderpad/data/access.log.aa").readlines()

counter = defaultdict(dict)
for line in log_file:
    line_splitted = line.split(" ")
    ip_address = line_splitted[0]
    status_code = line_splitted[8]
    url_path = line_splitted[6]

    if not counter.get("status_code"):
        counter["status_code"] = defaultdict(int)

    if not counter.get("urls"):
        counter["urls"] = {}

    # count status code
    counter["status_code"][status_code] +=1

    # do we urls in te counter dict?
    # if not, do we have the given status code for the url in the inner dict?
    # if not we increase it by one
    {
        "urls": {
            "200": {
                "/abc": 1,
                "/def": 2
            },
            "400": {
                "/abc": 1,
                "/def": 2
            }
        }
    }

    if not counter.get("urls"):
        counter["urls"] = {}

    if not counter.get("urls").get(status_code):
        counter["urls"][status_code] = {}
        counter["urls"][status_code][url_path] += 1


from collections import Counter
counter_obj = Counter(counter["urls"]["status_code"])
counter_obj = {
    "200": {
        "/abc": 1
    }
}
counter_obj.get(10)