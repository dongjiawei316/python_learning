import requests

#执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("status code:", r.status_code)

#将API响应存储在一个变量中
response_dict = r.json()

#处理结果
print(response_dict.keys())
print("Total repositories :", response_dict['total_count'])

#返回了多少个仓库
repo_dicts = response_dict["items"]
print("Return repos : ", len(repo_dicts))

for repo_dict in repo_dicts:
    print("\n Selected information about each repository")
    print("Name : ", repo_dict['name'])
    print("Owner : ", repo_dict['owner']['login'])
    print("Stars : ", repo_dict['stargazers_count'])
    print("Repository : ", repo_dict['html_url'])
    print("Created at : ", repo_dict['created_at'])
    print("Updated at : ", repo_dict['updated_at'])
    print("Description : ", repo_dict['description'])


#for key in sorted(repo_dict.keys()):
#    print(key)


