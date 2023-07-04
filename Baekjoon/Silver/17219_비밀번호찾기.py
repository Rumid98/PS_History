n, m = map(int, input().split())
site_dic = {}
for i in range(n):  # site pw info
    site_url, pw = input().split()
    site_dic[site_url] = pw
for i in range(m):  # find pw in info
    print(site_dic[input().strip()])
